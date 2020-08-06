my_foods = ['pizza','falafel','carrot cake','steak','tacos']

friend_foods = my_foods[:]
# Don´t do this ¬¬
#friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend´s favorite foods are:")
print(friend_foods)

print(my_foods[:3])
print(my_foods[1:4])
print(my_foods[3:])

for food in my_foods:
    print("My food: " + food)

for food in friend_foods:
    print("My friend´s food: " + food)
