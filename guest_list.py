people = ['Diana','Emma','Elvira','Maru','Janet']

print("Hi " + people[0] + " would you like go to dinner")
print("Hi " + people[1] + " would you like go to dinner")
print("Hi " + people[2] + " would you like go to dinner")
print("Hi " + people[3] + " would you like go to dinner")
print("Hi " + people[4] + " would you like go to dinner")

delete_person = 'Janet'
new_person = 'Ana'

print("Person to delete " + delete_person)
print("New person to invite " + new_person)

people.remove('Janet')
people.append(new_person)

print("------------------------------------------------")
print("Hi " + people[0] + " would you like go to dinner")
print("Hi " + people[1] + " would you like go to dinner")
print("Hi " + people[2] + " would you like go to dinner")
print("Hi " + people[3] + " would you like go to dinner")
print("Hi " + people[4] + " would you like go to dinner")

people.insert(0,'Claudia')
people.insert(3,'Laura')
people.append('Fernanda')

print("------------------------------------------------")
print("Hi " + people[0] + " would you like go to dinner")
print("Hi " + people[1] + " would you like go to dinner")
print("Hi " + people[2] + " would you like go to dinner")
print("Hi " + people[3] + " would you like go to dinner")
print("Hi " + people[4] + " would you like go to dinner")
print("Hi " + people[5] + " would you like go to dinner")
print("Hi " + people[6] + " would you like go to dinner")
print("Hi " + people[7] + " would you like go to dinner")

print("------------------------------------------------")
print("I'm sorry " + people.pop() + " you´re not invited yet")
print("I'm sorry " + people.pop() + " you´re not invited yet")
print("I'm sorry " + people.pop() + " you´re not invited yet")
print("I'm sorry " + people.pop() + " you´re not invited yet")
print("I'm sorry " + people.pop() + " you´re not invited yet")
print("I'm sorry " + people.pop() + " you´re not invited yet")
print(people)
print("Hi " + people[0] + " you´re still invited to dinner")
print("Hi " + people[1] + " you´re still invited to dinner")

print("People who have beeen invited to dinner: " + str(len(people)))
print("------------------------------------------------")
del people[0]
del people[0]
print(people)
print("People who have beeen invited to dinner: " + str(len(people)))
