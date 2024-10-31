import s3fs
from utils.constants import AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY
import pandas as pd
def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(key= AWS_ACCESS_KEY,secret=AWS_SECRET_ACCESS_KEY)
        return s3
    except Exception as e:
        print(e)

def create_bucket_if_not_exist(s3: s3fs.S3FileSystem, bucket:str):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print("Bucket created")
        else :
            print("Bucket already exists")
    except Exception as e:
        print(e)


# def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket:str, s3_file_name: str):
#     try:
#         s3.put(file_path, bucket+'/'+ s3_file_name)
#         print('File uploaded to s3')
#     except FileNotFoundError:
#         print('The file was not found')
        
        
def upload_data_to_s3(s3: s3fs.S3FileSystem, new_data: pd.DataFrame, bucket: str, s3_file_name: str):
    s3_path = f"{bucket}/{s3_file_name}"

    if s3.exists(s3_path):
        with s3.open(s3_path, 'a') as f:
            new_data.to_csv(f, header=False, index=False)
        print(f"Data has been added to {s3_path}.")
    else:
        with s3.open(s3_path, 'w') as f:
            new_data.to_csv(f, index=False)
        print(f"New file has been created and Data has been added to {s3_path}.")
                