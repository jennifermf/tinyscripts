# compare two strings
print('------------------------\nIt looks like you want to compare two strings. I can help!\n')
case = input('Would you like me to ignore case (A = a, B = b, etc)? [Y] for yes or any key for no: ')
if case.lower() == 'y':
	string1 = input('First string: ').lower()
	string2 = input('Second string: ').lower()
else: 
	string1 = input('First string: ')
	string2 = input('Second string: ')
if string1 == string2: print('\n*TRUE!* These strings are identical.')
else: print('\n*FALSE!* These strings are different.')
print('\n------------------------\n')
