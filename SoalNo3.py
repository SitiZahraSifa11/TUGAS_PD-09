# No.3
# Rani memiliki sebuah list yang berisi buah-buahan. Dia ingin menghapus semua kata
# yang memiliki panjang kurang dari lima karakter dan mengurutkan sisa kata-kata tersebut 
# secara alfabetis. Bantulah Rani untuk mencapai ini.
# Input: kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
# Output: ['anggur', 'durian', 'jeruk', 'mangga', 'pisang']

kata_int = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
kata_int.sort()
kata_int.pop(1)
print("Output : ", kata_int)