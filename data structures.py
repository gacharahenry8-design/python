# lists
fruits = ['apple','banana','mango']
print(fruits)
print(fruits[2])
fruits[0] = 'Orange'
print(fruits)
# tuples
Students = ('John','Smith','David')
print(Students)
print(Students[0])
# sets
cars = {'audi','bmw','toyota','lambo'}
cars.add('subaru')
print(cars)
if 'bmw' in cars:
    print('bmw')
if 'chevrolet' in cars:
    print('toyota')
else:
    print('Not found')
# Dictionary
Patient = {'name':'john',
           'age':21,
           'gender':'male'
           }
print(Patient)
if 'gender' in Patient:
    print(Patient['gender'])
else:
    print('Not found')
Patient['NoK']= 'Njoro'
print(Patient)

