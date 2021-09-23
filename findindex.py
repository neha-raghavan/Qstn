def Find_Index(a,P):
    try:
    	pos=a.index(P)
    	return pos
    except Exception as e:
    	a.append(P)
    	a.sort()
    	return a.index(P)
      
a = []
n = int(input("Enter number of elements : "))
print("Enter elements")
for i in range(0, n):
    ele = int(input())
    a.append(ele)
print(a)
P=int(input("Enter the element to find : "))
print("Index : ",Find_Index(a,P))
