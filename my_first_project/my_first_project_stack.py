from aws_cdk import (
    aws_s3 as _s3,
    aws_iam as _iam,
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
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL
        )

        mybucket = _s3.Bucket(
            self,
            "myBucketId1"
        )

        snstopicname="abcdzys123"

        if not core.Token.is_unresolved(snstopicname) and len(snstopicname) > 10:
            raise ValueError("Maximum value can be only 10 characters")

        print(mybucket.bucket_name)

        _iam.Group(
            self,
            "gid"
        )

        output_1 = core.CfnOutput(
            self,
            "myBucketOutput1",
            value=mybucket.bucket_name,
            description=f"My First CDK Bucket",
            export_name="myBucketOutput1"
        )
