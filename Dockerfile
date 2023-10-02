# MIT License
# 
# Copyright (c) 2019 Beate Ottenwälder
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

ARG BASE_IMAGE_TAG
FROM docker.io/jenkins/agent:${BASE_IMAGE_TAG}

ARG ANSIBLE_VERSION

USER root

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y --no-install-recommends install python3 python3-pip python3-wheel python3-setuptools python3-venv git \
    && python3 -m venv /opt/ansible \
    && /opt/ansible/bin/pip install ansible==${ANSIBLE_VERSION} \    
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

ENV PATH="/opt/ansible/bin:$PATH"

USER jenkins