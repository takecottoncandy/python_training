quote = "i love python"
# word = print(quote[3])


# print (quote[2:6])  # 6 is not include  
# print(quote[2:])   # love python

# print(quote[2:10:2])

# print(quote[-1:]) 

# print(quote[:-1]) 

# # reverse string
# print(quote[::-1]) 

# name = "  Yuma"
# print(name.upper())
# print(name.lower())


# delete space
# print(name.strip())


# # Task
secret_message = "   Programming in Python is not only powerful but also fun!   "

# # Expected Output
# # "PYTHON-POWERFUL"
print(secret_message[18:24]+"-"+secret_message[37:45])

expected_message = secret_message[18:24]+"-"+secret_message[37:45]
print(expected_message.upper())



# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"

original_message = flipped_message[::-1]
original_message = original_message[0:7]+"🗡️"+ original_message[10:21] +"🌸"
print(original_message.lower())
print(f"{}")


