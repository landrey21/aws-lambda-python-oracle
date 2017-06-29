SHELL=/bin/bash
.PHONY: init package install clean

# instantclient 12.1
INSTANT_CLIENT_ZIP_DIR=/tmp/instantclient
# extracts into this dir
INSTANT_CLIENT_DIR=instantclient_12_1

LAMBDA_ZIP=lambda.zip

export ORACLE_HOME=$(PWD)/lib/

init:
	unzip "$(INSTANT_CLIENT_ZIP_DIR)/instantclient*.zip" -d /tmp/ 
	mv /tmp/$(INSTANT_CLIENT_DIR)/ ./lib/
	ln -s ./libclntsh.so.12.1 ./lib/libclntsh.so
	cp /lib/x86_64-linux-gnu/libaio.so.1 ./lib/
	pip install cx_Oracle -t .;\

lambda.zip:
	zip -r $(LAMBDA_ZIP) lambda_function.py lib cx*

package: lambda.zip

install: lambda.zip
	aws lambda update-function-code --function-name pythonOracleTest --zip-file fileb://lambda.zip --publish

clean:
	rm -rf ./lib;
	rm -rf ./lambda.zip;
	rm -rf ./cx_Oracle*;
