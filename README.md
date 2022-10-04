# Epi-register

The module you ar looking for is full? Tired of watching everyday if students left a place? Epi-register is here for you !

Automate your registration to your favorite modules and save time for your aqua-ponney sessions.

## Usage

```txt
USAGE:
        ./register <module_id> -c <cookies> [-t <time>]

EXAMPLE
        ./register M-BDX-001 M-PRO-045 M-TRV-014 M-PRO-002 -c "foo=bar; name=Jhon; lastname=Doe"
```

> Watch out to the number of requests your're sending ("-t" option will come soon)

## Install

```bash
mv register.py $HOME/bin
```