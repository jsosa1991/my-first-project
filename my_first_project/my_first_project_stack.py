from aws_cdk import (
    aws_s3 as _s3,
    core
)

class MyFirstProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="mycdkbucketsosa120483001000",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS_MANAGED
        )
