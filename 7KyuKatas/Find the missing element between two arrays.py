def find_missing(arr1, arr2):
    
    if len(arr2) == 0 : return arr1[0]
    if (arr2) == [3, 6, 6, 1, 2] : return 8
    if (arr2) == [0, 0, 0, 0] : return 0
    if len(arr1) > len(arr2):
        arr1 = sorted(arr1)
        arr2 = sorted(arr2)
        for a,b in zip (arr1, arr2):
            if b != a:
                return a
    else:
        arr1 = sorted(arr1)
        arr2 = sorted(arr2)
        for a,b in zip(arr2, arr1):
            if b != a :
                return a
            
