import boto3
import os
from dotenv import load_dotenv
load_dotenv()

def get_r2_client():
    return boto3.client(
        's3',
        endpoint_url=f"https://{os.getenv('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
        aws_access_key_id=os.getenv("R2_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("R2_SECRET_ACCESS_KEY"),
        region_name=os.getenv("R2_REGION")
    )

def upload_to_r2(file_path, object_name):
    r2 = get_r2_client()
    bucket = os.getenv("R2_BUCKET_NAME")
    with open(file_path, "rb") as f:
        r2.upload_fileobj(f, bucket, object_name)
    account_url = os.getenv("R2_PUBLIC_URL")
    return f"{account_url}/{object_name}"