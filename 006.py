# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

import ngram

x_sentence = "paraparaparadise"
y_sentence = "paragraph"
bi_gram_list = []

def bigram(sentence):
    index = ngram.NGram(N=2)
    for term in index.ngrams(index.pad(sentence)):
        bi_gram_list.append(term)
    return (bi_gram_list)

X = bi_gram_list
print("＝＝＝これはX＝＝＝")
print (bigram(x_sentence))

bi_gram_list = []
bigram(y_sentence)
Y = bi_gram_list
print("＝＝＝これはY＝＝＝")
print (Y)

print("＝＝＝積集合＝＝＝")
print(set(X).intersection(set(Y)))
print("＝＝＝和集合＝＝＝")
print(set(X) and set(Y))
print("＝＝＝差集合(X-Y)＝＝＝")
print(set(X)-set(Y))
print("＝＝＝差集合(Y-X)＝＝＝")
print(set(Y)-set(X))
