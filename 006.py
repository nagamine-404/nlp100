# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

import ngram

x_sentence = "paraparaparadise"
y_sentence = "paragraph"
x_list = []

sentence = x_sentence

def bigram(sentence):
    index = ngram.NGram(N=2)
    for term in index.ngrams(index.pad(x_sentence)):
        x_list.append(term)
return (bigrams)
