N = int(input())
print(N)
re = N //100
N -= re*100
print("%i nota(s) de R$ 100,00" % (re))
re = N //50
N -= re*50
print("%i nota(s) de R$ 50,00" % (re))
re = N //20
N -= re*20
print("%i nota(s) de R$ 20,00" % (re))
re = N //10
N -= re*10
print("%i nota(s) de R$ 10,00" % (re))
re = N //5
N -= re*5
print("%i nota(s) de R$ 5,00" % (re))
re = N //2
N -= re*2
print("%i nota(s) de R$ 2,00" % (re))
re = N //1
print("%i nota(s) de R$ 1,00" % (re))