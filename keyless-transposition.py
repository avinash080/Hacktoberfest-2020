p = input("Enter plain text: ")
rows = int(input("Enter number of rows: "))

# Method 1
row_cipher_text = ""    
row_mat = [[] for row in range(rows)]

for i in range(len(p)):
    row_mat[i % rows].append(p[i])

for a in row_mat:
    row_cipher_text += "".join(a)

row_decrypted_text = ""
i, count, col  = 0, 0, 0

while count != len(row_cipher_text):
    while col != rows:
        if count == len(row_cipher_text):
            break
        row_decrypted_text += row_mat[col][i]
        count += 1
        col += 1
    col = 0
    i += 1

print("=====================")
print("Method 1: Rail-fence Cipher")
print(row_cipher_text)
print(row_decrypted_text)

# Method 2
print("=====================")
cols = int(input("Enter number of columns: "))

col_cipher_text = ""    
col_mat = [[] for col in range(cols)]

for i in range(len(p)):
    col_mat[i % cols].append(p[i])

for a in col_mat:
    col_cipher_text += "".join(a)

col_decrypted_text = ""
i, count, row  = 0, 0, 0

while count != len(col_cipher_text):
    while row != cols:
        if count == len(col_cipher_text):
            break
        col_decrypted_text += col_mat[row][i]
        count += 1
        row += 1
    row = 0
    i += 1

print("Method 2")
print(col_cipher_text)
print(col_decrypted_text)