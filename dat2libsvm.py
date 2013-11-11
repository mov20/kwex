"""
convert  dat file to libsvm
"""

import sys
import csv
import json
import argparse
import numpy as np
from sklearn.datasets import dump_svmlight_file
from sklearn.feature_extraction.text import CountVectorizer

parser = argparse.ArgumentParser()
parser.add_argument( "input_file" )

args = parser.parse_args()

i_f = open( args.input_file )
reader = csv.reader( i_f, delimiter = "\t" )
# skip header
reader.next()

vectorizer = CountVectorizer( min_df = 3, max_df = 0.9, strip_accents = 'unicode', binary = True )
X = vectorizer.fit_transform( iterable( reader, args.test_set ))