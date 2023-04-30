#! /usr/bin/env python3
# coding: utf-8

import requests
import argparse

from rich.theme import Theme
from rich.console import Console
from time import sleep

EXIT_SUCCESS = 0
EXIT_FAILURE = 84

DEFAULT_TIME = 120
DEFAULT_DELAY = 0.5

theme = Theme({"success": "green", "error": "bold red", "neutral": "white"})
console = Console(theme=theme)

token = "aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ=="


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
    if (rep.status_code == requests.codes.unauthorized): # Useless because the intra uses 403 instead, but it's there in case of they improve it lmao
        console.log("Invalid auth token.", style="error")
    if (rep.status_code == requests.codes.not_found):
        console.log("This is not the module you are looking for.", style="error")
    else:
        console.log("Failed to register to " + module + " (code " + str(rep.status_code) + ")", style="error")
    return False


def main(args):
    cookies = args.cookies.split(";")
    payload = {}
    session = requests.Session()
    step = 0

    console.log(f"Timer: {args.time} seconds", style="neutral")
    with console.status("[bold green]Progressing..."):
        while 1:
            step = step + 1
            console.log("try " + str(step), style="success")
            for elem in args.modules:
                url = "https://intra.epitech.eu/module/" + args.year + "/" + elem + "/register?format=json"

                if register(session, url, cookies, payload, elem):
                    args.modules.remove(elem)
                sleep(args.delay)
            if (len(args.modules) == 0):
                break
            sleep(args.time)
    console.log('Done!', style="success")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('modules', type=str, nargs="+")
    parser.add_argument('-c', "--cookies", type=str, help='auth cookies for the requests', required=True)
    parser.add_argument('-y', "--year", type=str, help='year of the module', required=True)
    parser.add_argument('-t', "--time", type=int, help='delay in sec between each try (default 120)', default=DEFAULT_TIME)
    parser.add_argument('-d', "--delay", type=float, help='delay in sec between each request inside a try (default 0.5)', default=DEFAULT_DELAY)
    args = parser.parse_args()
    try:
        main(args)
    except KeyboardInterrupt:
        console.log("Manual interrupt", style="error")
