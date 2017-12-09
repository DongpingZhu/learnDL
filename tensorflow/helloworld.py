#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:14:14 2017

@author: will
"""

import tensorflow as tf
word=tf.constant('hello,world!')
with tf.Session() as sess:
    print(sess.run(word))