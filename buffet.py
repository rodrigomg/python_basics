basic_foods = ("pizza","tacos","sopa","chiles en nogada","barbacoa")

print("Original menu")
for food in basic_foods:
    print("Basic food: " + food)

#Immutable do not forget
#basic_foods[3] = "pasta"

print("New menu")
basic_foods = ("carnitas","tacos","pasta","chiles en nogada","barbacoa")
for food in basic_foods:
    print("Basic food: " + food)

