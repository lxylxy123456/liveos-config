# LiveOS Config
Automatically configure a Fedora or Debian LiveOS
 
## License
GNU Affero General Public License, version 3

## Use
1. Connect to Internet
2. On Debian 12, `sudo apt-get install git`
3. `git clone https://github.com/lxylxy123456/liveos-config`
4. `cd liveos-config`
5. `./autorun.sh`
6. Open a new terminal (since there are Bash aliases configured) and enjoy

To minimize typing, steps 2 - 5 are available at `live.sh`. This file is likely
hosted in:
* <https://lxylxy123456.github.io/live.sh>
* <https://www.ercli.dev/live.sh>
* <https://raw.githubusercontent.com/lxylxy123456/liveos-config/master/live.sh>

e.g. For the first link, after connecting Fedora to the Internet, type:
```sh
curl https://lxylxy123456.github.io/live.sh | bash
```

