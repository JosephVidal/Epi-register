#! /usr/bin/env python3
# coding: utf-8

import sys
import requests

from rich.theme import Theme
from rich.console import Console
from time import sleep

EXIT_SUCCESS = 0
EXIT_FAILURE = 84

DEFAULT_TIME = 120
DEFAULT_DELAY = 0.5
MIN_ARGC = 6

theme = Theme({"success": "green", "error": "bold red", "neutral": "white"})
console = Console(theme=theme)

token = "aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ=="

def helper():
    print("USAGE:\n\t./register <module_id> -y <year> -c <cookies> [-t <time>] [-d <delay>]\n")
    print("OPTIONS:\n  -h, --help\tshow this help message and exit\n  -t N\t\tdelay in sec between each try (default 120)\n  -d N\t\tdelay in sec between each request inside a try (default 0.5)\n  -c COOKIES\tauth cookies for the requests\n  -y N\t\tyear of the module\n")
    print("EXAMPLE:\n\t./register M-BDX-001/PAR-9-2 M-PRO-045/PAR-9-2 M-TRV-014/PAR-9-2 M-PRO-002/PAR-9-2 -c \"foo=bar; name=Jhon; lastname=Doe\" -d 0.1")


def register(session, url, cookies, payload, module):
    for elem in cookies:
        obj = elem.split('=')
        payload[obj[0]] = obj[1]
    rep = session.post(url, cookies=payload)
    if (rep.status_code == requests.codes.too_many):
        console.log("You have been blacklisted", style="error")
        exit(EXIT_FAILURE)
    if (rep.status_code == requests.codes.ok):
        console.log("Succeessfully registerd to " + module, style="success")
        return True
    if (rep.status_code == requests.codes.not_found):
        console.log("This is not the module you are looking for.", style="error")
    else:
        console.log("Failed to register to " + module + " (code " + str(rep.status_code) + ")", style="error")
    return False


def main(args):
    cookies = args[args.index("-c") + 1].replace(' ', '').split(";")
    modules = args[1:args.index("-c")]
    payload = {}
    session = requests.Session()
    time = float(args[args.index("-t") + 1]) if "-t" in args else DEFAULT_TIME
    delay = float(args[args.index("-d") + 1]) if "-d" in args else DEFAULT_DELAY
    year = args[args.index("-y") + 1]
    step = 0

    console.log(f"Timer: {time} seconds", style="neutral")
    with console.status("[bold green]Waiting for next try..."):
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
    if "-h" in sys.argv or "--help" in sys.argv:
        helper()
        sys.exit(EXIT_SUCCESS)
    elif len(sys.argv) < MIN_ARGC or "-c" not in sys.argv or "-y" not in sys.argv:
        helper()
        sys.exit(EXIT_FAILURE)
    else:
        try:
            main(sys.argv)
        except KeyboardInterrupt:
            console.log("Manual interrupt", style="error")
