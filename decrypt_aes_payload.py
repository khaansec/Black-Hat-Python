import base64
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# AES configuration from the PowerShell snippet
KEY_B64 = 'QUVTLUtleQ=='
IV_B64 = 'QUVTLUlW'

def decrypt_aes_cbc_base64(encrypted_b64, key, iv):
    encrypted_data = base64.b64decode(encrypted_b64)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted.decode('utf-8', errors='ignore')

def main():
    if len(sys.argv) < 2:
        print("Usage: python decrypt_payload.py <path_to_file>")
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            encrypted_b64 = file.read().strip()
        
        key = base64.b64decode(KEY_B64)
        iv = base64.b64decode(IV_B64)

        decrypted_text = decrypt_aes_cbc_base64(encrypted_b64, key, iv)
        print("Decrypted content:")
        print(decrypted_text)

    except Exception as e:
        print(f"Decryption failed: {e}")

if __name__ == "__main__":
    main()

