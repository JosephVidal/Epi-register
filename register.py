#! /usr/bin/env python3
# coding: utf-8

import sys
import requests

from time import sleep

def register(session, url, cookies, payload, module):
    for elem in cookies:
        obj             = elem.split('=')
        payload[obj[0]] = obj[1]
    rep = session.post(url, cookies=payload)
    if (rep.status_code == 200):
        print("Registrationn succeed to " + module)
        return True
    print("Failed to register to " + module + " (code " + str(rep.status_code) + ")")
    return False

def main(args):
    cookies = args[args.index("-c") + 1].replace(' ', '').split(";") # ex : "foo=bar; name=Jhon; lastname=Doe"
    modules = args[1:args.index("-c")]
    payload = {}
    session = requests.Session()

    while 1 :
        for module in modules:
            url = "https://intra.epitech.eu/module/2022/" + module + "/PAR-9-2/register?format=json"
            if register(session, url, cookies, payload, module) == False:
                continue
            modules.remove(module)
        if (len(modules) == 0):
            break
        sleep(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("USAGE:\n\t./register <module_id> [-c <cookies>]\n\nEXAMPLE\n\t./register M-BDX-001 M-PRO-045 M-TRV-014 M-PRO-002 -c \"foo=bar; name=Jhon; lastname=Doe\"")
        sys.exit(84)
    else:
        main(sys.argv)
