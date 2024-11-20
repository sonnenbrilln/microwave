'''
Program Microwave
Mini Project mata kuliah Pengenalan Komputasi ITB tahun ajaran 2024/2025

Kelompok 10 K-05

Nama				NIM
Nafilah Adinata 		16024364
Nadha Aulia Ramadhani		16024380
Khalifa Prasetya Al Kautsar	16024394
Fathir Hasya Adrian		16024410
Talitha Siti Salsabila		16024426
Muhammad Hilmiy			16024455 



Kamus

selesai	: char, agar while loop berjalan, selama selesai != 'y', program akan terus berjalan
mode	: char, mode yang diinput user
temp	: int, temperatur yang diinput user
timer	: int, waktu yang diinput user
'''

import time

selesai = ''

while selesai != 'y':
	
	# Menerima user input untuk mengetahui mode yang dibutuhkan user
	mode = input("Pilih Mode [Manual (m) / Cook (c) / Steam (s) / Defrost (d) / Reheat (r)]: ")

	# Apabila user memilih mode manual, program akan meminta user memasukkan temperatur dan waktu memasak secara manual
	if mode == 'm':
		temp = input("Masukkan temperatur: ")
		timer = int(input("Masukkan waktu (dalam detik): "))
		print("Anda memasak selama ", timer, " detik dengan suhu ", temp, " celcius. Tekan Ctrl + C untuk mematikan microwave.")
		
		# Hitung mundur
		for x in range(timer, 0, -1):
			seconds = x % 60
			minutes = int(x / 60) % 60
			hours = int(x / 3600)
			print(f"{hours:02}:{minutes:02}:{seconds:02}")
			time.sleep(1)

	# Apabila user memilih mode cook, preset yang digunakan adalah temp = 160 ; timer = 15
	elif mode == 'c':
		temp = 160
		timer = 15
		print("Anda memasak selama ", timer, " detik dengan suhu ", temp, " celcius. Tekan Ctrl + C untuk mematikan microwave.")
		
		# Hitung mundur
		for x in range(timer, 0, -1):
			seconds = x % 60
			minutes = int(x / 60) % 60
			hours = int(x / 3600)
			print(f"{hours:02}:{minutes:02}:{seconds:02}")
			time.sleep(1)

	# Apabila user memilih mode steam, preset yang digunakan adalah temp = 100 ; timer = 15
	elif mode == 's':
		temp = 100
		timer = 15
		print("Anda memasak selama ", timer, " detik dengan suhu ", temp, " celcius. Tekan Ctrl + C untuk mematikan microwave.")
		
		# Hitung mundur
		for x in range(timer, 0, -1):
			seconds = x % 60
			minutes = int(x / 60) % 60
			hours = int(x / 3600)
			print(f"{hours:02}:{minutes:02}:{seconds:02}")
			time.sleep(1)

	# Apabila user memilih mode defrost, preset yang digunakan adalah temp = 40 ; timer = 10
	elif mode == 'd':
		temp = 40
		timer = 10
		print("Anda memasak selama ", timer, " detik dengan suhu ", temp, " celcius. Tekan Ctrl + C untuk mematikan microwave.")
		
		# Hitung mundur
		for x in range(timer, 0, -1):
			seconds = x % 60
			minutes = int(x / 60) % 60
			hours = int(x / 3600)
			print(f"{hours:02}:{minutes:02}:{seconds:02}")
			time.sleep(1)

	# Apabila user memilih mode reheat, preset yang digunakan adalah temp = 60 ; timer = 5
	elif mode == 'r':
		temp = 60
		timer = 5
		print("Anda memasak selama ", timer, " detik dengan suhu ", temp, " celcius. Tekan Ctrl + C untuk mematikan microwave.")
		
		# Hitung mundur
		for x in range(timer, 0, -1):
			seconds = x % 60
			minutes = int(x / 60) % 60
			hours = int(x / 3600)
			print(f"{hours:02}:{minutes:02}:{seconds:02}")
			time.sleep(1)
	
	# Apabila user menekan tombol lain, akan dipilih mode manual
	else : # manual
		temp = input("Masukkan temperatur: ")
		timer = int(input("Masukkan waktu (dalam detik): "))
		print("Anda memasak selama ", timer, " detik dengan suhu ", temp, " celcius. Tekan Ctrl + C untuk mematikan microwave.")
		
		# Hitung mundur
		for x in range(timer, 0, -1):
			seconds = x % 60
			minutes = int(x / 60) % 60
			hours = int(x / 3600)
			print(f"{hours:02}:{minutes:02}:{seconds:02}")
			time.sleep(1)
	
	# Menanyakan apakah user masih mau memasak atau mematikan microwave, jika masih mau memasak, program tidak akan keluar dari loop sehingga mengulang prosesnya.
	selesai = input("Makanan sudah matang! Matikan microwave? [Ya (y) / Tidak (tombol lain)]: ")
