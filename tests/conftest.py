from sys import modules
from fastapi.testclient import TestClient
from app.main import app
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db, Base
from app.oauth2 import create_access_token
import pytest
from app import models

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)


TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

# Base.metadata.create_all(bind=engine)

#Base= declarative_base()

# def override_get_db():
#    db = TestingSessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()

#app.dependency_overrides[get_db] = override_get_db


@pytest.fixture()
def session():
    print()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture()
def test_user2(client):
    user_data = {"email": "test2@yahoo.in", "password": "random"}
    res = client.post('/users/', json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture()
def test_user(client):
    user_data = {"email": "testone@yahoo.in", "password": "random"}
    res = client.post('/users/', json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client


@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [{
        "title": "first title",
        "content": "1st random",
        "owner_id": test_user['id']
    }, {
        "title": "second title",
        "content": "2nd random",
        "owner_id": test_user['id']
    }, {
        "title": "third title",
        "content": "3rd random",
        "owner_id": test_user['id']
    }, {
        "title": "first title",
        "content": "1st random",
        "owner_id": test_user2['id']
    }]

    def create_post_model(post):
        return models.Post(**post)
    post_map = map(create_post_model, posts_data)
    posts = list(post_map)

    session.add_all(posts)

    # session.add_all([models.Post(title="first title", content="1st random", owner_id=test_user['id']),
    #models.Post(title="second title", content="2nd random", owner_id=test_user['id']),
    # models.Post(title="third title", content="3rd random", owner_id=test_user['id'])])
    session.commit()

    posts = session.query(models.Post).all()
    return posts
