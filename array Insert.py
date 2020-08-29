def insertAny(arr,value,position):
    arr1=[]
    if position==1:  #If Number is inserted on the 0th Index
        arr1.append(value)     
        for n in range(0,(len(arr))):
            arr1.append(arr[n])
        return arr1
    elif position==len(arr):     # if number is inserted on last index
        for i in range(0,len(arr)):
            arr1.append(arr[i])
        arr1.insert(position,value)
        return arr1

    else:       #if number is inserted in between
        for i in range(0,position):
            arr1.append(arr[i])
        arr1.insert(position-1,value)
        for n in range(position,len(arr)):
            arr1.append(arr[n])
        return arr1


arr = list(map(int,input('Enter Array: ').split()))

value=int(input('Enter the Number to be inserted: '))

position=int(input('Enter the position of the number to be inserted: '))

print(insertAny(arr,value,position))




