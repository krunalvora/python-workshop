cars = ['hyundai', 'nissan', 'tesla', 'chevy', 'honda']

for car in cars:
    print(car)

for value in range(1, 5):    # starting from 1 not including 5
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))      # third arg is step
print(even_numbers)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)

# Slicing
print(cars[1:2])          # 2nd index not included
print(cars[:2])
print(cars[2:])
print(cars[-3:])          # print last 3


# copying a list
cars_copy_1 = cars[:]
print(cars.copy())
