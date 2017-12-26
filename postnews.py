#!/usr/bin/env python
# coding: utf-8
"""
Post a usenet article (including headers) to an NNTP SERVER.

Usage: postnews [OPTIONS] SERVER
Article must at least contain the headers 'From:', 'Newsgroups:' and 'Subject:',
a newline and a body.

Options: -h, --help          display this text"
         -v, --verbose       be verbose"
         -f, --file=FILE     read file instead of stdin"
         -p, --port=PORT     port number"
             --user=NAME     user name"
             --pass=PASSWD   password"
         -r, --readermode    send MODE READER before authentication"
"""

# postnews 0.6.3 - post a usenet article
#
# (C) 2001-2002 by Michael Waschbüsch <waschbuesch@users.sourceforge.net>
# (C) 2014-2017 Robert James Clay <jame@rocasa.us>
# http://sourceforge.net/projects/postnews/
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# Juhuu! Mein erstes Python-Programm :o)

import sys
import nntplib
import getopt


def main():
    """Get arguments and options from the command line and then post the message."""
    #get arguments and options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:p:vr", ["help", "file=", \
                    "port=", "user=", "pass=", "verbose", "readermode"])
    except:
        print __doc__
        sys.exit(2)

    #parse arguments
    if len(args) != 1:
        print __doc__
        sys.exit(2)

    server = args[0]

    #parse options
    article_text = sys.stdin
    port = 119
    user = ""
    password = ""
    verbose = 0
    readermode = None

    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit()
        if o in ("-f", "--file"):
            try:
                article_text = open(a)
            except IOError:
                sys.stderr.write("File not found: "+a+"\n")
                sys.exit(2)
        if o in ("-p", "--port"):
            try:
                port = int(a)
                if port < 0 or port > 65535:
                    raise ValueError
            except ValueError:
                sys.stderr.write("Invalid port number: "+a+"\n")
                sys.exit(2)
        if o == "--user":
            user = a
        if o == "--pass":
            password = a
        if o in ("-v", "--verbose"):
            verbose = 1
        if o in ("-r", "--readermode"):
            readermode = 1

    #post message
    if verbose:
        print "Connecting to Server..."
    try:
        s = nntplib.NNTP(server, port, user, password, readermode)
    except Exception, e:    # it can throw a class exception...
        sys.stderr.write("Can't connect to server: "+server+"\n")
        sys.stderr.write(str(e)+"\n")
        sys.exit(2)
    except:         # ... or a string exception
        sys.stderr.write("Can't connect to server: "+server+"\n")
        sys.stderr.write(sys.exc_info()[1]+"\n")
        sys.exit(2)
    if verbose:
        print "Posting article..."
    try:
        s.post(article_text)
    except Exception, e:    # it can throw a class exception...
        sys.stderr.write("Can't post the given input.\n")
        sys.stderr.write(str(e)+"\n")
        sys.exit(2)
    except:         # ... or a string exception
        sys.stderr.write("Can't post the given input.\n")
        sys.stderr.write(sys.exc_info()[1]+"\n")
        sys.exit(2)

    s.quit()


if __name__ == "__main__":
    main()
