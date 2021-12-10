#!/usr/bin/python3
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

import os, sys

backlight_path = '/sys/class/backlight/intel_backlight/'

def backlight_read(name):
	assert name in { 'max_brightness', 'brightness', 'actual_brightness' }
	return int(open(backlight_path + name).read())

def backlight_write(value, name='brightness'):
	assert name in { 'brightness', 'actual_brightness' }
	if type(value) != int:
		value = int(value)
	return open(backlight_path + name, 'w').write('%d\n' % value)

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print()
		print('path', '\t= %s' % backlight_path)
		print()
		for i, j in [('max_brightness', 'max'),
					('brightness', 'bright'),
					('actual_brightness', 'actual')]:
			print(j, '\t=', backlight_read(i))
		print()
		exit(0)

	if os.getuid():
		raise Exception('Needs root permission')

	backlight_write(sys.argv[1])

