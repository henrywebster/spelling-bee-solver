#!/usr/bin/env python3

'''
Spelling Bee Solver - Solver for Spelling Bee Game

Written in 2019 by Henry Webster <henry@hwebs.info>

To the extent possible under law, the author(s) have dedicated all copyright and related and neighboring rights to this software to the public domain worldwide. This software is distributed without any warranty.

You should have received a copy of the CC0 Public Domain Dedication along with this software. If not, see <http://creativecommons.org/publicdomain/zero/1.0/>. 
'''

import argparse

def solve(center, outer, words):
    valid_letters = outer.union(center)
    results = set()
    for word in words:
        word_letters = set([char for char in word])
        if len(word) > 3 and center in word_letters and word_letters.issubset(valid_letters):
            results.add(word)
    return results

def validate_center(center):
    if 1 != len(center):
        raise argparse.ArgumentTypeError('center can only be one letter')
    if not center[0].isalpha():
        raise argparse.ArgumentTypeError('{} is not a letter'.format(center[0]))
    return center

def validate_outer(outer):
    if 6 != len(set(outer)):
        raise argparse.ArgumentTypeError('must be 6 distinct letters') 
    for char in outer:
         if not char.isalpha():
            raise argparse.ArgumentTypeError('{} is not a letter'.format(char)) 
    return outer

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Solve Spelling Bee')
    parser.add_argument('--center', type=validate_center, help='the center letter', required=True)
    parser.add_argument('--outer', type=validate_outer, help='the outside letters', required=True)
    parser.add_argument('--file', type=str, nargs='?', help='the file of words', default='words_alpha.txt', required=False)

    args = parser.parse_args()
    center = args.center.lower()
    outer = set([char.lower() for char in args.outer])
    filename = args.file

    with open(filename) as word_file:
        words = set(word_file.read().split())
    
    for word in solve(center, outer, words):
        print(word)


    
