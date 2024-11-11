def check_cosecutive(arr):
    odd=0
    for i in arr:
        if i%2==1:
            odd+=1
            if odd==3:
                return True
        else:
            odd=0
    return False
print(check_cosecutive([1,2,3,3,3,4]))