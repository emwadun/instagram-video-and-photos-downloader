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

#Once you access the page on http://127.0.0.1:5000/, the page loads then
#You are prompted your instagram username and password.
#Then the download begins.
#Once the download completes a message from the rendered index.html is displayed showing that download is complete.

@instagramAPP.route("/")
def home():
    import instagramAutomation
    return render_template("index.html")

if __name__ == "__main__":
    instagramAPP.run(debug=True)