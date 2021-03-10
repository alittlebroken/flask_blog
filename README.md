# Flask Blog
> A very basic blog written in python and flask.
>
> The initial base was app created by following the excellent tutorial written by Abdelhadi Dyouri [here](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)
>
<hr>

<!-- # Table of contents
* [Team Members](#teammembers)
-->

# Setup
* Create the initial project folder
```bash
cd /projects/
mkdir flask_blog
cd flask_blog
```

* Create a new python virtual environment & activate it
```bash
python -m venv venv
source venv/bin/activate
```

* Install required python libraries
```bash
pip install flask
```

* Clone the flask_blog repo
```bash
git clone https://github.com/alittlebroken/flask_blog.git
```

* Create the sqlite3 database
```bash
python init_db.py
```

* Run the flask app
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

* Copy and paste the URL provided into your favourite browsers address bar
