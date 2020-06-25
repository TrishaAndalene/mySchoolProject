a = int(input())
re = a //365
a -= re*365
print("%i ano(s)" % re)
re = a //30
a -= re*30
print("%i mes(es)" % re)
re = a //1
a -= re*1
print("%i dia(s)" % re)