def temp_convert(c):
    #gerhenhite to celcious convert
    if c<0:
        return print("farhenhite cant be negative value!")
    else:
        farhenhite =(9/5)*c + 32
        if farhenhite<10:
            return print("result: ",farhenhite," this temoarature is to low")
        elif farhenhite<10<20:
            return print("result:",farhenhite," this temparature is medium")
        elif 30>farhenhite>20:
            return print("result:",farhenhite, " the temparature is too heigh")
        else:
            return print("result:",farhenhite," this is not a appropiate temparature")    

        #return print (farhenhite)
    


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