from upload_to_s3.server import app as application

if __name__ == '__main__':
    application.run(debug=True)