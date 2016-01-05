# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def n_gram(s, n):
    words = s
    return {tuple(words[i:i+n]) for i in range(len(words)-n+1)}

s = "I am an NLPer I am an NLPer"

print(n_gram(s, 2))
print(n_gram([t.strip(".,") for t in s.split()], 2))

