favorite_languages = {
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phill':'ptthon',
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

print("Sarah´s favorite language is " +
        favorite_languages['sarah'].title() +
        ".")

favorite_languages = {
        'jen': ['python','ruby'],
        'sarah': ['c'],
        'edward': ['ruby','go'],
        'phil': ['python','haskell'],
        }

for name,languages in favorite_languages.items():
    if len(languages) > 1:
         print("\n" + name.title() + "`s favorite languages are:")
    else:
         print("\n" + name.title() + "`s favorite language is:")

    for language in languages:
        print("\t" + language.title())
