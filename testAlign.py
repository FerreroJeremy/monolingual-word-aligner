# -*- coding: utf-8 -*

from aligner import *
import re
import sys
import unicodedata
import math

reload(sys)
sys.setdefaultencoding("utf-8")

input1 = open('input1.txt', 'r')
input2 = open('input2.txt', 'r')

sentences1 = input1.readlines()
print 'Input file 1 loaded.'

sentences2 = input2.readlines()
print 'Input file 2 loaded.'

df = {}
numberOfDocuments = 0

for lineId in range(0, len(sentences1)):
	tf = {}
	numberOfDocuments += 1
	sentence = re.findall(r"[\w]+", sentences1[lineId])
	for wordOffset in range(0, len(sentence)):
		word = sentence[wordOffset].lower()
		if word not in df:
			df[word] = 0
		if word not in tf:
			tf[word] = 1
			df[word] += 1

print 'Document frequencies of input file 1 computed.'

for lineId in range(0,len(sentences2)):
	tf = {}
	numberOfDocuments += 1
	sentence = re.findall(r"[\w]+", sentences2[lineId])
	for wordOffset in range(0, len(sentence)):
		word = sentence[wordOffset].lower()
		if word not in df:
			df[word] = 0
		if word not in tf:
			tf[word] = 1
			df[word] += 1

print 'Document frequencies of input file 2 computed.'

idf = {}

for word in df:
	idf[word] = math.log(numberOfDocuments / df[word])

print 'Inverse document frequencies computed.'

print '----- Comparison -----'

for lineId in range(0, len(sentences1)):
	sentence1 = re.findall(r"[\w]+", sentences1[lineId])
	sentence2 = re.findall(r"[\w]+", sentences2[lineId])

	numerator = 0
	denominator = 0

	for wordOffset in range(0, len(sentence1)):
		denominator += idf[sentence1[wordOffset].lower()]

	for wordOffset in range(0, len(sentence2)):
		denominator += idf[sentence2[wordOffset].lower()]

	commonWords = align(sentence1, sentence2)

	for sentenceId in range(0, len(commonWords)):
		for wordOffset in range(0, len(commonWords[sentenceId])):
			numerator += idf[commonWords[sentenceId][wordOffset].lower()]	
		
	score = "{0:.3f}".format(float(numerator) / float(denominator))

	#print 'line no ' + str(lineId) + ' computed with a score of ' + score
	print score
