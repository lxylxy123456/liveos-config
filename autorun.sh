#!/bin/bash
#
#  liveos-config - Automatically configure a Fedora LiveOS
#  Copyright (C) 2021  lxylxy123456
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

set -xe

SOURCE_DIR="$(dirname ${BASH_SOURCE})"
bash "${SOURCE_DIR}/dconf.sh"
echo ". ${SOURCE_DIR}/alias.sh" >> ~/.bashrc
echo ". ${SOURCE_DIR}/alias.sh" >> ~/.bash_profile
bash "${SOURCE_DIR}/dnf.sh"
echo SUCCESS

