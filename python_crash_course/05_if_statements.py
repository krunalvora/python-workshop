cars = ['hyundai', 'nissan', 'tesla', 'chevy', 'honda']

for car in cars:
    if car == 'honda':
        print(car.upper())
    else:
        print(car.lower())

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'jalapeno' in requested_toppings:
    print('yay!')
elif 'pineapple' not in requested_toppings:
    print('thank god!')
else:
    print('just eat!')

if requested_toppings:
    print('toppings are requested...')
    