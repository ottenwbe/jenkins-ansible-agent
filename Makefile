NAME := jenkins-ansible-agent
VERSION := 0.1.0
BASE_IMAGE_TAG := latest
BUILD_DATE := $(shell date +'%y.%m.%d %H:%M:%S')
REPO := ottenwbe

docker: ## Create the ansible docker image
	docker build --build-arg BASE_IMAGE_TAG=$(BASE_IMAGE_TAG) --label "version=${VERSION}" --label "build_date=${BUILD_DATE}"  --label "maintainer=Beate Ottenwaelder <ottenwbe.public@gmail.com>" -t $(REPO)/$(NAME):$(VERSION) .

docker-push: ## Publish the image on https://hub.docker.com
	docker push $(REPO)/$(NAME):$(VERSION)

help: ## Print all commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
