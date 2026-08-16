data = "Alpha_User 101! #Beta$ & Gamma_99"
cleaned_data = ""

for character in data:
    if character.isalpha():
        cleaned_data += character
    elif character == " ":
        cleaned_data += " "
    else:
        pass

print("Task 1 - Cleaned Data:", cleaned_data)

