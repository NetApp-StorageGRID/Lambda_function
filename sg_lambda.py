from __future__ import print_function

import boto3
import logging
import ast
import glob
import uuid
import random
from urllib.parse import urlparse

ENDPOINT="https://webscaledemo.netapp.com"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    sgObj = event['Records'][0]['Sns']['Message']
    message = ast.literal_eval(sgObj)
    
    assetID = str(uuid.uuid4())
    sourceS3Bucket = message['Records'][0]['s3']['bucket']['name']
    sourceS3Key = message['Records'][0]['s3']['object']['key']
    sourceS3 =  ENDPOINT + '/'+ sourceS3Bucket + '/' + sourceS3Key #build a pre-signed URL in production
    
    logger.info("Source S3 Bucket : %s", sourceS3Bucket)
    logger.info("Source S3 Key : %s", sourceS3Key)
    logger.info("S3 Object Source : %s", sourceS3)
