favorite_languages = {
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'ptthon',
        }

for name, language in favorite_languages.items():
    print(name.title() + "s favorite language is " + language.title()+ ".")

print(favorite_languages)

print("Sarah´s favorite language is " +
        favorite_languages['sarah'].title() +
        ".")
