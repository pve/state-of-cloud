FROM alpine:latest
MAINTAINER pve@clubcloudcomputing.com 
LABEL vendor=www.clubcloudcomputing.com

RUN apk add --update py-pip
RUN apk add git

RUN git clone https://github.com/pve/state-of-cloud.git
RUN pip install --no-cache-dir -r state-of-cloud/requirements.txt

ENV AWS_DEFAULT_REGION eu-west-1
ENV AWS_ACCESS_KEY_ID secret
ENV AWS_SECRET_ACCESS_KEY secret

CMD ["python", "/state-of-cloud/aws.py"]
