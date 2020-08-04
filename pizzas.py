pizzas = ['Mexicana','Pepperoni','Pastor','Carnes frías']

for pizza in pizzas:
    print('I like ' + pizza + " pizza")
print("I really love pizza!!")

friend_pizzas = pizzas[:]
friend_pizzas.append("Vegetariana")

for pizza in pizzas:
    print("My favorite pizzas are:" + pizza)

for pizza in friend_pizzas:
    print("My friend´s favorite pizzas are:" + pizza)
