#! /usr/bin/env python3
# coding: utf-8

import sys
import requests

from rich.theme import Theme
from rich.console import Console
from time import sleep

theme = Theme({"success": "green", "error": "bold red", "neutral": "white"})
console = Console(theme=theme)

token = "aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ=="


def register(session, url, cookies, payload, module):
    for elem in cookies:
        obj = elem.split('=')
        payload[obj[0]] = obj[1]
    rep = session.post(url, cookies=payload)
    if (rep.status_code == 429):
        console.log("You have been blacklisted", style="error")
        exit(84)
    if (rep.status_code == 200):
        console.log("Succeessfully registerd to " + module, style="success")
        return True
    if (rep.status_code == 404):
        console.log("This is not the module you are looking for.", style="error")
    else:
        console.log("Failed to register to " + module + " (code " + str(rep.status_code) + ")", style="error")
    return False


def main(args):
    cookies = args[args.index("-c") + 1].replace(' ', '').split(";")
    modules = args[1:args.index("-c")]
    payload = {}
    session = requests.Session()
    time = float(args[args.index("-t") + 1]) if "-t" in args else 120
    delay = float(args[args.index("-d") + 1]) if "-d" in args else 0.5
    year = args[args.index("-y") + 1]
    step = 0

    console.log(f"Timer: {time} seconds", style="neutral")
    with console.status("[bold green]Progressing..."):
        while 1:
            step = step + 1
            console.log("try " + str(step), style="success")
            for module in modules:
                url = "https://intra.epitech.eu/module/" + year + "/" + module + "/register?format=json"

                if register(session, url, cookies, payload, module):
                    modules.remove(module)
                sleep(delay)
            if (len(modules) == 0):
                break
            sleep(time)
    console.log('Done!', style="success")


if __name__ == "__main__":
    if len(sys.argv) < 6 or "-c" not in sys.argv or "-y" not in sys.argv:
        print("USAGE:\n\t./register <module_id> -y <year> -c <cookies> [-t <time>] [-d <delay>]\n\nEXAMPLE\n\t./register M-BDX-001/PAR-9-2 M-PRO-045/PAR-9-2 M-TRV-014/PAR-9-2 M-PRO-002/PAR-9-2 -c \"foo=bar; name=Jhon; lastname=Doe\" -d 0.1")
        sys.exit(84)
    else:
        try:
            main(sys.argv)
        except KeyboardInterrupt:
            console.log("Manual interrupt", style="error")
