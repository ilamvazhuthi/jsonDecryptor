# JSON Decryptor

This Python script is designed to decrypt JSON files that have been encrypted using the Fernet symmetric encryption method provided by the `cryptography` library. It reads an encrypted file and the encryption key from specified paths, decrypts the content, and then saves the decrypted JSON data to a new file in a human-readable format.

## Requirements

- Python 3.6 or higher
- `cryptography` library

## Installation

Before running the script, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

After installing Python, you need to install the `cryptography` library. This can be done by running the following command in your terminal or command prompt:

```bash
pip install cryptography
# Usage
To use the script, you need to have an encrypted JSON file and the corresponding encryption key. The script is executed with the paths to these files as arguments.

Prepare your encrypted JSON file and encryption key. Ensure the JSON file is encrypted using Fernet encryption, and you have the key stored in a separate file.

Set the file paths in the script. Open jsonDecryptor.py and modify the encrypted_file_path, key_file_path, and output_file_path variables to point to your encrypted file, encryption key file, and desired output file path, respectively.

Run the script. Execute the script using Python:

python jsonDecryptor.py

After running, the script will decrypt the JSON data and save it to the specified output file path. A message will be printed to the console indicating the success of the operation and the location of the decrypted file.

Example
Given an encrypted file encrypted_data.json and an encryption key in encryption_key.key, you can set the paths in the script as follows:
encrypted_file_path = r'C:\path\to\encrypted_data.json'
key_file_path = r'C:\path\to\encryption_key.key'
output_file_path = r'C:\path\to\decrypted_data.json'
Running the script will decrypt the content of encrypted_data.json and save the decrypted JSON data to decrypted_data.json.

Note
This script is intended for use with JSON files encrypted using the Fernet symmetric encryption method. Ensure your encrypted data and key match this requirement.

License
This project is open-source and available under the MIT License
