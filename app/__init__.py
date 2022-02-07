from .models import init_db
from .main import app

@app.cli.command()
def init():
    init_db()