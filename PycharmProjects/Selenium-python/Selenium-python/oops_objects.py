#demo of object oriented programming

s = "this is my first program"
s.upper()
print(type(s))

class Car(object):
           #creating default init method
    wheels = 4
    def __init__(self,make,model,price,condition):
        self.make = make
        self.model = model
        self.price = price
        self.condition = condition
            #creating our own method out of the above
    def info(self):
        print('car make', self.make)
        print('car model',self.model)

    def car_details(self):
        print('the car price is',self.price)
        print('the car condition is',self.condition)

print(Car.wheels)
c1 = Car('bmw','550i',55000,'good')
c2 = Car('benz','ml250',55000,'ok')
c1.info()
c2.info()

print(c1.make)
print(c2.model)
print(c1.price)
print(c2.condition)

c1.car_details()
c2.car_details()

print(c1.wheels)

c1.wheels = 10
print(c1.wheels)
print(c2.wheels)


