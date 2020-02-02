from application import create_app, db
from flask import current_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
