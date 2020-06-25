a,b,s = input().split()
a = int(a)
b = int(b)
s = int(s)
MaiorAB = (a+b+abs(a-b)) /2
MaiorAB2 = (MaiorAB+s+abs(MaiorAB-s)) /2
print("%i eh o maior" % MaiorAB2)