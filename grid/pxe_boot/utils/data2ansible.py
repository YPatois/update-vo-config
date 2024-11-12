#!/usr/bin/env python3
import os
import re


def main():
    for wni in range(40,59):
        wn = 'sbgwn' + str(wni) + '.in2p3.fr'
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
            print("ERROR: no interface found")
            break
        #print(current_interface[0])
        iname=re.match("^[0-9]+:\s+(\w+):", current_interface[0]).group(1)
        print("interface: " + iname)


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
