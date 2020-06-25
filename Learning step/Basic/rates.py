#This program counts time rates
print ("Please input rate and distance")
rate = float(input("Rate : "))
distance = float(input("Distance : "))

#process

times = distance/rate

#output
print("The times you need : %.2f s " % (times))