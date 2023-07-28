def create(dataset: dict, data: dict):
    dataset.update(data)
    return dataset

def update(dataset: dict, phone: str, data: dict):
    if phone in dataset:
        for key, value in data.items():
            if value:
                dataset[phone][key] = value
        return dataset
    else:
        print(f'Запис з номером телефону {phone} не знайдено.')
        return dataset

def delete(dataset: dict, phone: str):
    if phone in dataset:
        del dataset[phone]
        print(f'Запис з номером телефону {phone} був видалений.')
    else:
        print(f'Запис з номером телефону {phone} не знайдено.')
    return dataset
