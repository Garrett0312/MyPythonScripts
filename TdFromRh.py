import math
def rh2dpt(T,rh):
    
    K = (T-32)*(5/9)+273.15
    #print(K)
    DewK = -1/(((math.log(math.exp((5423)*((1/273)-(1/K)))*(rh/100))/5423))-(1/273))
    #print(DewK)
    Dew = round((DewK-273.15)*(9/5)+32,2)
    return(Dew)
    #print(Dew)
t = int(input("What is the temperature?\n\n"))
RH = int(input("What is the Relative Humidity?\n\n"))

result = rh2dpt(t,RH)
print(result)
