# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

from random import random

typo = lambda s: " ".join(t[0]+"".join(sorted(t[1:-1], key=lambda k:random()))+t[-1] if len(t) > 4 else t for t in s.split())

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typo(s))

