#!/bin/sh

#set info variable values
SECRET_ARTIFACT=`aws secretsmanager get-secret-value --secret-id dev/360energy/codeartifact --query SecretString --output text`
DOMAIN=$(echo $SECRET_ARTIFACT | jq -r '.DOMAIN')
DOMAIN_OWNER=$(echo $SECRET_ARTIFACT | jq -r '.DOMAIN_OWNER')
REPOSITORY=$(echo $SECRET_ARTIFACT | jq -r '.REPOSITORY')


#login
aws codeartifact login --tool pip --repository $REPOSITORY --domain $DOMAIN --domain-owner $DOMAIN_OWNER --region us-east-1

#install
pip install lib-llm==0.1.1
