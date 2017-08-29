# hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
#以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
#

# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
import re

f = open('hightemp.txt')
data = f.readlines()
f.close()
ary = []
for line in data:
    line = line.replace('\n','')
    ary.append((re.split('\t+',line)))
ary = sorted(ary, key=lambda temp: temp[2],reverse=True)
for line_print in ary:
    print(line_print)
