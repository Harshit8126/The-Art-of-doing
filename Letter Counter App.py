#Letter Counter App
@Harshit Verma


print(" Welcome in Letter Counter App :")

#Get user Input

name = input("\n What is your name: ").title().strip()

print(" Hello, "+ name + "!")

print("Letter counter App will count no of times taht a specific letter occurs in a message.")

message = input("\n Please enter a message")

letter = input("Which letter would you like to count the occurences of: ")

#Standardize to lowercase
message = message.lower()

letter = letter.lower()

#Get the count and display
letter_count = message.count(letter)

print("\n" + name + ", Your message has " + str(letter_count) + " " + letter + " 's in it. ")
