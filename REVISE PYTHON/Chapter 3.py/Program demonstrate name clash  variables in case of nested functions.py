def outer_fuc():
    var = 200
    def inner_fuc():
        var = 3434
        print("This will be the value of the Inner fucntions-->", var)
    inner_fuc()
    print("This will be the value of the Inner fucntions-->",var)
outer_fuc()