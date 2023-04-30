# Epi-register

The module you are looking for is full? Tired of watching everyday if students left a place? Epi-register is here for you !

Automate your registration to your favorite modules and save time for your aqua-ponney daily sessions !

## Dependancies
- Rich
- Requests

```bash
pip3 install -r requirements.txt
```

## Usage

```txt
usage: register.py [-h] -c COOKIES -y YEAR [-t TIME] [-d DELAY] modules [modules ...]

positional arguments:
  modules

options:
  -h, --help            show this help message and exit
  -c COOKIES, --cookies COOKIES
                        auth cookies for the requests
  -y YEAR, --year YEAR  year of the module
  -t TIME, --time TIME  delay in sec between each try (default 120)
  -d DELAY, --delay DELAY
                        delay in sec between each request inside a try (default 0.5)
```

> Watch out the number of requests your're sending, you could be banned !

## Install

```bash
mv register.py $HOME/bin/register && chmod +x $HOME/bin/register
```
