cities = ["Rome", "New-York", "London", "Tokyo", "Tel-Aviv"]

for city in cities:
    l = len(city)
    print(f"the length of {city} is {l}")
    if city.count("-")>0:
        print(f'found city with - , city name is {city}')
