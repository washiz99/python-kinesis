import boto3


session = boto3.session.Session(
    aws_access_key_id = 'my-access-key',
    aws_secret_access_key = 'my-secret-access-key'
)


def show_s3bucket():

    s3 = session.resource(
        's3',
        region_name='ap-northeast-1',
        endpoint_url='http://localhost:4566'
    )
    bucket = s3.Bucket('test-bucket')
    print(bucket.name)

    PUT_OBJECT_KEY_NAME = 'hayate.txt'

    obj = bucket.Object(PUT_OBJECT_KEY_NAME)

    body = """盛岡〜新函館北斗 1往復
    新青森〜新函館北斗 1往復
    """

    response = obj.put(
        Body=body.encode('utf-8'),
        ContentEncoding='utf-8',
        ContentType='text/plane'
    )

def put_kinesis():

    kinesis = session.client(
        'kinesis',
        region_name='ap-northeast-1',
        endpoint_url='http://localhost:4566'
    )

    response = kinesis.put_record(
        StreamName = "python-test-stream",
        Data = "test1-test2-test3",
        PartitionKey = "123",
    )
    print(response)

if __name__ == '__main__':
    # show_s3bucket()
    put_kinesis()
