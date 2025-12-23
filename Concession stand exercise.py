# The program's data:

menu = {'pizza': 3.00, 
        'nachos': 6.99, 
        'ice cream': 10.99, 
        'popcorn': 5.50, 
        'fries': 6.75, 
        'soda': 3.75, 
        'chips': 6.25}

cart = []
total = 0

# Display of the menu. The user must enter an item from the menu to add in the cart. The script 
# prints the contents of the cart.

print('###################' + '\n' '   |Cinema Menu|' + '\n' + '###################' + '\n')

for key, value in menu.items():
	print(f'{key:10}: ${value:.2f}')

print('-------------------')

while True:
	food = input('Select an item to buy (q to quit): ').lower()
	
	if food == 'q':
		break
	elif food not in menu:
		print('Your choice doesn\'t exist in the menu!')
	else:
		print(f'You added 1 x {food} to your cart')
		cart.append(food)

	def cart_contents():
		print('Your cart contains: ', end='')
		for food in cart:
			if food is not cart[-1]:
				print(f'{food}', end=', ')
			else:
				print(f'{food}', end='')
		print('\n')

	cart_contents()

# At the end, the total price is calculated and displayed and the user can choose to buy the 
# selected items or not.

for food in cart:
	total += menu.get(food)

print('\n' + '------Your total------' + '\n')
cart_contents()
print(f'Your total is: ${total:.2f}')

while True:
	decision = input('Buy? (y/n):').lower()
	if decision == 'y':
		print('Thank you for your purchase! <3')
		break
	elif decision != 'n':
		print('Invalid answer')