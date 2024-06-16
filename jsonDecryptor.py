import json
from cryptography.fernet import Fernet

def decrypt_json(encrypted_file_path, key_file_path, output_file_path):
    # Read the encryption key
    with open(key_file_path, 'rb') as key_file:
        key = key_file.read()

    # Initialize the cipher suite
    cipher_suite = Fernet(key)

    # Read the encrypted JSON data
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Decrypt the JSON data
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()

    # Parse the JSON data
    json_data = json.loads(decrypted_data)

    # Write the decrypted data to a text file in a readable format
    with open(output_file_path, 'w') as output_file:
        json.dump(json_data, output_file, indent=4)

    print(f"Decrypted data has been saved to {output_file_path}")

# Example usage with raw strings
encrypted_file_path = r'C:\Users\UC300999\Downloads\JsonDecryptor\encrypted_data.json'
key_file_path = r'C:\Users\UC300999\Downloads\JsonDecryptor\encryption_key.key'
output_file_path = r'C:\Users\UC300999\Downloads\JsonDecryptor\decrypted_data.txt'

decrypt_json(encrypted_file_path, key_file_path, output_file_path)
