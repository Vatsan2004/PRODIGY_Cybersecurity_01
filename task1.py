def caesar_cipher(text, shift, direction):
    result = ""
    shift = shift % 26  # Ensure shift is within the alphabet range

    for char in text:
        if char.isalpha():
            shift_amount = shift if direction == 'encrypt' else -shift
            new_char = chr(((ord(char) - 65 + shift_amount) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 + shift_amount) % 26) + 97)
            result += new_char
        else:
            result += char

    return result

# Input from user
message = input("Enter your message: ")
shift_value = int(input("Enter the shift value: "))
action = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

# Output the result
output_message = caesar_cipher(message, shift_value, action)
print(f"Result: {output_message}")
