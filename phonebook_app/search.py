def search_record(dataset, search_type, value):
    result = {}
    if search_type == 'sp':
        for phone in dataset:
            if value in phone:
                result.update({phone: dataset[phone]})
    elif search_type == 'sf':
        for phone, data in dataset.items():
            if value.lower() in data['first_name'].lower():  # Case-insensitive search
                result.update({phone: data})
    elif search_type == 'sl':
        for phone, data in dataset.items():
            if value.lower() in data['last_name'].lower():  # Case-insensitive search
                result.update({phone: data})
    elif search_type == 'sfl':
        for phone, data in dataset.items():
            full_name = f"{data['first_name']} {data['last_name']}".lower()
            if value.lower() in full_name:  # Case-insensitive search
                result.update({phone: data})
    elif search_type == 'sct':
        for phone, data in dataset.items():
            if value.lower() in data['city'].lower():  # Case-insensitive search
                result.update({phone: data})
    elif search_type == 'sc':
        for phone, data in dataset.items():
            if value.lower() in data['country'].lower():  # Case-insensitive search
                result.update({phone: data})
    return result
