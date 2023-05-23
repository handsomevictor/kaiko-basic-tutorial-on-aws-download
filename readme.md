Basic AWS Cli commands:

# AWS CLI: Download all files of some date from S3 bucket to local:
```
aws s3 sync s3://your-s3-bucket-name /local/directory --exclude "*" --include "*.csv"
```
The above command downloads all csv files, similarly:

```
aws s3 sync s3://your-s3-bucket-name /local/directory --exclude "*" --include "2023-05-20"
```
This command downloads all csv files of date 2023-05-20.


# Use Python Script to download:

Please refer to the file: download_from_aws.py and run main.py when you want to download anything.

[Alert] The overall logic is like this:
1. Establish connection to your AWS account by using "boto3" module and "resource" or "client" function 
2. (If you have the full path of the files wanted, ignore this step) Use the function "cli.list_objects_v2(**kwargs)"
   to list all files in your S3 bucket, and save the names that you want to download in a txt file
3. Read the txt file created in Step 2 and download all files in the list by iterating through the list. In my script
   download_from_aws.py, I am using concurrency to download, which is usually faster.

Reminder:
1. This script is only for aws accounts that didn't enable MFA. If MFA is enabled, then you should add something more in
   the script. Please contact zhenning.li@kaiko.com
2. The download_from_aws.py script will automatically create a folder to store all the data downloaded, in the same
   structure as they are in S3 bucket.
