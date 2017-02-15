# -*- coding: utf-8 -*

from aligner import *
import re
import sys
import unicodedata
import math

reload(sys)
sys.setdefaultencoding("utf-8")

output = open('output.track4b.txt', 'a')

input1 = open('semeval_data/multi.sentences.en.txt', 'r')
input2 = open('semeval_data/multi.sentences.es-en.txt', 'r')

# input1 = open('semeval_data/news.sentences.en.txt', 'r')
# input2 = open('semeval_data/news.sentences.es-en.txt', 'r')

sentences1 = input1.readlines()
print 'Input file 1 loaded.'

sentences2 = input2.readlines()
print 'Input file 2 loaded.'

print '----- Comparison -----'

for lineId in range(0, len(sentences1)):
	sentence1 = re.findall(r"[\w]+", sentences1[lineId])
	sentence2 = re.findall(r"[\w]+", sentences2[lineId])

	numerator = 0
	denominator = len(sentence1) + len(sentence2)

	commonWords = align(sentence1, sentence2)

	for sentenceId in range(0, len(commonWords)):
		numerator += len(commonWords[sentenceId])
		
	score = "{0:.3f}".format(float(numerator) / float(denominator))

	output.write(score + '\n')
	#print 'line no ' + str(lineId) + ' computed with a score of ' + score

output.close()
