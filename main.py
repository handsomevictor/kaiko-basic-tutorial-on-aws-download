from download_from_aws import AwsS3VictorTool


def main_aws_s3():
    bucket_name = 'your-bucket-name'
    folder_name = 'folder/directory/you/want/to/download'

    download_files_server = AwsS3VictorTool(bucket_name, login=True)
    download_files_server.download_all_file_names_in_folder(folder_name)
    download_files_server.download_files_from_s3_concurrent(max_workers=7,
                                                            file_type='csv.gz')


if __name__ == '__main__':
    main_aws_s3()
