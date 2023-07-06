mark=int(input("x "))
def scope():
    mark=int(input("y "))
    print(mark,"global or local variable")
scope()
def globalscope():
    print(mark,"certainly local?? or global??")
globalscope()
