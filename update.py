import os
import re
import fileinput

VERSION_REGEX = "[0-9]+.[0-9]+.[0-9]+"
ANSIBLE_IMAGE_VERSION = "ANSIBLE_IMAGE_VERSION"
VERSIONS_SH = "versions.sh"


def update_versions_in_git(new_version):
    os.system("git commit -m'Ansible Updated to v{}'".format(new_version))
    os.system('git push')
    os.system("git tag {}".format(new_version))
    os.system('git push --tags')

def get_latest_ansible_version():
    ansible_version_env = os.popen('yolk -V ansible').read()
    return re.search(VERSION_REGEX, ansible_version_env).group()


def replace_outdated_versions(new_version):
    updated = False
    for line in fileinput.input(VERSIONS_SH, inplace=True):
        if(re.search(ANSIBLE_IMAGE_VERSION, line) != None):
            current_version = re.search(VERSION_REGEX, line).group()
            if (current_version != new_version):
                updated = True
                print("ANSIBLE_IMAGE_VERSION={}".format(new_version))
            else:
                print(line)
        else:
            print(line, end='')
    return updated


if __name__ == "__main__":
    version_number = get_latest_ansible_version()
    updated = replace_outdated_versions(version_number)
    if updated:
        print("New Version: {}".format(version_number))
        update_versions_in_git(version_number)
    else:
        print("No Update")
