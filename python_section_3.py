def flatten_dict(d, parent_key='', sep='.'):
    items = []

    for k, v in d.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k

        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        

        elif isinstance(v, list):
            for index, item in enumerate(v):
                list_key = f'{new_key}[{index}]'
                if isinstance(item, dict):
               
                    items.extend(flatten_dict(item, list_key, sep=sep).items())
                else:
                    
                    items.append((list_key, item))
        else:

            items.append((new_key, v))
    
    return dict(items)


nested_dict = {
    "name": "John",
    "details": {
        "age": 30,
        "contacts": [
            {"type": "email", "value": "john@example.com"},
            {"type": "phone", "value": "123-456-7890"}
        ],
        "address": {
            "street": "123 Main St",
            "city": "New York"
        }
    }
}

flattened = flatten_dict(nested_dict)
print(flattened)
