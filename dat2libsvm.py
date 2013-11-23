"""
convert  dat file to libsvm
"""

import sys, csv, argparse
import numpy as np
from sklearn.datasets import dump_svmlight_file
from sklearn.feature_extraction.text import CountVectorizer

tags = []
DictTags = {}

# a generator wrapper to get data from a file
def iterable( reader ):
    n = 0
    for line in reader:
        n += 1
        if n % 1000 == 0:
                print n
                
        id = line.pop( 0 )        # id
        title = line.pop( 0 )        # title
        
        body = line.pop( 0 ) # body
    
        tags = line.pop(0) # tags
        # todo add tags somewhere
        yield title



def countTags( reader ):
    global DictTags
    n = 0
    for line in reader:
        id = line.pop( 0 )        # id
        title = line.pop( 0 )        # title
        
        body = line.pop( 0 ) # body
    
        tags = line.pop(0) # tags

        for tag in tags.split():
            #print tag
            if tag in DictTags:
                DictTags[tag] += 1
            else:
                DictTags[tag] = 1

        n += 1
        if n % 10000 == 0:
                print n, ' DictSize = ', len(DictTags), ' ', tags

        if n > 20000:
                print 'breaking loop'
                return

parser = argparse.ArgumentParser()
parser.add_argument( "input_file" )

args = parser.parse_args()

i_f = open( args.input_file )
reader = csv.reader( i_f)
# skip header
reader.next()

'''
vectorizer = CountVectorizer( strip_accents = 'unicode')
X = vectorizer.fit_transform( iterable( reader ))
print X
'''
countTags( reader )
for item in DictTags:
    print item, ' ', DictTags[item]
