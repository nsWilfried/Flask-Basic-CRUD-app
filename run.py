from app.main import app
from app.models import init_db


@app.cli.command()
def init():
    init_db()


if __name__ == '__main__':
    app.run(debug=True)