from encryption import encrypt_data,generate_key, decrypt_data

key = generate_key()

message = "This is a simple message"

encrypted_message = encrypt_data(message,key)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt_data(encrypted_message,key)
print("Decrypted Message:", decrypted_message)