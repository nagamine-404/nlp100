# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

import re

#ファイル読み込み
f = open('hightemp.txt')
data = f.readlines()
f = open('hightemp.txt')
data_join = f.read()
f.close()
#print(data)

ary = []
for line in data:
    line = line.replace('\n','')
    ary.append((re.split('\t+',line)))

print(ary[0][0] in data_join)

#http://lightson.dip.jp/zope/ZWiki/032_e7_89_b9_e5_ae_9a_e3_81_ae_e6_96_87_e5_ad_97_e3_83_bb_e6_96_87_e5_ad_97_e5_88_97_e3_81_ae_e5_87_ba_e7_8f_be_e5_9b_9e_e6_95_b0_e3_82_92_e8_aa_bf_e3_81_b9_e3_82_8b
