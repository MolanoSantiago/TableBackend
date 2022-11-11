""" import os


BUCKET_NAME = os.environ.get("bucketName", "")
BASE_PATH = os.environ.get("basepath", "")
ARN_SECRET_ODS = os.environ.get("arnSecretOds", "")
ARN_SECRET_RTB_COL = os.environ.get("arnSecretRtbCol", "")
ARN_SECRET_OZONO = os.environ.get("arnSecretOzono", "")
ARN_EXCHANGE_RATE_AUTH = os.environ.get("arnExchangeRateAuth", "")
URL_EXCHANGE_RATE_API = os.environ.get("urlExchangeRateApi", "")
URL_EXCHANGE_RATE_AUTH = os.environ.get("urlExchangeRateAuth", "")
REGION = os.environ.get('region',"") """