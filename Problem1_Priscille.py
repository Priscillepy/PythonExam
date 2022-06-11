#Here is the solution of Problem 1 Palindrome

def is_palindrome_or_not(given_string):
    if given_string[:].lower() == given_string[::-1].lower():
        return f"{given_string} is a palindrome"
    else:
        return f"{given_string} is not palindrome."


print(is_palindrome_or_not("Hannah"))

