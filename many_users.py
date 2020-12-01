users = {
        'aeinstein': {
            'firts':'albert',
            'last':'einstein',
            'location':'proncenton',
            },
        'mcurie':{
            'firts':'marie',
            'last':'curie',
            'location':'paris',
            },
        }

for username, user_info in users.items():
    print("\nUsername:" + username)
    full_name = user_info['firts'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name:" + full_name.title())
    print("\tLocation:" + location.title())
