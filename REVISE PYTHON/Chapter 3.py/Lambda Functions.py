def func(f, n):
    print("This is the Answer----->",f(n))

twice = lambda x : x*2
thrice = lambda x : x*3
func(twice, 4)
func(thrice, 9)
