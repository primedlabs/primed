#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
  MMMMMMMMMNh  MMMMMMMMMNd  MMMM  MMMMm     MMMM  MMMMMMMMd  MMMMMMMMMN
  MMMMdhhMMMM  MMMMdhhMMMM  MMMM  MMMMMs   /MMMM  MMMMNmmmm  MMMMdhhMMMM
  MMMM   mMMM  MMMM   MMMM  MMMM  MMMMMM-.mMMMMM  MMMM       MMMM   MMMM
  MMMM   mMMM  MMMM   MMMM  MMMM  MMMMMMdsMMMMMM  MMMM       MMMM   MMMM
  MMMM   mMMM  MMMM   MMMM  MMMM  MMMMMMMMMMMMMM  MMMMNddd   MMMM   MMMM
  MMMM   mMMM  MMMMmdmMMMM  MMMM  MMMMdMMMMdMMMM  MMMMNddd   MMMM   MMMM
  MMMM   mMMM  MMMMdMMMMm   MMMM  MMMM/hMMN-MMMM  MMMM       MMMM   MMMM
  MMMM --NMMM  MMMM/ MMMm   MMMM  MMMM  NM  MMMM  MMMM       MMMM   MMMM
  MMMMNNNMMMM  MMMM  dMMM   MMMM  MMMM      MMMM  MMMMMNNNN  MMMMNNNMMMM
  MMMMdhhhhh   hhhh   hhhh  hhhh  hhhh      hhhh  hhhhhhhhs  hhhhhhhhhh
  MMMM
  MMMM
  MMMM
  MMMM
  KP:

########################################################################
#                                                                      #
#                            PRIMED TOOLKIT                            #
#                                                                      #
########################################################################

coverage run --source=primed setup.py test
coverage report -m
coveralls
m2r README.md
python setup.py sdist
twine upload dist/*
'''

__author__ = "Eugene Bann, Primed"
__copyright__ = 'Copyright (C) 2018 Demios, Inc.'
__version__ = '0.8'

from collections import defaultdict
from string import ascii_uppercase
from primed import nlp, utilities

def test_ireplace():
    assert nlp.ireplace('I want a hIPpo for my birthday', 'hippo', 'giraffe') == 'I want a giraffe for my birthday'
    assert nlp.ireplace('I want a hIPpo for my birthday', 'cat', 'dog') == 'I want a hIPpo for my birthday'
    assert nlp.ireplace('', 'cat', 'dog') == ''
    assert nlp.ireplace('', '', '') == ''

def test_ngrams():
    assert nlp.ngrams('cats will be cats') == {'cats': 2, 'will': 1, 'be': 1, 'cats will': 1, 'will be': 1, 'be cats': 1, 'cats will be': 1, 'will be cats': 1, 'cats will be cats': 1}
    assert nlp.ngrams('cats rule', min_grams=2, max_grams=2) == {'cats rule': 1}

def test_oxfordize():
    assert nlp.oxfordize(['cats', 'kittens', 'quantum', 'simulation']) == 'cats, kittens, quantum, and simulation'
    assert nlp.oxfordize(['cats']) == 'cats'
    assert nlp.oxfordize([]) == ''
    assert nlp.oxfordize(['cats', 'kittens']) == 'cats and kittens'

def test_capi():
    assert nlp.capi('i am british, and i also codify things') == 'I am british, and I also codify things'
    assert nlp.capi('me, myself, and i') == 'me, myself, and I'

def test_clean():
    assert nlp.clean('Ha, this   is fun! YUP!!!', lower=True) == 'ha this is fun yup'
    assert nlp.clean('Ha, this   is fun! YUP!!!', lower=False) == 'Ha this is fun YUP'

def test_a():
    assert nlp.a('university') == 'a'
    assert nlp.a('uninteresting') == 'an'
    assert nlp.a('US') == 'a'
    assert nlp.a('umbrella') == 'an'
    assert nlp.a('hotel') == 'a'
    assert nlp.a('hour') == 'an'
    assert nlp.a('waeiulfhaweiluh') == 'a'
    assert nlp.a('aappppiiii') == 'an'

def test_snake():
    assert nlp.snake('MAROON 5') == 'maroon_5'
    assert nlp.snake('the_Chair') == 'the_chair'
    assert nlp.snake('DELTA-V Budget', preserve_hyphens=True) == 'delta-v_budget'
    assert nlp.snake('DELTA-V Budget', preserve_hyphens=False) == 'deltav_budget'

def test_wiki_uri():
    assert nlp.wiki_uri('MAROON 5') == 'Maroon_5'
    assert nlp.wiki_uri('the_Chair') == 'The_chair'
    assert nlp.wiki_uri('DELTA-V Budget') == 'Delta-v_budget'

def test_keeper():
    assert nlp.keeper(ascii_uppercase) == defaultdict(type(None), {65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z'})

def test_cprint():
    utilities.cprint('Testing cprint function', style='OK', bold=True, underline=True, newline=True)
    assert True