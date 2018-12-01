# String part

name1 = "This is my first string"

print(name1)

# We use string contactinationoperator

print(name1 + str(2))

name2 = "I am adding few more lines"

print(name1 + name2)
first_name = 'kavitha'
last_name = 'bitra'

print(first_name + " " + last_name)

# Formatiing

your_name = input("what is your name")
your_age = input("what is your age")

print("Hi {} Nice to meet you. glad you are {} years of old".format(your_name, your_age))

subject = ["maths", "science", "social"]
print("I favorite subject is {},but i like {} and i am not good at {}".format(subject[0], subject[1], subject[2]))

#another print format
print("Hi %s Nice to meet you. glad you are %s years of old" % (your_name, your_age))
print("hey %s what is all about your %s" %(your_name,your_age))

n1 = 'kk'
n2 = 'bitra'

print(n1 + n2)