first_letter= 'a'
last_letter = input("Please, enter a character to create your pyramid: ")

def pyramid():
    for middle_letter in range(ord(first_letter), ord(last_letter)+1):
        space =(ord(last_letter)+1-middle_letter)
        print(' '*space, end='')
        for letter in range(ord(first_letter), (middle_letter)+1):
            print(chr(letter), end='')
        for letter in reversed(range(ord(first_letter), (middle_letter))):
            print(chr(letter), end='')
        print('')
        middle_letter += 1

pyramid()
