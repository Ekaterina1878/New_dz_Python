from smartphone import Smartphone

catalog = [
    Smartphone("Samsung Galaxy", "S24 Ultra", "+79119111199"),
    Smartphone("Apple IPhone", "16 Pro Max", "+79051454545"),
    Smartphone("Xiaomi", "Redmi Note 14", "+79212912191"),
    Smartphone("Honor", "X9A", "+79111190808"),
    Smartphone("Huawei nova", "Y91", "+79152477474")
]

for smartphone in catalog:
    print(f"{smartphone.phone_brand}-"
          f"{smartphone.phone_model}. {smartphone.number}")
