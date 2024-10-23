def reverse_by_n(lst, n):
    result = []
    for i in range(0, len(lst), n):
  
        temp = []
        
        for j in range(min(n, len(lst) - i)):
            temp.insert(0, lst[i + j])
        
        result.extend(temp)
    
    return result


print(reverse_by_n([1, 2, 3, 4, 5, 6, 7, 8], 3))  # Output: [3, 2, 1, 6, 5, 4, 8, 7]

