List = [5,2,4,3,6,1,8,9,7]
fun = 0
def sort(List,fun):
    count=0
    for i in range(len(List)) :
        if count < len(List)-1 :#8
            if List[i]<List[i+1] :
                pass
            else :
                var=List[i]
                List[i]=List[i+1]
                List[i+1]=var
        else :
            continue
        count = count+1
    if fun < len(List):
        sort(List,fun=fun+1)
    else :
       print(List)
    
sort(List,fun)