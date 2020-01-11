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
1. automatically update the docker build configuration, i.e., __versions.sh__ with the latest ansible version (see update_ansible.yml)
1. automatically test the update script for the docker configuration (see ci_update_app.yml)
1. create and publish the docker images (see docker_image.yml)

    1. It will automatically create a docker tag based on the git branch/tag:

        | git branch/tag  |  docker tag     |  description   |
        |---              | ---     | ---            |
        | master          |  \<sem-ver-tag\>  + latest        |  built on push + daily builds  |

## Vesion Update

To automatically update the ansible version we provide a small python script. This script is executed as part of the _Ansible Version Update_ workflow.

    python3 scripts/update/update.py 

## License 

```
MIT License
```

As with all Docker images, these likely also contain other software which may be under other licenses.