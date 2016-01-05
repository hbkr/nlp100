# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def char_ngram(s, n):
    return [s[i:i+n] for i in range(len(s)-n+1)]

def word_ngram(s, n):
    words = [word.strip(".,") for word in s.split()]
    return tuple([words[i:i+n] for i in range(len(words)-n+1)])  

s = "I am an NLPer I am an NLPer"

print(char_ngram(s, 2))
print(word_ngram(s, 2))

