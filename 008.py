# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(sentence):
    list_sentence = []
    list_sentence = list(sentence)
    return(list_sentence)

sentence = "apple"
cipher(sentence)
print(list_sentence)
print(ord("a"))
#print(unicode('あ',encording='utf-8'))
#print('あ'.decode('utf-8'))