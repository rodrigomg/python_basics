cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here´s the original list:")
print(cars)
print("\nHere´s the sorted list:")
print(sorted(cars))
print("\nHere´s the original list again:")
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nreverse:")
print(cars)
cars.reverse()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
