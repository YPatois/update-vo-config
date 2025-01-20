#!/usr/bin/env python3
import os
import re


def main():
    files = [ f for f in os.listdir('data') if os.path.isfile(os.path.join('data', f))]
    for lf in files:
        if (re.search('\.txt',lf)):
            wn = lf.replace('.txt','')
            print(wn)
            with open(os.path.join('data', wn) + '.txt', 'r') as f:
                current_interface = []
                good_interface=False
                for line in f:
                    #print(line)
                    # If line starts with <n>: it's a new interface
                    if (re.match('^[0-9]+: ', line)):
                        if (good_interface):
                            break
                        current_interface = [line]
                    else:
                        current_interface.append(line)
                    # If we see a valid IP address in "134.158", it's the good interface
                    if (re.search('134.158',line)):
                        good_interface=True
            if (not good_interface):
                print("ERROR: no interface found for " + wn)
            iname="INVALID"
            mac="INVALID"
            ip4="INVALID"
            ip6="INVALID"
            for line in current_interface:
                #print (line)
                if (re.match('^[0-9]+: ', line)):
                    iname=re.match("^[0-9]+:\s+(\w+):", line).group(1)
                    print("interface: " + iname)
                if (re.search('link/ether',line)):
                    mac=re.search('link/ether ([0-9a-f:]+)',line).group(1)
                    print("mac: " + mac)
                if (re.search('inet ',line)):
                    ip4=re.search('inet ([0-9./]+)',line).group(1)
                    print("ip4: " + ip4)
                if (re.search('inet6 2001',line)):
                    ip6=re.search('inet6 ([0-9a-f:/]+)',line).group(1)
                    print("ip6: " + ip6)
            if (ip4 == "INVALID"):
                continue
            if (ip6 == "INVALID"):
                ip4split=ip4.split('/')[0]
                ip4split=ip4split.split('.')
                ip6="2001:660:4705:d002:" + ip4split[0] + ":" + ip4split[1] + ":" + ip4split[2] + ":" + ip4split[3]+"/64"
            with open(os.path.join('data', wn) + '.yml', 'w') as f:
                f.write("---\n")
                f.write("hostname: '" + wn + "'\n")
                f.write("ipv4: '" + ip4 + "'\n")
                f.write("ipv6: '" + ip6 + "'\n")
                f.write("iface_name: '" + iname + "'\n")
                f.write("ifdevice: '" + mac.upper() + "'\n")
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
