import base64

def encode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string    
    
def decode(key, string):
    decoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        decoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        decoded_chars.append(decoded_c)
    decoded_string = ''.join(decoded_chars)
    return decoded_string

    

def encode64(key, string):
    encoded_chars = []
    for i in xrange(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string)
    
def decode64(key, string):
    string=base64.urlsafe_b64decode(string)
    decoded_chars = []
    for i in xrange(len(string)):
        key_c = key[i % len(key)]
        decoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        decoded_chars.append(decoded_c)
    decoded_string = "".join(decoded_chars)  
    return (decoded_string)


# Start
message="Privet"
key="enckey"

# Simple
print("original:")    
print(message)    
encoded=encode(key, message)
print("encoded: " + ''.join([encoded]))
print([encoded]);
decoded=decode(key, encoded)
print("decoded: " + decoded)


# 64 Encode
print("\n\nUrlsafe")    
encoded=encode64(key, message)
print("encoded: " + encoded)
decoded=decode64(key, encoded)
print("decoded: " + decoded)

