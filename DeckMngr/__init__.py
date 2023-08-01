from flask import Flask

app = Flask(__name__)
app.config.from_object("DeckMngr.config")

import DeckMngr.views
