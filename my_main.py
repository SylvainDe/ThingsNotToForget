#! /usr/bin/python
# vim: set tabstop=4 expandtab shiftwidth=4 :
# Generated by letscode

"""Docstring for Python module"""

import collections
import my_list
import my_list_fr

# Python 2/3 compatibility
try:
    basestring
except NameError:
    basestring = (str, bytes)


def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and \
                not isinstance(el, basestring):
            for sub in flatten(el):
                yield sub
        else:
            yield el


def main():
    """Main function"""
    print('\n'.join(sorted(set(flatten(my_list_fr.london)))))

if __name__ == "__main__":
    main()
