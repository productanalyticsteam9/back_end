from project import app as application
# from project import db


if __name__ == "__main__":
    # db.create_all()
    application.run(debug=True)