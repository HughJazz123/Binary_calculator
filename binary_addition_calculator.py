"""
This calculator calculaters 2bits+2bits
"""


def space():
    print("\n"*40)

def AND(a,b):
    if a==1 and b==1:
        return 1
    else:
        return 0

def OR(a,b):
    if a==1 or b==1:
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



def process(x1,x2,y1,y2):
    z3 = XOR(x2,y2)
    
    and1 = AND(x2,y2)
    xor1 = XOR(x1,y1)

    z2 = XOR(xor1,and1)

    and2=AND(and1,xor1)
    and3=AND(x1,y1)

    z1=OR(and2,and3)

    output=str(z1)+str(z2)+str(z3)
    return output

def main():
    while True:
        input1=input("Enter binary string 1: ")
        input2=input("Enter binary string 2: ")

        x1=int(input1[0])
        x2=int(input1[1])
        y1=int(input2[0])
        y2=int(input2[1])
        space()
        print(process(x1,x2,y1,y2))
    
if __name__ == "__main__":
    main()
