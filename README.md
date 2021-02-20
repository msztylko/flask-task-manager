# flask-task-manager
A simple Task Manager website in Flask

This is my first project with Flask but definitely not the last one! I treat it mainly as a reference/starting point for the next projects.

## INSTALL

If you want to try it yourself just run:

1. `git clone https://github.com/msztylko/flask-task-manager.git && cd flask-task-manager`
2. `python3 -m virtualenv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `flask run`

### Run with Docker
After cloning the repo:
1. `docker build -t flask-task-manager .`  
2. `docker run -p 5000:5000 flask-task-manager`

When you see that the app is running in your terminal go to `localhost:5000` in your browser
