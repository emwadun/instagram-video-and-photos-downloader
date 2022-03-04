'''
* We will create an app to download instagram photos and videos.
* We will use:
 - Python Selenium : To control the browser.
 - Flask : Python web framework.
* we will create this in a virtual environment named  'instaapp':
   #python -m venv instaapp
   #.\instaapp\Scripts\activate
* we will install flask library using pip:
    #pip install flask
    #pip list 
    Package      Version
    ------------ -------
    click        8.0.4
    colorama     0.4.4
    Flask        2.0.3
    itsdangerous 2.1.0
    Jinja2       3.0.3
    MarkupSafe   2.1.0
    pip          22.0.3
    setuptools   41.2.0
    Werkzeug     2.0.3
'''

from flask import Flask, render_template, url_for

instagramAPP = Flask(__name__)

@instagramAPP.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    instagramAPP.run(debug=True)