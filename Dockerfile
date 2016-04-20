FROM alpine-3
MAINTAINER pveijk@gmail.com 
LABEL vendor=www.clubcloudcomputing.com

ENV APPLICATION_USER  application
ENV APPLICATION_GROUP application


RUN /usr/local/bin/apk-install \
    # Install services
    openssh \

# Deploy scripts/configurations
COPY conf/ /opt/docker/
RUN bash /opt/docker/bin/control.sh provision.role.bootstrap webdevops-base-app \
    && bash /opt/docker/bin/bootstrap.sh

ENTRYPOINT ["/opt/docker/aws.py"]
CMD ["noop"]