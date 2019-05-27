# project: extracting speech from the chinese news corpus
# author: github.com/xinweixu1
# date created:  May 11, 2019
# last updated:  May 25, 2019


# using the official StanfordNLP python package:
#https://github.com/stanfordnlp/stanfordnlp

# there are two ways:
# 1) use the pre-trained neural pipelines directly from python (require torch > 1.0.0)
# 2) access the java NLP server through the python package

# however, it seems 1) only provides basic NLP features (e.g., tokenize, lemma, pos, depparse)
# and doesn't offer the 'tokensregex' function...

############################
# Using the neural pipeline
###########################

import sys
import argparse
import os

import stanfordnlp
#from stanfordnlp.utils.resources import DEFAULT_MODEL_DIR

# download the chinese pipeline
#stanfordnlp.download('zh')

# set up the pipeline for chinese models
print('---')
print('Building pipeline...')
pipeline = stanfordnlp.Pipeline(lang='zh')

# read in news sample, but to avoid '\n', we use .read().splitlines()
with open('./test_chinese_news.txt', encoding='utf-8') as f:
    news_sample = f.read().splitlines()

# change the list into a string
news_content = ''.join(news_sample)

# process the document
results = pipeline(news_content)


# access nlp annotations
print('')
print('Input: {}'.format(news_content))
print("The tokenizer split the input into {} sentences.".format(len(results.sentences)))
print('---')
print('tokens of first sentence: ')
results.sentences[0].print_tokens()
print('')
print('---')
print('dependency parse of first sentence: ')
results.sentences[0].print_dependencies()
print('')


###################################
# Accessing the Java CoreNLP client
###################################

# the following example is directly taken from the github,
# but failed...
# the python console just stuck when the NLP server is started ...

from stanfordnlp.server import CoreNLPClient

# example text
print('---')
print('input text')
print('')

text = "Chris Manning is a nice person. Chris wrote a simple sentence. He also gives oranges to people."


# set up the client
print('---')
print('starting up Java Stanford CoreNLP Server...')

# set up the client
with CoreNLPClient(annotators=['tokenize','ssplit','pos','lemma','ner', 'parse', 'depparse','coref'], timeout=60000, memory='16G') as client:
    # submit the request to the server
    ann = client.annotate(text)

    # get the first sentence
    sentence = ann.sentence[0]

    # get the dependency parse of the first sentence
    print('---')
    print('dependency parse of first sentence')
    dependency_parse = sentence.basicDependencies
    print(dependency_parse)

    # get the part-of-speech tag
    print('---')
    print('part of speech tag of token')
    token.pos
    print(token.pos)

    # get the named entity tag
    print('---')
    print('named entity tag of token')
    print(token.ner)

    # access the coref chain
    print('---')
    print('coref chains for the example')
    print(ann.corefChain)

    # Use tokensregex patterns to find who wrote a sentence.
    pattern = '([ner: PERSON]+) /wrote/ /an?/ []{0,3} /sentence|article/'
    matches = client.tokensregex(text, pattern)
    # sentences contains a list with matches for each sentence.
    assert len(matches["sentences"]) == 3
    # length tells you whether or not there are any matches in this
    assert matches["sentences"][1]["length"] == 1
    # You can access matches like most regex groups.
    print(matches["sentences"][1]["0"]["text"])



# f = open('./test_chinese_news.txt', encoding='utf-8')
# news_sample = f.read()
# news_content = ''.join(news_sample)

# set up the client
#with CoreNLPClient(annotators=['tokenize','ssplit','pos','lemma','ner', 'parse', 'depparse','coref'],
#                   properties='StanfordCoreNLP-chinese.properties',
#                   timeout=60000, memory='16G') as client:
#    # submit the request to the server
#    ann = client.annotate(news_content)


    #pattern = '([ner: PERSON]+) /说|提到|表示/  []'
    #matches = client.tokensregex(news_content, pattern)



