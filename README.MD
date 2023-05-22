# File Hash Calculator Documentation

## Introduction
The File Hash Calculator is a Python program that allows users to calculate the hash value of a file using various hash algorithms, such as MD5, SHA-1, or SHA-256. The program helps to ensure file integrity and detect any modifications or tampering that might have occurred.

## Usage
1. Ensure that Python is installed on your system.
2. Run the program using a Python interpreter.
3. Follow the prompts to enter the path of the file and choose a hash algorithm.
4. The program will calculate the hash value of the file using the selected algorithm and display it on the screen.

## Requirements
- Python 3.x

## Functionality
1. User Input:
   - The program prompts the user to enter the path of the file they want to calculate the hash value for.
   - The user is also asked to choose a hash algorithm from the available options: MD5, SHA-1, or SHA-256.

2. Hash Calculation:
   - The program reads the contents of the file in binary mode.
   - Based on the selected hash algorithm, it calculates the hash value of the file using the corresponding cryptographic function.

3. Hash Display:
   - The program displays the calculated hash value on the screen, along with the chosen hash algorithm.

4. Error Handling:
   - If the specified file path is not found, or if an invalid hash algorithm is chosen, an appropriate error message is displayed.

## Example Usage
```
python file_hash_calculator.py
```
Enter the path of the file: /path/to/file.txt

Choose a hash algorithm (md5, sha1, sha256): sha256

SHA256 hash value: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z

## Notes
- The program utilizes the hashlib module in Python for performing hash calculations.
- Users can compare the calculated hash value with known hash values to verify file integrity or detect any modifications.

---

Please note that this documentation serves as a guide for using the "file_hash_calculator.py" program and can be customized or expanded upon based on your specific needs.

