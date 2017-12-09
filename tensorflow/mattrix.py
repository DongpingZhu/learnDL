#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:03:15 2017

@author: will
"""
import tensorflow as tf 
a=tf.Variable(tf.ones([3,2]))
b=tf.Variable(tf.ones([2,3]))
product=tf.matmul(5*a,4*b)
init=tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(product))
