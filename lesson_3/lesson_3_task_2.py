from smartphone import Smartphone

catalog=[]

catalog.append(Smartphone("Apple", "iPhone 15", "+79849675849"))
catalog.append(Smartphone("Samsung", "Galaxy S7", "+79780354675"))
catalog.append(Smartphone("Apple", "iPhone 13", "+79645324564"))
catalog.append(Smartphone("Honor", "7 pro", "+79467856434"))
catalog.append(Smartphone("Huawei", "9 Pro", "+7956342178"))

for phone in catalog:
    print(f"{phone.phone_brand} - {phone.phone_model}. {phone.subscriber_number}")