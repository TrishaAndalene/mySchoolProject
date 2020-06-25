N = int(input())
re1 = N //3600
N -= re1*3600
re2 = N //60
N -= re2*60
re3 = N //1
N -= re3*1
print("%i:%i:%i" % (re1,re2,re3))
