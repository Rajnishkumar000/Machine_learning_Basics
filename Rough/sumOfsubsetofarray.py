def sum(arr,index=0,cur=0):
    if index==len(arr):
        print(cur)
        return
    sum(arr,index+1,cur+arr[index])
    sum(arr,index+1,cur)
sum([1,2,3])
