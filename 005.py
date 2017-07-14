# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
import re
import ngram

def myfunction(seq):
    if isinstance(seq, str):
        index = ngram.NGram(N=2)
        for term in index.ngrams(index.pad(seq)):
            print (term)
    elif isinstance(seq, list):
        print("分岐できてる")


sequence = 'I am an NLPer'
sequence_nospace = sequence.replace(" ","")
myfunction(sequence_nospace)

sequence_li = re.split('\W+',sequence)
myfunction(sequence_li)

print(sequence_li)
