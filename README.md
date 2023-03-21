# Epi-register

The module you are looking for is full? Tired of watching everyday if students left a place? Epi-register is here for you !

Automate your registration to your favorite modules and save time for your aqua-ponney daily sessions !

## Usage

```txt
USAGE:
        ./register <module_id> -c <cookies> -y <year> [-t <time>]

EXAMPLE
        ./register M-BDX-001 M-PRO-045 M-TRV-014 M-PRO-002 -c -y 2022 "foo=bar; name=Jhon; lastname=Doe"
```

the default timer is 120 sec.

> Watch out the number of requests your're sending, you could be banned !

## Install

```bash
$ mv register.py $HOME/bin/register && chmod +x $HOME/bin/register
```
