#!/usr/bin/env python
"""
usage: python readinfos.py filename
"""
from os import system
import numpy as np

filename = argv[1]

infos = np.genfromtxt('test.tsv',dtype='f8',skip_header=1,delimiter='\t',usecols=(-1))

