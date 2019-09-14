import os
import re
import fileinput

VERSION_REGEX = "[0-9]+.[0-9]+.[0-9]+"
ANSIBLE_IMAGE_VERSION = "ANSIBLE_IMAGE_VERSION"
VERSIONS_SH = "versions.sh"


def get_latest_ansible_version():
    ansible_version_env = os.popen('yolk -V ansible').read()
    return re.search(VERSION_REGEX, ansible_version_env).group()


def replace_outdated_versions(new_version):
    for line in fileinput.input(VERSIONS_SH, inplace=True):
        if(re.search(ANSIBLE_IMAGE_VERSION, line) != None):
            current_version = re.search(VERSION_REGEX, line).group()
            if (current_version != new_version):
                print("ANSIBLE_IMAGE_VERSION={}".format(new_version))
            else:
                print(line)
        else:
            print(line, end='')



if __name__ == "__main__":
    version_number = get_latest_ansible_version()
    replace_outdated_versions(version_number)
    print(version_number)
