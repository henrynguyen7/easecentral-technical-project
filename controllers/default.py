# -*- coding: utf-8 -*-

"""
Controller for /default service.

Author: Henry Nguyen (henry@dxconcept.com)
"""

def index():
    redirect(URL('default', 'anagrams'))
    return dict(message=None)

def anagrams():

    if request.vars.uploadfile is not None:

        inputfile = request.vars.uploadfile.file.read()
        words = inputfile.split()

        for word in words:
            print word

    return dict(message=None)

def contactdb():
    return dict(message=None)