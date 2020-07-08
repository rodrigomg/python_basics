motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ktm')
print(motorcycles)

motorcycles = []
motorcycles.append('ktm')
motorcycles.append('honda')
motorcycles.append('yamaha')
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
first_motorcycle = motorcycles.pop(0)
print(motorcycles)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")
print("The firs motorcycle I owned was a " + first_motorcycle.title() + ".")

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)
