#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    hello = HelloTravic()
    hello.print_hello()


class HelloTravic(object):
    def __init__(self):
        self.str = "Hello Travis!"

    def print_hello(self):

        print self.str

if __name__ == "__main__":
    main()
