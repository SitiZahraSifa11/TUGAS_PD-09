import array as arr
# No.4
# Dewi memiliki dua list yang berisi nama-nama buah-buahan. Dia ingin menggabungkan 
# kedua list tersebut dan menghapus semua buah yang memiliki nama yang sama. Setelah itu, 
# dia ingin mengurutkan sisa buah-buahan secara alfabetis. Bantu Dewi
# Input: ["apel", "jeruk", "mangga"], ["apel", "anggur", "nanas"]
# Output: ['anggur', 'apel', 'jeruk', 'mangga', 'nanas']

data1 = ["apel", "jeruk", "mangga"]
data2 = ["apel", "anggur", "nanas"]

buah=data1.copy()
buah.extend(data2)
saring= set(buah)
buahDewi=sorted(saring)
print("Buah Dewi sekarang = ",buahDewi)
