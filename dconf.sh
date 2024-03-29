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

# Do not sleep
DCONF_DIR=/org/gnome/settings-daemon/plugins/power
dconf write $DCONF_DIR/idle-dim                         "false"
dconf write $DCONF_DIR/ambient-enabled                  "false"
dconf write $DCONF_DIR/sleep-inactive-battery-type      "'nothing'"
dconf write $DCONF_DIR/sleep-inactive-ac-timeout        "3600"
dconf write $DCONF_DIR/sleep-inactive-ac-type           "'nothing'"
dconf write $DCONF_DIR/sleep-inactive-battery-timeout   "1800"

# Do not idle
DCONF_DIR=/org/gnome/desktop/session
dconf write $DCONF_DIR/idle-delay                       "uint32 0"

# Touchpad tap to click
DCONF_DIR=/org/gnome/desktop/peripherals/touchpad
dconf write $DCONF_DIR/tap-to-click                     "true"

