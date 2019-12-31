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

## GitHub Actions

Github Action Workflows are are configured to 
1. automatically update the docker build configuration, i.e., __versions.sh__ with the latest ansible version (TODO)
1. automatically test the update script for  the docker configuration 
1. create and publish the docker images

    1. It will automatically create a docker tag based on the git branch/tag (TODO):

        | git branch/tag    | docker tag     |  
        |---                | ---            |
        | master            | testing        |  
        | feature/*         | testing        |  
        | \<sem-ver-tag\>     | \<sem-ver-tag\>  + latest   |  

## Vesion Update

To automatically check for version updates of ansible we provide a small python script.

    python3 update/update.py 

## License 

```
MIT License
```

As with all Docker images, these likely also contain other software which may be under other licenses.