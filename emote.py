#!/usr/bin/env python3

"""
Simple script to copy emoticons to the clipboard.
Especially the complex ones, like ¯\_(ツ)_/¯ that
are hard to type.

Depends on Python 3.6+ features.
"""


import xerox
import click


emoticons = {
    'wink': ';-)',
    'smile': ':-)',
    'shrug': '¯\_(ツ)_/¯',
    'shock': '(°□°)',
}
# a short list for now; see also
# https://en.wikipedia.org/wiki/List_of_emoticons
# https://www.webpagefx.com/tools/emoji-cheat-sheet/
# http://www.unicode.org/emoji/charts/full-emoji-list.html
# https://pypi.python.org/pypi/emot/1.0


def list_emoticons():
    """
    Attractively list out all available named emoticons.
    """
    maxkeylen = max(len(k) for k in emoticons.keys())
    for name, value in emoticons.items():
        print(f'{name:{maxkeylen}} {value}')


@click.command()
@click.argument('name', default='smile')
def emote(name):
    """
    Return named emoticon on the clipboard.
    """
    if name == 'list':
        list_emoticons()
        return
    string = emoticons.get(name)
    if not string:
        print(f"Sorry, {name!r} unknown. Try 'emote list'.")
        return
    xerox.copy(string)


if __name__ == '__main__':
    emote()
