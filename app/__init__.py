
from flask import Flask

app = Flask(__name__)
app.secret_key = 'your_session_key'

from app.views import main_views