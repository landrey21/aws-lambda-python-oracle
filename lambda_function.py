import cx_Oracle
import os
import logging
import boto3
from botocore.exceptions import ClientError
from base64 import b64decode

# These ENV vars are encrypted with lambda/env
e_username = os.environ["ORACLE_USER"]
e_password = os.environ['ORACLE_PASSWORD']
e_host = os.environ['ORACLE_HOST']
e_port = os.environ['ORACLE_PORT']
e_sid = os.environ['ORACLE_SID']

username = boto3.client('kms').decrypt(CiphertextBlob=b64decode(e_username))['Plaintext']
password = boto3.client('kms').decrypt(CiphertextBlob=b64decode(e_password))['Plaintext']
host = boto3.client('kms').decrypt(CiphertextBlob=b64decode(e_host))['Plaintext']
port = boto3.client('kms').decrypt(CiphertextBlob=b64decode(e_port))['Plaintext']
sid = boto3.client('kms').decrypt(CiphertextBlob=b64decode(e_sid))['Plaintext']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    logger.info('begin lambda_handler')

    dsn = cx_Oracle.makedsn(host, port, sid)
    con = cx_Oracle.connect(username, password, dsn)
    cur = con.cursor()

    #logger.info('username: ' + username)
    #logger.info('host: ' + host)

    sql = """SELECT COUNT(*) AS TEST_COUNT FROM DUAL"""

    cur.execute(sql)
    columns = [i[0] for i in cur.description]
    rows = [dict(zip(columns, row)) for row in cur]
    logger.info(rows)

    con.close()
    logger.info('end lambda_handler')
    return "Successfully connected to oracle."
