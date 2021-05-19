'''List = [1,2,3,4,5,6,7,8,9,10]
ser = input("Enter a Num : ")
i=0
Val = len(List)
def Search(List,ser,i):
    var = List[i]
    sar = ser
    if var == sar :
        print("Found")
    else :
        i=i+1
        if i < 10 :
            Search(List,ser,i)
        else :
            pass
Search(List,ser,i)'''
List=[1,2,3,4,5,6,7,8,9,10]
ser = int(input("Enter a no to Search : "))
count=0
for i in range(len(List)):
    if List[i]==ser:
        print("Found :","Position",i,"Value",List[i])
    else :
        count=count+1
        continue
if count==len(List):
    print("Not Found")
else :
    pass