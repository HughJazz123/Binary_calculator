"""
Binary addition calculat version 2, calculates 3 bits + 3 bits
"""

def space():
    print("\n"*40)

def AND(a,b):
    if a==1 and b==1:
        return 1
    else:
        return 0

def XOR(a,b):
    if a==1 or b==1:
        if a==1 and b==1:
            return 0
        else:
            return 1
    else:
        return 0


def process(x1,x2,x3,y1,y2,y3):
    xor1=XOR(x1,y1)
    and1=AND(x1,y1)
    xor2=XOR(x2,y2)
    and2=AND(x2,y2)
    xor3=XOR(x3,y3)
    and3=AND(x3,y3)

    xor4=XOR(and1,xor2)
    and4=AND(and1,xor2)
    xor5=XOR(and2,xor3)
    and5=AND(and2,xor3)

    xor6=XOR(and4,xor5)
    and6=AND(and4,xor5)
    
    xor7=XOR(and3,and5)
    xor8=XOR(and6,xor7)

    z1=xor1
    z2=xor4
    z3=xor6
    z4=xor8

    output=str(z4)+str(z3)+str(z2)+str(z1)
    return output
    
def main():
    while True:
        input1=input("Enter binary string 1 (3 bits): ")
        input2=input("Enter binary string 2 (3 bits): ")

        X1=input1[2]
        X2=input1[1]
        X3=input1[0]

        Y1=input2[2]
        Y2=input2[1]
        Y3=input2[0]

        print("output: "+process(int(X1),int(X2),int(X3),int(Y1),int(Y2),int(Y3)))

if __name__=="__main__":
    main()
