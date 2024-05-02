#Volume of a rectangular prism
def Rectangular_volume(l,w,h):
    return l*w*h

l = int(input("Length: "))
w = int(input("Width: "))
h = int(input("Height: "))

print("Volume is " +str(Rectangular_volume(l,w,h)))