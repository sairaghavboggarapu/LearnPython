class robot:
    forward=0
    backward=0
    leftside=0
    rightside=0
    def fwd(self,a):
        robot.forward+=a
    def bwd(self,a):
        robot.backward+=a
    def left(self,a):
        robot.leftside+=a
    def right(self,a):
        robot.rightside+=a
m=robot()
m1=input("Switching:")
print("f-Forward\nb-Backward\nl-leftside\nr-rightside")
while (m1=="on"):
    m2=input("enter the direction:")
    if m2=="f":
          a=int(input("enter the steps:"))
          m.fwd(a)
    elif m2=="b":
        m.bwd(a)
        a=int(input("enter the steps:"))
    elif m2=="l":
        a=int(input("enter the steps:"))
        m.left(a)
    elif m2=="r":
        a=int(input("enter the steps:"))
        m.right(a)
    elif m2=="off":
        total_movements=robot.forward+robot.backward+robot.leftside+robot.rightside
        print("forward steps count:",robot.forward)
        print("backward steps count:",robot.backward)
        print("left steps count:",robot.leftside)
        print("right steps count:",robot.rightside)
        print("Total steps count:",total_movements)
        print("robot switching off")
        break
    else:
        print("sorry wrong command")
