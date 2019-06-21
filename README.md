# Whentfis

So there's that extremely important thing you've got to go to. You have the date and
everything, but you have no *feeling* for when it actually is. whentfis is the solution.

## Examples

So the current date appears to be:
```
$ date +%d/%m/%y
21/06/19

```

We have a big meeting set for 26/6/19, let's see what we can do with that:

```
$ whentfis 26/6/19
Next Wednesday

```

Great! But you've just remembered your mum's birthday is on 23/6/2019 (every year!):

```
$ whentfis 23/6/2019
This Sunday

```
Thank god we checked. You're friend from the states says he's arriving on 7/15/19. We can
do M/D/Y as well:

```
$ whentfis -m 7/15/2019
4 weeks Monday

```


## Usage

```
usage: whentfis [-h] [-m] date

Transforms dates in the form DMY or MDY to a human readable format.

positional arguments:
  date        Date you want to rationalise

optional arguments:
  -h, --help  show this help message and exit
  -m, --MDY   Interpret date format as MDY

```

## Installation

Requires python 3.

```
# Installs locally
$ git clone https://github.com/LaurenceWarne/whentfis && cd whentfis
$ python3 setup.py install --user
```
