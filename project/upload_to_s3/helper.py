from .. import app
from ..resources import _get_s3_client
from flask import redirect

ALLOWED_EXTENSIONS = set(['txt', 'md', 'markdown', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(name):
    return "." in name and name.split(".")[1].lower() in ALLOWED_EXTENSIONS

# Connect and upload to s3

def upload_file_to_s3(file, bucket_name, folder='test_user', poll='test_poll', image='id'):
    """
    Docs: http://boto3.readthedocs.io/en/latest/guides/s3.html
    """
    s3 = _get_s3_client()
    try:
        file_path = "{}/{}/{}/{}".format(folder, poll, image, file.filename)
        s3.upload_fileobj(
            file,
            bucket_name,
            file_path
        )
        s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 
                                                        'Key': file_path},
                                  ExpiresIn=604800)
    except Exception as e:
        print("Something happened:", e)
        return e


def generate_file_url(file, bucket_name, folder='test_user', poll='test_poll', image='id'):
    s3 = _get_s3_client()
    try:
        file_path = "{}/{}/{}/{}".format(folder, poll, image, file.filename)
        url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name,
                                                              'Key': file_path},
                                        ExpiresIn=604800)
    except Exception as e:
        print("Something happened:", e)
        return e
    return url