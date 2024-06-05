print('Selamat Datang di Pasar Buah!')

# Minta Input User
nApel = int(input('Masukan jumlah Apel: '))
nJeruk = int(input('Masukan jumlah Jeruk: '))
nANggur = int(input('Masukan jumlah Anggur: '))

# Definsikan harga buah
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

# Hitung total harga per buah
totalHargaApel = nApel * hargaApel
totalHargaJeruk = nJeruk * hargaJeruk
totalHargaAnggur = nANggur * hargaAnggur

# Hitung total harga belanjaan
totalBelanja = totalHargaAnggur + totalHargaApel + totalHargaJeruk

# Tampilkan rincian belanja
print(f'''
Detail Belanja

Apel: {nApel} x {hargaApel} = {totalHargaApel}
Jeruk: {nJeruk} x {hargaJeruk} = {totalHargaJeruk}
Anggur: {nANggur} x {hargaAnggur} = {totalHargaAnggur}

Total Belanja: {totalBelanja}
''')