import array as arr
# No.3
# Rani memiliki sebuah list yang berisi buah-buahan. Dia ingin menghapus semua kata
# yang memiliki panjang kurang dari lima karakter dan mengurutkan sisa kata-kata tersebut 
# secara alfabetis. Bantulah Rani untuk mencapai ini.
# Input: kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
# Output: ['anggur', 'durian', 'jeruk', 'mangga', 'pisang']

kata_int = ('u',["apel", "jeruk", "mangga", "pisang", "anggur", "durian"])
output=[]
for kata in kata_int[1]:  
    if len(kata) >= 5:
        output.append(kata)
output.sort()
print("Output : ",output)

