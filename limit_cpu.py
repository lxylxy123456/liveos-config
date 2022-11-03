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

'''
	Limit and show CPU frequency when program is running
'''

import re, sys, time, glob, argparse
from subprocess import Popen
from threading import Thread

def get_cpu_freq() :
	for i in open('/proc/cpuinfo').read().split('\n') :
		matched = re.fullmatch('cpu MHz\s*: ([\d\.]+)', i)
		if matched :
			yield float(matched.groups()[0])

def set_cpu_freq(freq) :
	cmd = ['sudo', 'cpupower', 'frequency-set', '-u', str(freq)]
	Popen(cmd, stdout=-1).communicate()

def set_limit(limit) :
	if limit > 0 :
		if limit < 100:
			limit *= 100
		freq = limit * 1000
	else :
		# Used to be 18446744073709551615 = (1 << 64) - 1
		# Now is 15032385535 = 0x37fffffff
		freq = 15032385535
	set_cpu_freq(freq)

def get_limit() :
	limit_file = '/sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq'
	s = 0
	c = 0
	for i in glob.glob(limit_file) :
		s += int(open(i).read())
		c += 1
	try :
		return int(round(s / (1000 * c), 0))
	except ZeroDivisionError :
		return None

def format_freq(freq) :
	s = '% 5d' % freq
	if freq < 800 :
		return '\033[32;2m' + str(s) + '\033[0m'
	if freq < 1000 :
		return '\033[32m' + str(s) + '\033[0m'
	return str(s)

def show_stat_thread(battery=False) :
	'battery: limit CPU when using battery; unlimit when using AC power'
	fail_count = 0
	prev_battery = None
	while True :
		if battery :
			cur_battery = int(open('/sys/class/power_supply/AC/online').read())
			if prev_battery != cur_battery :
				if cur_battery :
					print('\033[41m\033[30mAC POWER -> NO LIMIT\033[0m')
					set_limit(0)
				else :
					print('\033[41m\033[30mBATTERY -> LIMIT\033[0m')
					set_limit(1)
				prev_battery = cur_battery
		lim = get_limit()
		freq = list(get_cpu_freq())
		# Reset when above frequency limit
		# Useful when computer waken from sleep mode
		if any(map(lambda x: x > lim + 100, freq)) :
			fail_count += 1
		else :
			fail_count = 0
		if fail_count >= 5 :
			fail_count = 0
			set_limit(0)
			print('\033[41m\033[30mRESET\033[0m')
			set_limit(lim)
		print(lim, ' '.join(map(format_freq, freq)), sep='\t')
		time.sleep(1)

def change_freq_thread() :
	try :
		while True :
			cmd = input()
			try :
				set_limit(int(cmd))
			except ValueError :
				print('ValueError:', repr(cmd))
	except (KeyboardInterrupt, EOFError):
		set_limit(0)
		print('set_limit(0)')

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-b', '--battery', action='store_true',
						help='Limit CPU when using battery')
	parser.add_argument('entry_limit', nargs='?', type=int, default=1,
						help='CPU limit during entry of this program')
	args = parser.parse_args()
	set_limit(args.entry_limit)
	Thread(target=show_stat_thread, daemon=True, args=(args.battery,)).start()
	change_freq_thread()

if __name__ == '__main__' :
	main()

