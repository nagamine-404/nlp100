# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(sentence):
    ary_sentence = []
    ary_sentence = list(sentence)
    rtn_sentence = []
    rtn_word = ""
    for stnc in ary_sentence:
        if 219-ord(stnc) >0 and 219-ord(stnc) < 154:
            rtn_sentence.append(chr(219-ord(stnc)))
        else:
            rtn_sentence.append(stnc)
    rtn_word="".join(rtn_sentence)
    return(rtn_word)

sentence = "Apple"
print(sentence)
print_sentence=cipher(sentence)
print(print_sentence)
print_sentence=cipher(print_sentence)
print("".join(print_sentence))

