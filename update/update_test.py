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

import unittest
from update import update
import os
import unittest.mock
from unittest.mock import MagicMock

class UpdateTest(unittest.TestCase):
    def setUp(self):
        update._get_latest_ansible_version = MagicMock()   
        update._update_versons_in_git = MagicMock()     
        update.VERSIONS_SH = "valid.sh"
        f = open(update.VERSIONS_SH, "w+")
        f.write("#!/bin/bash\n\nJENKINS_IMAGE_TAG=latest\nANSIBLE_IMAGE_VERSION=0.0.0\n")
        f.close() 

    def test_keep_version(self):
        update._get_latest_ansible_version.return_value = "0.0.0"
        update.main()
        update._update_versons_in_git.assert_not_called()

    def test_update_version(self):
        update._get_latest_ansible_version.return_value = "1.0.0"
        update.main()
        update._update_versons_in_git.assert_called_once()

    def tearDown(self):
        os.remove(update.VERSIONS_SH)


if __name__ == '__main__':
    unittest.main()
