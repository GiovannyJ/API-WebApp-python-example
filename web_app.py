from cgitb import html
from ctypes import c_ssize_t
from flask import Flask, render_template, redirect, url_for, request, flash

'''
The same premise can be done for a web app
a web app is very similar to an API but the difference is that the data being served is HTML data rather than
JSON. In this simple example i can render out different pages depending on what endpoint and method I goto.
The templates can also be filled with data (not shown bc im lazy). You are basically running a web server using python
in this way u can also take data from things like forum submissions and such and interact with them accordingly


some resources to learn ab the flask framework
https://flask.palletsprojects.com/en/3.0.x/
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
'''



#app is a flask object
app = Flask(__name__)

#when you run the page this is the first directory that we go to
@app.route('/', methods=['POST', 'GET'])
def landingpage():
    if request.method == "GET":
        return render_template("landingpage.html")



if __name__ == "__main__":
    app.run(debug=True)