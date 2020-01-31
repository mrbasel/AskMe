from application import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

# if __name__ == '__main__':
<<<<<<< HEAD
    # app.run(debug=True)
=======
    # app.run()
>>>>>>> 9e27f16740eae84415a39a5a7e6b8d604107b148
