# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:04:35 2018

@author: Administrator
"""

def pre(name):
    def sentence(words):
        print(name,words)
    return sentence

test=pre('sina')
test('hello')
test('how are you')