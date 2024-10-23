import re

def find_all_dates(text):

    date_pattern = r'(\b\d{2}-\d{2}-\d{4}\b)|(\b\d{2}/\d{2}/\d{4}\b)|(\b\d{4}\.\d{2}\.\d{2}\b)'
    
    matches = re.findall(date_pattern, text)
    

    valid_dates = [match for group in matches for match in group if match]
    
    return valid_dates
text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
output = find_all_dates(text)
print(output)  # Output: ['23-08-1994', '08/23/1994', '1994.08.23']
