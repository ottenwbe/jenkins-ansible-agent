
NAME := jenkins-ansible-agent
BUILD_DATE := $(shell date +'%y.%m.%d %H:%M:%S')
REPO := ottenwbe

-include env.mk

env.mk: versions.sh
	sed 's/"//g ; s/=/:=/' < $< > $@

docker: versions.sh ## Create the ansible docker image
	docker build --build-arg BASE_IMAGE_TAG=$(JENKINS_IMAGE_TAG) --build-arg ANSIBLE_VERSION=$(ANSIBLE_IMAGE_VERSION) --label "version=${ANSIBLE_IMAGE_VERSION}" --label "build_date=${BUILD_DATE}"  --label "maintainer=Beate Ottenwaelder <ottenwbe.public@gmail.com>" -t $(REPO)/$(NAME):$(ANSIBLE_IMAGE_VERSION) .

docker-test: versions.sh ## Create the ansible docker image
	docker run $(REPO)/$(NAME):$(ANSIBLE_IMAGE_VERSION) tests/run_test.sh

docker-push: ## Publish the image on https://hub.docker.com
	docker push $(REPO)/$(NAME):$(ANSIBLE_IMAGE_VERSION)

help: ## Print all commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
