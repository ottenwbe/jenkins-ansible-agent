
NAME := jenkins-ansible-agent
BUILD_DATE := $(shell date +'%y.%m.%d %H:%M:%S')
REPO := ottenwbe

-include env.mk

env.mk: versions.sh
	sed 's/"//g ; s/=/:=/' < $< > $@

docker: versions.sh ## Create the ansible docker image form linux/amd64
	docker build \
	--build-arg BASE_IMAGE_TAG=$(JENKINS_IMAGE_TAG) \
	--build-arg ANSIBLE_VERSION=$(ANSIBLE_IMAGE_VERSION) \
	--label "version=${ANSIBLE_IMAGE_VERSION}" \
	--label "build_date=${BUILD_DATE}"  \
	--label "maintainer=Beate Ottenwaelder <ottenwbe.public@gmail.com>" -t $(REPO)/$(NAME):$(ANSIBLE_IMAGE_VERSION) .

docker-arm: versions.sh ## Create the ansible docker image for linux/arm/v7
	export DOCKER_CLI_EXPERIMENTAL=enabled ; \
	docker buildx build \
	--build-arg BASE_IMAGE_TAG=$(JENKINS_IMAGE_TAG) \
	--build-arg ANSIBLE_VERSION=$(ANSIBLE_IMAGE_VERSION) \
	--label "version=${ANSIBLE_IMAGE_VERSION}" \
	--label "build_date=${BUILD_DATE}" \
	--platform linux/arm/v7 --label "maintainer=Beate Ottenwaelder <ottenwbe.public@gmail.com>" \
	--push -f Dockerfile.armhf -t $(REPO)/$(NAME):armv7-$(ANSIBLE_IMAGE_VERSION) .

docker-test: versions.sh ## Create the ansible docker image
	docker run -d --name $(NAME)-test -v $(shell pwd)/tests:/tests $(REPO)/$(NAME):$(ANSIBLE_IMAGE_VERSION) 
	docker exec $(NAME)-test chmod +x /tests/run_test.sh	
	docker exec $(NAME)-test /tests/run_test.sh
	docker stop $(NAME)-test && docker rm $(NAME)-test	

docker-push: ## Publish the image on https://hub.docker.com
	docker push $(REPO)/$(NAME):$(ANSIBLE_IMAGE_VERSION)

help: ## Print all commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
