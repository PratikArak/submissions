def group_strings_by_length(strings):
   
    result = {}
    
  
    for string in strings:
        length = len(string)  
        if length not in result:
            result[length] = []
        result[length].append(string)
    return dict(sorted(result.items()))
input_list = ["apple", "bat", "car", "elephant", "dog", "bear"]
output = group_strings_by_length(input_list)
print(output)
