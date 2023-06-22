
import os
class S3Sync:

    # save data from foldr to s3 bucket
    def sync_folder_to_s3(self,folder,aws_buket_url):
        command = f"aws s3 sync {folder} {aws_buket_url} "
        os.system(command)

    # get data from s3 bucket
    def sync_folder_from_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync  {aws_bucket_url} {folder} "
        os.system(command)

