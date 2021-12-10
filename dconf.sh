#!/bin/bash

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

