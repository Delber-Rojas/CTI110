def main():
	first_name = input('Enter your first name: ')
	last_name = input('Enter your last name: ')
	# Normalize capitalization and remove surrounding whitespace
	first_name = first_name.strip().title()
	last_name = last_name.strip().title()
	print(f'Hello, {first_name} {last_name}! Welcome to CTI-110')


if __name__ == '__main__':
	main()

