from flask import Flask
from config import Comfig

app = Flask(__name__)
app.config.from_object(Config)

import app