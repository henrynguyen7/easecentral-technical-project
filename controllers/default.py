# -*- coding: utf-8 -*-

"""
Controller for /default service.

Author: Henry Nguyen (henry@dxconcept.com)
"""

def index():
    redirect(URL('default', 'anagrams'))
    return dict(message=None)

def anagrams():
    return dict(message=None)

def contactdb():
    return dict(message=None)