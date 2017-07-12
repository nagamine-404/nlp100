#
# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
import re

sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

pi = []

pi =  re.split('\W+',sentence)

alphabet = []

print((pi[0])[:1])


# upper-case A-Z
uppercase = [chr(i) for i in range(65,65+26)]

# lower-case a-z
lowercase = [chr(i) for i in range(97,97+26)]



alphabet.append(uppercase)
alphabet.append(lowercase)

print(alphabet)


print (uppercase.index('B'))

for word in range(pi)
    uppercase.index(pi[word])
    
