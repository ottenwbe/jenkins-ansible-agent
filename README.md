# jenkins-ansible-agent

A docker ssh agent for Jenkins that allows you to run ansible scripts. 


## Docker Images

[Images](https://hub.docker.com/r/ottenwbe/jenkins-ansible-agent) are hosted on [Docker Hub](https://hub.docker.com/) and can be used with the [Jenkins Docker Plugin](https://wiki.jenkins.io/display/JENKINS/Docker+Plugin).

```
docker pull ottenwbe/jenkins-ansible-agent
```

## Build

## Local Build

Use the Makefile to build the Docker image locally.

```
make docker
```

## Docker Automated Build

Docker hub's automated builds are configured to create the images.