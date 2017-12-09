#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:13:06 2017

@author: will
"""

import tensorflow as tf 
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
add = tf.add(a, b)
mul = tf.mul(a, b)

with tf.Session() as sess:
    print('a+b=',sess.run(add, feed_dict={a: 2, b: 3}))
    print('a*b=',sess.run(mul, feed_dict={a: 2, b: 3}))