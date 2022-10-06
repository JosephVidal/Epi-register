#! /usr/bin/env python3
# coding: utf-8

import sys
import requests

from rich.theme import Theme
from rich.console import Console
from time import sleep

theme = Theme({"success": "green", "error": "bold red", "neutral": "white"})
console = Console(theme=theme)


def register(session, url, cookies, payload, module):
    for elem in cookies:
        obj = elem.split('=')
        payload[obj[0]] = obj[1]
    rep = session.post(url, cookies=payload)
    if (rep.status_code == 200):
        console.log("Succeessfully registerd to " + module, style="success")
        return True
    console.log("Failed to register to " + module + " (code " + str(rep.status_code) + ")", style="error")
    return False


def main(args):
    cookies = args[args.index("-c") + 1].replace(' ', '').split(";")
    modules = args[1:args.index("-c")]
    payload = {}
    session = requests.Session()
    time = float(args[args.index("-t") + 1]) if "-t" in args else 120
    step = 0

    console.log(f"Timer: {time} seconds", style="neutral")
    with console.status("[bold green]Progressing...") as status:
        while 1:
            step = step + 1
            console.log("try " + str(step), style="success")
            for module in modules:
                url = "https://intra.epitech.eu/module/2022/" + module + "/PAR-9-2/register?format=json"

                if register(session, url, cookies, payload, module):
                    modules.remove(module)
            if (len(modules) == 0):
                break
            sleep(time)
    console.log('Done!', style="success")


if __name__ == "__main__":
    if len(sys.argv) < 3 or not "-c" in sys.argv:
        print("USAGE:\n\t./register <module_id> -c <cookies> [-t <time>]\n\nEXAMPLE\n\t./register M-BDX-001 M-PRO-045 M-TRV-014 M-PRO-002 -c \"foo=bar; name=Jhon; lastname=Doe\"")
        sys.exit(84)
    else:
        try:
            main(sys.argv)
        except KeyboardInterrupt:
            console.log("Manual interrupt", style="error")
