for number in range(1,21):
    print(number)

one_million = range(1,10000001)
#for number in one_million:
#    print(number)

print(min(one_million))
print(max(one_million))

odd_numbers = range(1,20,2)
for odd_number in odd_numbers:
    print(odd_number)

multiples_of_three = range(3,30,3)
for multiple_of_three in multiples_of_three:
    print(multiple_of_three)

cubes = [value**3 for value in range(1,10)]
print(cubes)
