a = float(input())
print("NOTAS:")
re = a //100
a -= re*100
print("%i nota(s) de R$ 100.00" % re)
re = a //50
a -= re*50
print("%i nota(s) de R$ 50.00" % re)
re = a //20
a -= re*20
print("%i nota(s) de R$ 20.00" % re)
re = a //10
a -= re*10
print("%i nota(s) de R$ 10.00" % re)
re = a //5
a -= re*5
print("%i nota(s) de R$ 5.00" % re)
re = a //2 
a -= re*2
print("%i nota(s) de R$ 2.00" % re)
print("MOEDAS:")
re = a //1
a -= re*1
print("%i moeda(s) de R$ 1.00" % re)
re = a //0.5
a -= re*0.5
print("%i moeda(s) de R$ 0.50" % re)
re = a //0.25
a -= re*0.25
print("%i moeda(s) de R$ 0.25" % re)
re = a //0.10
a -= re*0.10
print("%i moeda(s) de R$ 0.10" % re)
re = a //0.05
a -= re*0.05
print("%i moeda(s) de R$ 0.05" % re)
re = a //0.01
a -= re*0.01
print("%i moeda(s) de R$ 0.01" % re)