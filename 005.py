# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
import re
import ngram

def myfunction(seq):
    index = ngram.NGram(N=2)
    for term in index.ngrams(index.pad(seq)):
        print (term)


sequence = 'I am an NLPer'
sequence.translate(" ")
print(sequence)
myfunction(sequence)
