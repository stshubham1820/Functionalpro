List = [1,2,3,4,5,6,7,8,9]
ser = int(input("Enter a number You want to search :"))

def sar(Listo,ser) :
    List3=[]

    mid = int(len(Listo)/2)
    s=ser
    #print(mid)
    if s == Listo[mid] :
        print("Found :",Listo[mid],"Position :",mid)
    elif s<Listo[mid] :
        for i in range(mid):
            
            List3.insert(i,Listo[i])
            
        Listo=List3
        print(Listo)
        sar(Listo,ser)

    else :
        for i in range(mid+1,len(Listo)):
            List3.insert(i,Listo[i])
        Listo=List3  
        print(Listo)
        sar(Listo,ser)

sar(List,ser)
