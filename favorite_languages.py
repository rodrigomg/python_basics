favorite_languages = {
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phill':'python',
        'rock':'python',
        }

for name, language in favorite_languages.items():
    print(name.title() + "s favorite language is " + language.title()+ ".")

for name in favorite_languages.keys():
    print(name.title())

friends = ['phill','sarah']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " +favorite_languages[name].title()+ "!")

    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our pool!")

print(favorite_languages)

print("Sarah's favorite language is " +
        favorite_languages['sarah'].title() +
        ".")

for name in sorted(favorite_languages.keys()):
    print(name.title()+" , thank you for taking the poll.")

print("The following languages have been mentioned;")
for name in favorite_languages.values():
    print(name.title())
print("The following languages have been mentioned; unique cases")
for name in set(favorite_languages.values()):
    print(name.title())
