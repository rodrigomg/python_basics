alien_O = {'color':'green','points':5}

print(alien_O['color'])
print(alien_O['points'])
print(alien_O)

alien_O['x_position'] = 0
alien_O['y_position'] = 25
print(alien_O)


new_points = alien_O['points']
print("You just earned " + str(new_points) + " points")

alien_E = {}

alien_E['color'] = 'green'
alien_E['points'] = 5

print(alien_E)

alien_E['color'] = 'yellow'

print("The alien is now " + alien_E['color'] +".")

alien_P = {'x_position':0, 'y_position':25,'speed':'medium'}
print("Original x-position: " + str(alien_P['x_position']))

# Move the alien to the right.
# Determine how far to move the alien bades on its current speed.

if alien_P['speed'] == 'slow':
    x_increment = 1
elif alien_P['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# Thw new position is de old position plus the increment.

alien_P['x_position'] =alien_P['x_position'] + x_increment

print("New x_position: " + str(alien_P['x_position']))

alien_O = {'color':'green','points':5}
print(alien_O)
del alien_O['points']
print(alien_O)
