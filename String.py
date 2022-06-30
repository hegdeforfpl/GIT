message = "Hello World"
print(message)
print(message[8])
print(message[0:5])
print(message[:5])
print(message[6:])
print(message.lower())
print(message.upper())
print(message.find('Hello'))
print(message.count('o'))
print(message.find('H'))
print(message.replace('World','Vishakh'))
greeting = "Hello"
name = "Vishakh"
new_message = greeting + " " + name
print(new_message)
new_message = '{}, {}. welcome!'.format(greeting,name)
print(new_message)
new_message = f'{greeting}, {name}. welcome!'
print(new_message)
new_message = f'{greeting.upper()}, {name.lower()}. welcome!'
print(new_message)
print(dir(new_message))
print(help(str))
print(help(str.lower))
