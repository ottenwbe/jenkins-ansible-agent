# jenkins-ansible-agent

A docker ssh agent for Jenkins that allows you to run ansible scripts. 


## Docker Images

[Images](https://hub.docker.com/r/ottenwbe/jenkins-ansible-agent) are hosted on [Docker Hub](https://hub.docker.com/) and can be used with the [Jenkins Docker Plugin](https://wiki.jenkins.io/display/JENKINS/Docker+Plugin).

```
docker pull ottenwbe/jenkins-ansible-agent
```

## Build

### Local Build

Use the Makefile to build the Docker image locally.

```
make docker
```

### Docker Automated Build

Docker hub's automated builds are configured to create the images.

It will automatically create a docker tag based on the git branch/tag:

| git branch/tag    | docker tag        |  
|---                | ---               |
| master            | testing           |  
| feature/*         | testing           |  
| \<sem-ver-tag\>     | 0.1.2  + latest   |  

## Vesion Update

To automatically check for version updates of ansible we provide a small python script.

    python3 update/update.py 

## License 

```
MIT License
```

As with all Docker images, these likely also contain other software which may be under other licenses.