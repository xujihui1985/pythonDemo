def print_args(arg1,arg2,*args):
    print(arg1)
    print(arg2)
    print(args)

def color(red, green, blue, **kwargs):
    print("r = ", red)
    print("g = ", green)
    print("b = ", blue)
    print(kwargs)

t = (11,12,13,14,15,16)

print_args(*t)

c = {'red':21, 'green':68, 'blue':120, 'alpha':52}

color(**c)




