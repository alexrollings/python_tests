from flask import Flask

# application object is created as an instance od the flask package
# __name__ is set to the name of the module in which it is used
app = Flask(__name__)

from app import routes