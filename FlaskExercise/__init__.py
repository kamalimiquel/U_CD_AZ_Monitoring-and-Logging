import logging
from flask import Flask

app = Flask(__name__)
wsgi_app = app.wsgi_app
# TODO: Set the app's logger level to "warning"
#   and any other necessary changes
#Flask doesn't output regular print statements 
#but the logger contained within a Flask app does output to syst.stderr
app.logger.setLevel(logging.WARNING) #set logging to WARNNG level
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING) #adapting the streamHandler to pay attention to warnings and above
app.logger.addHandler(streamHandler)#we add the Handler to our app.logger object

import FlaskExercise.views