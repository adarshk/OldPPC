#!/usr/bin/env python

"""
SYNOPSIS

    service.py [-h] [-v,--verbose] [--version]

DESCRIPTION

    This is a service python script that listens on port 8080 and has the following methods:

    /upload [POST] - upload a photo and run it through the paperpixel service, receieve JSON values.

EXAMPLES

    python service.py

AUTHOR

    Anderson Miller <anderson.miller@frogdesign.com>

LICENSE

    Copyright 2014, Frog Design

VERSION

    
"""

import sys
import os
import traceback
import optparse
import time
#from pexpect import run, spawn

# Uncomment the following section if you want readline history support.
#import readline, atexit
#histfile = os.path.join(os.environ['HOME'], '.TODO_history')
#try:
#    readline.read_history_file(histfile)
#except IOError:
#    pass
#atexit.register(readline.write_history_file, histfile)
from flask import Flask
from flask import request
from paperpixel import Components
import uuid

class NoDestinationException(Exception):
    pass

def main ():

    global options, args


    #TODO http://flask.pocoo.org/docs/deploying/fastcgi/#configuring-nginx
    file_location = ""
    try:
        file_location = os.environ['PIXEL_FILES']
    except KeyError:
        raise NoDestinationException("please set PIXEL_FILES environment variable")

    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return 'Hello World!'

    #Just make sure not to forget to set the enctype="multipart/form-data"
    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            f = request.files['photo']
            filetype = f.filename.split(".")[1]
            newFilename = "{2}/{0}.{1}".format(str(uuid.uuid4()).replace("-",""),filetype,file_location)
            f.save(newFilename)
            #c = Components(newFilename)
            #c.print_values
            #TODO make this JSON output from Components
            return "{'finished': true}"

    app.run(host='0.0.0.0')
    print 'running service'

if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(
                formatter=optparse.TitledHelpFormatter(),
                usage=globals()['__doc__'],
                version='$Id: py.tpl 332 2008-10-21 22:24:52Z root $')
        parser.add_option ('-v', '--verbose', action='store_true',
                default=False, help='verbose output')
        (options, args) = parser.parse_args()
        #if len(args) < 1:
        #    parser.error ('missing argument')
        if options.verbose: print time.asctime()
        exit_code = main()
        if exit_code is None:
            exit_code = 0
        if options.verbose: print time.asctime()
        if options.verbose: print 'TOTAL TIME IN MINUTES:',
        if options.verbose: print (time.time() - start_time) / 60.0
        sys.exit(exit_code)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)

