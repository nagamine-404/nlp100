# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
import re
import ngram

def myfunction(seq):
    if isinstance(seq, str):
        print("＝＝＝文字bi-gram＝＝＝")
        index = ngram.NGram(N=2)
        for term in index.ngrams(index.pad(seq)):
            print (term)
    elif isinstance(seq, list):
        print("＝＝＝単語bi-gram＝＝＝")
        for (word,count) in zip(seq,range(len(seq))):
            sec_word = ""
            if len(seq) >= count and count <= len(seq)-2 :
                sec_word = "-" + seq[count+1]
            print(word +  sec_word)

sequence = 'I am an NLPer'
sequence_nospace = sequence.replace(" ","")
myfunction(sequence_nospace)

sequence_li = re.split('\W+',sequence)
myfunction(sequence_li)
