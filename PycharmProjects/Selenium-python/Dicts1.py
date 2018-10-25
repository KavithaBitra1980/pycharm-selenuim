#Learning Dictionaries

car = {"make": "bmw" ,"model":"550i","year":2016}
print(car)
print(car['make'])
print(car["year"])

print('-------------------------------------')
person = { 'name':'smith','address':'123 main street','Business':'456 market street'}
print(person)
print(person['name'])
print(person['address'])

person['city'] = 'nashua'

print(person)

print('city ' not in person)

d = {}

d['one'] = 1
d['two'] = 2
print(d)

person['mobile'] = 9199176037

summ = d['one' ]+ d['two']
print(summ)

personcontact = person['name'] + str(person['mobile'])
print(personcontact)

summary = person['name'] + person['city']
print(summary)



print(person)
print(d)

d['one'] = d['one'] + 10

print(d)