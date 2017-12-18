"""The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name.
These functions are throw-away functions, i.e. they are just needed where they have been created"""



def celcius(t):
    return (float(5)/9)*(t-32)

def fahrenheit(t):
    return (float(9)/5)*t + 32


temperature=[23,37,45,65,23]

Fh = map(lambda x: fahrenheit(x), temperature)
print(list(Fh))

cel=map(lambda x:celcius(x),temperature)
print(list(cel))