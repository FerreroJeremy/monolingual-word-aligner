# A Word Aligner for English

This is a word aligner for English: given two English sentences, it aligns related words in the two sentences.
It exploits the semantic and contextual similarities of the words to make alignment decisions.

## Contributions

Initially, this is a fork of <i>[ma-sultan/monolingual-word-aligner](https://github.com/ma-sultan/monolingual-word-aligner)</i>, the aligner presented in [Sultan et al., 2015](https://github.com/FerreroJeremy/monolingual-word-aligner/blob/master/docs/DLS%40CU-%20Sentence%20Similarity%20from%20Word%20Alignment%20and%20Semantic%20Vector%20Composition.pdf) that has been very successful in [SemEval STS (Semantic Textual Similarity) Task](https://github.com/FerreroJeremy/monolingual-word-aligner/blob/master/docs/SemEval-2016%20Task%201-%20Semantic%20Textual%20Similarity%2C%20Monolingual%20and%20Cross-Lingual%20Evaluation.pdf) in recent years.

But in 2016, the team UWB [(Brychcin and Svoboda, 2016)](https://github.com/FerreroJeremy/monolingual-word-aligner/blob/master/docs/UWB%20at%20SemEval-2016%20Task%201-%20Semantic%20Textual%20Similarity%20using%20Lexical%2C%20Syntactic%2C%20and%20Semantic%20Information.pdf) improves the aligner.
They introduce the consideration of IDF weighting in the Jaccard distance formula but without releasing the new source code.
And that's why I offer to share, in this repository, an implementation of this improvement.

In the `docs/` directory, you can find the papers cited above.

The results of the two different implementations on the SemEval-2016 STS task crosslingual track evaluation data are reported below.

Method | News | Multi-Src | Mean
--- | --- | ---| ---
The initial implementation of <i>[ma-sultan](https://github.com/ma-sultan/monolingual-word-aligner)</i> | 0.89604 | 0.71850 | 0.80831
The implementation with IDF weighting | 0.90601 | 0.81447 | 0.86078

And the results of the two different implementations on the SemEval-2017 STS task Spanish-English crosslingual track evaluation data are reported below.

Method | track4a | track4b | Mean
--- | --- | ---| ---
The initial implementation of <i>[ma-sultan](https://github.com/ma-sultan/monolingual-word-aligner)</i> | 0.66961 | 0.08250 | 0.37605
The implementation with IDF weighting | 0.76006 | 0.12447 | 0.44226

In the `semeval_data/` directory, you can find all the necessary data to repeat the tests by yourself. 
For the 2016 evaluation, there are two sets of data, called `news` and `multisource`.
For the 2017 evaluation, there are two sets of data, called `track4a` and `track4b`.
The gold standard (expected scores) for the four sets are also in the directory.
You can verify the correlation between the output of the aligner and the related gold standard file with the correlation Perl script as follow:

```
perl correlation.pl STS.gs.XXX.txt your_output_for_XXX.txt
```

## Requirements

1) Python [NLTK](http://www.nltk.org/install.html) <br/>
2) The [Python wrapper for Stanford CoreNLP](https://github.com/dasmith/stanford-corenlp-python)  

## Installation and Usage

1) Install the above tools. <br/>
2) Change line 107 of <i>corenlp.py</i>, from `rel, left, right = map(lambda x: remove_id(x), split_entry)` to `rel, left, right = split_entry`

3) Install the NLTK stopword corpus and <i>jsonrpclib</i>. <br/>

```
python -m nltk.downloader stopwords
sudo pip install jsonrpclib
```

4) Download the aligner.

```
git clone https://github.com/FerreroJeremy/monolingual-word-aligner.git
```

5) Run the `corenlp.py` script to launch the server:  
```
python stanford-corenlp-python/corenlp.py
```

6) Wait the loading of the models, once completed you should see in the terminal:

```
Loading Models: 5/5                                                                                                                       
INFO:__main__:Serving on http://127.0.0.1:8080
```

7) In another terminal, run the `testAlign_idf.py` script to launch the comparison between the specified files in the source code:  
```
python testAlign_idf.py
```
