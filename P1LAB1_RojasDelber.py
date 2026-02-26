#Delber Rojas 
# 2/25/2026
# The goal is to get input from the user and it displays output


#input#first name#input#last

def main():
	first_name = input('Enter your first name: ')
	last_name = input('Enter your last name: ')
	first_name = first_name.strip().title()
	last_name = last_name.strip().title()
	print(f'Hello, {first_name} {last_name}! Welcome to CTI-110')


if __name__ == '__main__':
	main()


