# aws-lambda-python-oracle

Skeleton program to get Oracle Instantclient running in an AWS Lambda function.

# Create an AWS Lambda Function

Login to your AWS console. Go to Lambda's. Create a new, blank lambda function. Name it "pythonOracleTest", and select Runtime Python 2.7.

Add the following encrypted environment variables:

	ORACLE_SID
	ORACLE_PORT
	ORACLE_HOST
	ORACLE_USER
	ORACLE_PASSWORD

See the code in lambda_function.py for reference. The program is using these environment variables to connect to Oracle, instead of a tnsnames.ora file.

# Get the Required Libraries

I used an Ubuntu EC2 instance to build the libraries. Go over to your Ubuntu machine.

Prerequisites:

zip and unzip (sudo apt-get install zip unzip)
python 2.7 and pip (google "ubuntu pip install")
make (you can just run the commands in the Makefile if you rather)

## Download the Oracle Instantclient

Download the following files from http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html into /tmp/instantclient/:

	instantclient-basiclite-linux.x64-12.1.0.2.0.zip
	instantclient-sdk-linux.x64-12.1.0.2.0.zip

## Get libaio

Run the following command to install it:

	sudo apt-get install -y libaio1

# Building and Deploying

Clone this repo:

        git clone git@github.com:landrey21/aws-lambda-python-oracle.git

        cd aws-lambda-python-oracle

Compile the instantclient and cx_Oracle:

	make

The Makefile expects the zip files to be in /tmp/instantclient. It also assumes you have the awscli installed and can connect. If you don't have the awscli setup you can manually upload the resulting zip. Instead of using "make install", run "make package". This will generate a file called lambda.zip. You can upload this file manually in the AWS console, for your lamdba. "make install" will upload the zip file to a lambda function called pythonOracleTest.

	make install

Notes:

lambda_function.py uses the default function "lambda_handler".



