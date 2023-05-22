import hashlib

def calculate_hash(file_path, hash_algorithm):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            if hash_algorithm == 'md5':
                hash_value = hashlib.md5(data).hexdigest()
            elif hash_algorithm == 'sha1':
                hash_value = hashlib.sha1(data).hexdigest()
            elif hash_algorithm == 'sha256':
                hash_value = hashlib.sha256(data).hexdigest()
            else:
                return None
            return hash_value
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    file_path = input("Enter the path of the file: ")
    hash_algorithm = input("Choose a hash algorithm (md5, sha1, sha256): ")

    hash_value = calculate_hash(file_path, hash_algorithm)

    if hash_value:
        print(f"{hash_algorithm.upper()} hash value: {hash_value}")
    else:
        print("File not found or invalid hash algorithm specified.")
