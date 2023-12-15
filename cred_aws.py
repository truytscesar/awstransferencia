import boto3

# Configura as credenciais diretamente (não recomendado para produção)
boto3.setup_default_session(
    aws_access_key_id='AKIAYIKCTZ2IPFMDFY4Q',
    aws_secret_access_key='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',
    region_name='sa-east-1'
)

from botocore.exceptions import NoCredentialsError

def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a pre-signed URL to upload a file."""
    # Create a S3 client
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('put_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except NoCredentialsError:
        print("Credentials not available")
        return None

    return response

# COLOCAR O NOME DO BUCKET
bucket_name = 'tranfdedados'
# COLOCAR O NOME DO ARQUIVO
object_name = 'fotos.jpeg'
presigned_url = create_presigned_url(bucket_name, object_name, 3600)
print(presigned_url)