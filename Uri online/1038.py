X,Y = input().split()
X,Y = int(),int()

#X = key
#Y = value
price = {
	1 : 4,00,
	2 : "4,50",
	3 : "5,00",
	4 : "2,00",
	5 : "1,50"
}

result: price[X]*Y

print("Total: R$ %.2f" % (result))