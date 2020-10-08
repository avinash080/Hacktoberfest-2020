import math

def decrypt_cipher(row , key ,cipher_text):
    matrix_new = [ ['X']*len_key for i in range(row) ]
    key_order = [ key.index(ch) for ch in sorted(list(key))]  #to make original key order when we know keyword

    t = 0
    for c in key_order:
        for r,ch in enumerate(cipher_text[t : t+ row]):
            matrix_new[r][c] = ch
        t += row

    p_text = ''
    for r in range(row):
        for c in range(len_key):
            p_text += matrix_new[r][c] if matrix_new[r][c] != 'X' else ''
    
    return p_text
    
    
def encrypt_cipher(len_key,key,row):
    t = 0
    for r in range(row):
        for c,ch in enumerate(plain_text[t : t+ len_key]):
            matrix[r][c] = ch
        t += len_key


    sort_order = sorted([(ch,i) for i,ch in enumerate(key)])  

    cipher_text = ''
    for ch,c in sort_order:
        for r in range(row):
            cipher_text += matrix[r][c]
            
    return cipher_text
    
    
key=input("Enter keyword text (Contains unique letters only): ").lower().replace(" ", "")
plain_text = input("Enter plain text (Letters only): ").lower().replace(" ", "")
len_key = len(key)
len_plain = len(plain_text)
row = int(math.ceil(len_plain / len_key))
matrix = [ ['X']*len_key for i in range(row) ] 

encoded_text = encrypt_cipher(len_key=len_key,row=row,key=key)
print("encoded_text : " ,encoded_text)
decoded_text = decrypt_cipher(row=row , key=key , cipher_text=encoded_text)
print("decoded_text : ",decoded_text)
