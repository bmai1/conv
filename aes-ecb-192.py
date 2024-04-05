from Crypto.Cipher import AES
import base64

def pad_key(key):
    return key + ' ' * (24 - len(key))

def decrypt_aes_ecb_192(encoded_string, key):
    padded_key = pad_key(key)
    ciphertext = base64.b64decode(encoded_string)
    cipher = AES.new(padded_key.encode(), AES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)

    return decrypted_data.decode()

encoded_string = "GIx4PblHScpfcy9NXEa2cZ8heYfnnauUAwV/8Ro60+DQSJoCew41hVcsEgu43LYM"
key = "can we make a difference"

decrypted_string = decrypt_aes_ecb_192(encoded_string, key)
print("Decrypted String:", decrypted_string)