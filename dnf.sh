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

case "$(lsb_release -is)" in
	Debian)
		sudo apt-get install linux-cpupower -y
		;;
	Fedora)
		sudo dnf install kernel-tools -y
		;;
	*)
		echo "Error: unknown Linux distribution: $(lsb_release -is)"
		;;
esac

