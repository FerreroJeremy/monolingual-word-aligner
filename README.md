# A Word Aligner for English

This is a word aligner for English: given two English sentences, it aligns related words in the two sentences. It exploits the semantic and contextual similarities of the words to make alignment decisions.

## Contributions

Initially, this is a fork of [ma-sultan/monolingual-word-aligner](https://github.com/ma-sultan/monolingual-word-aligner), the aligner presented in [(Sultan et al., 2015)](http://www.aclweb.org/anthology/S15-2027) that has been very successful in [SemEval STS (Semantic Textual Similarity) Task](https://aclweb.org/anthology/S/S16/S16-1081.pdf) in recent years.

But in 2016 the team UWB [(Brychcin and Svoboda, 2016)](https://www.aclweb.org/anthology/S/S16/S16-1089.pdf) improves the aligner. They introduce the IDF weight in the initial distance Jaccard formula but without distributing the new source code. This repository is an implementation of this improvement.

In the <i>semeval_data/</i> directory, you can find all the necessary data to repeat the tests yourself. There are two sets of data, called <i>news</i> and <i>multisource</i>. You can verify the correlation between the output of the aligner and the gold standard of the evaluation with the correlation perl script as follow :

```
./correlation.pl  STS.gs.XXX.txt  your_output.txt
```

The results of the different implementations on the SemEval 2016 STS evaluation data below.

Method | News | Multi-Src | Mean
--- | --- | ---| ---
The initial implementation of <i>ma-sultan</i> without IDF consideration | 0.89604 | 0.71850 | 0.80831
This implementation with IDF consideration | 0.90601 | 0.81447 | 0.86078

## Requirements

1. Python [NLTK](http://www.nltk.org/install.html)
2. The [Python wrapper for Stanford CoreNLP](https://github.com/dasmith/stanford-corenlp-python)  

## Installation and Usage

1. Install the above tools.
2. Change line 100 of corenlp.py, from :
```
rel, left, right = map(lambda x: remove_id(x), split_entry)
```
to 
```
rel, left, right = split_entry
```

3. Install the NLTK stopword corpus and jsonrpclib
4. Download the aligner

```
python -m nltk.downloader stopwords
sudo pip install jsonrpclib
git clone https://github.com/ma-sultan/monolingual-word-aligner.git
```

5. Run the corenlp.py script to launch the server:  
```
python testAlign.py
```
