# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
import re
sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
pi =  re.split('\W+',sentence)
ans = ''
for count in pi:
    ans += str(len(count))
print (ans)
