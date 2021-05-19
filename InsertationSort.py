def inser(List):
    count=0
    for i in range(len(List)):
        
        if count < len(List)-1 :
            if List[i]<List[i+1]:
                pass
            else :
                var=List[i]
                List[i]=List[i+1]
                List[i+1]=var
                inser(List)
        else:
            continue
        count=count+1
    return List
    