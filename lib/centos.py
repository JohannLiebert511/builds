# Copyright (C) IBM Corp. 2016.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

from lib import distro
from lib import mockbuilder

CENTOS_VERSIONS = ["7.2", ]


class CentOS(distro.LinuxDistribution):

    supported_versions = CENTOS_VERSIONS

    def __init__(self, name, version, arch_and_endianess):
        super(CentOS, self).__init__(name=name, version=version,
                                     arch_and_endianess=arch_and_endianess)
        mock_config_dir = os.path.join(os.getcwd(), 'extras/centOS/7.2/mock')
        self.package_builder = mockbuilder.Mock(os.path.join(
            mock_config_dir,
            'epel-7-ppc64le.cfg'))
