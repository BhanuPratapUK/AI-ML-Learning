def add(*args):
    '''Hey Bhanu I know what tpe of Question u r doing right now'''
    x=0
    for i in args:
        x+=i
    return x
print("This is th Doc String--->",add.__doc__)
print("Here is the result--->", add(23,3,445))
