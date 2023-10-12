import hashlib

class CustomHashFunction:
    def __init__(self, data):
        self.data = data.encode('utf-8')
    
    def generate_hash(self):
        # Choose a cryptographic hash algorithm (e.g., SHA-256)
        sha256_hash = hashlib.sha256()
        sha256_hash.update(self.data)               #we use hash 256 algorithm (SHA)
        return sha256_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    input_data = "This is a sample input."

    # Create an instance of the CustomHashFunction class
    custom_hash = CustomHashFunction(input_data)

    # Generate the hash value
    hash_value = custom_hash.generate_hash()

    print(f"Input data: {input_data}")
    print(f"Hash value: {hash_value}")