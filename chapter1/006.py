# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

n_gram = lambda s, n: {tuple(s[i:i+n]) for i in range(len(s)-n+1)}

X = n_gram("paraparaparadise", 2)
Y = n_gram("paragraph", 2)

print("X: %s" % X)
print("Y: %s" % Y)
print("union: %s" % str(X|Y))
print("difference: %s" % str(X-Y))
print("intersection: %s" % str(X&Y))

if n_gram("se", 2) <= X: print("'se' is included in X.")
if n_gram("se", 2) <= Y: print("'se' is included in Y.")

