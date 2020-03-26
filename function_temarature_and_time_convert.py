def temp_convert(c):
    #gerhenhite to celcious convert
    farhenhite =(9/5)*c + 32
    return print(farhenhite)


def time_convert(m,s):
    hour = m/60 + s/3600
    return print(hour)

celcious = input("write temparature in celcious: ")
celcious = int(celcious)

minuites = input("enter amount of minuites: ")
minuites = int(minuites)

second = input("enter amount of second: ")
second = int(second)

temp_convert(celcious)
time_convert(minuites,second)