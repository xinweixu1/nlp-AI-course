# project: extracting speech from the chinese news corpus
# author: github.com/xinweixu1
# date created:  May 11, 2019
# last updated:  May 24, 2019

# Step 1 - try the 'quote' annotator from the stanford-corenlp on a snippet of news article

############
# Attempt 1 - using 'stanfordcorenlp' wrapper developed by Lynten Guo -- failed!
# import the python API for CORENLP
# see github page here: https://github.com/Lynten/stanford-corenlp
# note -- this requires us to run code as root!
# $ sudo python script.py

#import logging # for debugging stanford-corenlp

#from stanfordcorenlp import StanfordCoreNLP
#nlp = StanfordCoreNLP(r'/Users/xinweixu/stanford-corenlp-full-2018-10-05', quiet=False)

# report error:
# socket.gaierror: [Errno 8] nodename nor servname provided, or not known

#text = 'Mary has a little lamb.'

#print(nlp.annotate(text))

#print('Tokenize:', nlp.word_tokenize(text))
#print('Part of Speech:', nlp.pos_tag(text))


# for chinese text:
#from stanfordcorenlp import StanfordCoreNLP

#sentence = '清华大学位于北京。'

#with StanfordCoreNLP(r'/Users/xinweixu/stanford-corenlp-full-2018-10-05', lang='zh') as nlp:
#    print(nlp.word_tokenize(sentence))
#    print(nlp.pos_tag(sentence))
#    print(nlp.ner(sentence))
#    print(nlp.parse(sentence))
#    print(nlp.dependency_parse(sentence))


#nlp.close()



#############
# Attempt 2 - using the 'stanford-corenlp' wrapper developed by stanfordnlp -- failed!
# github page: https://github.com/stanfordnlp/python-stanford-corenlp

# set the $CORENLP_HOME variable before calling the NLP client
#import os
#os.environ["CORENLP_HOME"]='/Users/xinweixu/stanford-corenlp-full-2018-10-05'

text = 'Mary has a little lamb.'

import corenlp
with corenlp.CoreNLPClient(annotators=['tokenize','pos','ner','depparse'], be_quiet=False) as client:
    text_annotated = client.annotate(text)

# report error:
# corenlp.client.PermanentlyFailedException: Timed out waiting for service to come alive.

print(text_annotated)

########
# Final Solution!
# Just run the following in terminal without using any python API .......
# cd path/to/stanford-corenlp-full-2018-10-05
# java -Xmx8192m -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLP -props StanfordCoreNLP-chinese.properties
#      -annotators tokenize,ssplit,pos,lemma,ner,parse,depparse,coref,quote
#      -file /path/to/input/file.txt
#      -outputFormat text (or json, xml)
#      -outputDirectory /path/to/output/dir

###########

