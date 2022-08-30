
# FastAPI
![alt tag](https://github.com/github/llraekll/blob/assets/fastapi.png?raw=True)
https://github.com/llraekll/FastAPI/blob/main/images/fastapi.png
https://github.com/github/llraekll/blob/assets/fastapi.png

This project is built on FastAPI framework based on a social media platform performing actions such actions User and Post creation using Postgres database, user authentication using hashed passwords and issusing JWT tokens hosting on Heroku, setting up and deploying on a Virtual Machine, creating CI/CD pipeline with github jobs.
* User creation
* User authentication    
* User login timeout with JWT tokens
* Creating Post linked to the user table
* Reading a Post
* Updating a Post
* Deleting a Post
* Voting a Post  



### Deploy on Heroku
https://github.com/github/llraekll/blob/assets/Heroku.png 
* Create a Procfile mentioning your app’s web server
* Create a requirements.txt file for Heroku to identify the language
* Ensure there are no unused libraries mentioned in the source code
* Add and commit source code, create a Heroku remote as mentioned on Heroku
* Deploy your code 

```bash
    git push heroku main
```

https://github.com/github/llraekll/blob/assets/DigitalOcean.png 

### Deploy on Ubuntu VM
* Create a droplet on digital ocean
* login into your VM using command promt/ windows terminal
```bash
    ssh root@IP address
```
* Configure user with admin rights 
* Python3 comes pre-installed 
* Install PIP and Postgres
* Configure config files on the VM
* Setup the database using postgres
* Make a directory to clone your github repo
* Link your domain to the IP address of your droplet
https://github.com/github/llraekll/blob/assets/ubuntu.png 
