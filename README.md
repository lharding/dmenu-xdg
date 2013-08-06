# dmenu-xdg

Script for scanning XDG .desktop files and launching them using dmenu.

## Installation

Requires Python 2.4+ and [pyxdg](http://freedesktop.org/wiki/Software/pyxdg/) for parsing .desktop files.

Run install.sh to copy the scripts into ~/bin, and copy the .conf file into ~/.config/ and set SEARCH_DIRS appropriately.

## Usage

Use your preferred method to trigger build-menu.py when your collection of .desktop files changes, then invoke the dmenu-xdg script to actually get the menu. The script as included references "vmenu", which is an alias to dmenu I have set up with options I like. I strongly recommend the vertical format (-l nn) option for this script.

## For the love of god, why?

I have one of [these](http://openpandora.org) and the included OS launches games and some very useful scripts from a custom menu app (which I don't use because it doesn't play nicely with dwm) that populates itself from .desktop files containing some fairly long command lines. This script lets me launch those as if I were just invoking dmenu_run on something from my PATH.

That said, this should provide the "missing" suckless-style start menu for users of dwm, awesome, and so on.
