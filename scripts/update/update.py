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

import os
import re
import fileinput

VERSION_REGEX = "[0-9]+.[0-9]+.[0-9]+"
ANSIBLE_IMAGE_VERSION = "ANSIBLE_IMAGE_VERSION"
VERSIONS_SH = "versions.sh"


def _update_versons_in_git(new_version):
    os.system("git commit -m'Ansible Version Updated to v{}' -a".format(new_version))
    os.system('git push --quiet origin HEAD:production')
    os.system("git tag {}".format(new_version))
    os.system('git push --tags')


def _get_latest_ansible_version():
    ansible_version_env = os.popen('yolk -V ansible').read()
    return re.search(VERSION_REGEX, ansible_version_env).group()


def _ansible_image_version_exists(line):
    return re.search(ANSIBLE_IMAGE_VERSION, line)


def _replace_line_if_image_version(new_version, line):
    updated = False
    current_version = re.search(VERSION_REGEX, line).group()
    if (current_version != new_version):
        print("export {}={}".format(ANSIBLE_IMAGE_VERSION, new_version))
        updated = True
    else:
        print(line)
    return updated


def _replace_outdated_versions(new_version):
    updated = False
    for line in fileinput.input(VERSIONS_SH, inplace=True):
        if(_ansible_image_version_exists(line)):
            updated = _replace_line_if_image_version(new_version, line) or updated
        else:
            print(line, end='')
    return updated


def main():
    version_number = _get_latest_ansible_version()
    updated = _replace_outdated_versions(version_number)
    if updated:
        print("New Version: {}".format(version_number))
        _update_versons_in_git(version_number)
    else:
        print("No Version Update")


if __name__ == "__main__":
    main()
