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
USAGE:
        ./register <module_id> -y <year> -c <cookies> [-t <time>] [-d <delay>]

OPTIONS:
  -h, --help    show this help message and exit
  -t N          delay in sec between each try (default 120)
  -d N          delay in sec between each request inside a try (default 0.5)
  -c COOKIES    auth cookies for the requests
  -y N          year of the module

EXAMPLE:
        ./register M-BDX-001/PAR-9-2 M-PRO-045/PAR-9-2 M-TRV-014/PAR-9-2 M-PRO-002/PAR-9-2 -c "foo=bar; name=Jhon; lastname=Doe" -d 0.1
```

> Watch out the number of requests your're sending, you could be banned !

## Install

```bash
mv register.py $HOME/bin/register && chmod +x $HOME/bin/register
```
