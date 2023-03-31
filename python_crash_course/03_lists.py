cars = ['hyundai', 'nissan', 'tesla', 'chevy']
print(cars[2])
print(cars[-1])
print(type(cars))
print(type(cars[0]))

random = ['a', 1, 2, 'b']
print(type(random))
print(type(random[1]))

cars.append('honda')
cars.insert(0, 'mercedes')

print(cars)

# Removing from list
del cars[0]

print(cars)

popped_car = cars.pop() # removes the last item
print(popped_car)

popped_car = cars.pop(2)
print(popped_car)

cars.remove('chevy') # removes first occurrence
print(cars)

# Permanent sorting
cars.sort(reverse=True)
print(cars)

# Temporary sorting
print(sorted(cars))

cars.reverse()

print(len(cars))
