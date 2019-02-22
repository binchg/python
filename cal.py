import math
def log2(a):
    return math.log2(a)
def Ent(a,b):
    if(a==b):
        return 0
    p1=a/b
    p2=1-p1
    return -(p1*log2(p1)+p2*log2(p2))
def Gain(list):
    l1 = list[::2]
    l2 = list[1::2]
    a = l1[0]
    b = l2[0]
    al = l1[1::]
    bl = l2[1::]
    sum = 0
    print("################")
    print("Ent(%d,%d)=%f"%(a,b,Ent(a, b)))
    for i in range(0, len(al)):
        print("Ent(%d,%d)=%f"%(al[i],bl[i],Ent(al[i], bl[i])))
        sum += bl[i] / b * Ent(al[i], bl[i])
    gain = Ent(a,b) - sum
    print("Gain=%f"%(gain))
    return Gain
list=[8,17,3,6,4,6,1,5]
Gain(list)
list=[8,17,5,8,3,7,2,2]
Gain(list)
list=[8,17,6,10,2,5,2,2]
Gain(list)
list=[8,17,7,9,1,5,3,3]
Gain(list)
list=[8,17,5,7,3,6,4,4]
Gain(list)
list=[8,17,6,12,2,5]
Gain(list)


# print(a[1::],b[1::])
# print(Ent(1,5))