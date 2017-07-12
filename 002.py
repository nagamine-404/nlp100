# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
#
a = 'パトカー'
b = 'タクシー'
a_len = len(a)
b_len = len(b)
ab = []

for count in range(a_len):
    a_str = a[count]
    b_str = b[count]
    ab.append(a_str)
    ab.append(b_str)

ab ="".join(ab)
print (ab)
