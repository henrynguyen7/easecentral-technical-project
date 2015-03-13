# -*- coding: utf-8 -*-

"""
Controller for /default service.

Author: Henry Nguyen (henry@dxconcept.com)
"""

import itertools

def index():
    redirect(URL('default', 'anagrams'))
    return dict(message=None)

def anagrams():

    # A file was uploaded
    if request.vars.uploadfile is not None:

        # Read the file
        inputfile = request.vars.uploadfile.file.read()

        # Parse the input into a list of words
        words = inputfile.split()

        # Sort the list, sorting each word before comparing
        sorted_words = sorted(words, key=sorted)

        # Group words if sorted letters in each word match
        groups = itertools.groupby(sorted_words, sorted)

        # Assemble list of grouped words since groupby returns an iterator
        grouped_words = [list(group) for key, group in groups]

        # Assemble anagrams by checking groups that have two or more words
        anagram_groups = [group for group in grouped_words if len(group) > 1]

        # Return anagrams so they can be rendered in the view
        return dict(
            is_solution=True,
            words=words,
            anagram_groups=anagram_groups
        )

    return dict(is_solution=False)

def contactdb():
    return dict(message=None)