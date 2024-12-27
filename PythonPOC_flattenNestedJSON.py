import pandas as pd
from pandas import json_normalize

# Function to recursively flatten the nested JSON
def flatten_json(nested_json, parent_key='', sep='_'):
    flat_dict = {}
    
    # Iterate through the keys in the nested JSON
    for k, v in nested_json.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        
        # If value is a dictionary, recursively flatten it
        if isinstance(v, dict):
            flat_dict.update(flatten_json(v, new_key, sep=sep))
        
        # If value is a list, flatten the list elements (if list of dicts)
        elif isinstance(v, list):
            if len(v) > 0 and isinstance(v[0], dict):  # Check if list contains dictionaries
                for i, item in enumerate(v):
                    flat_dict.update(flatten_json(item, f"{new_key}_{i}", sep=sep))
            else:  # If list contains primitive values
                flat_dict[new_key] = v
        else:
            flat_dict[new_key] = v
    
    return flat_dict

# Sample nested JSON
nested_json = {
    "id": 1,
    "name": "John Doe",
    "contact": {
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    },
    "address": {
        "street": "123 Main St",
        "city": "Somewhere",
        "zipcode": "12345",
        "geo": {
            "lat": 40.7128,
            "lng": -74.0060
        }
    },
    "orders": [
        {
            "order_id": 101,
            "product": "Laptop",
            "quantity": 1
        },
        {
            "order_id": 102,
            "product": "Smartphone",
            "quantity": 2
        }
    ]
}

# Flatten the nested JSON
flattened_json = flatten_json(nested_json)

# Convert the flattened JSON to a pandas DataFrame
df = pd.DataFrame([flattened_json])

# Print the DataFrame
print(df)
