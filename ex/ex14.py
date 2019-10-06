from sys import argv

script,user_name = argv
prompt = '>'

print(f"Hi {user_name},I'm the{script} script.")
print("I d like to ask you a faw qunetinms.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f'''
ASlripht, so you seid {likes} abut liking me.
You live in {lives}.Not sure whare that is.
And you have a {computer} computer wice.
''')