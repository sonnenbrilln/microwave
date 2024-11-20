# Microwave

import time

tambah = 'y'

while tambah == 'y':
	mode = input("Pilih Mode [Manual (m) / Cook (c) / Steam (s) / Defrost (d) / Reheat (r)]: ")

	if mode == 'm':
		temp = input("Masukkan temperatur: ")
		timer = int(input("Masukkan waktu (dalam detik): "))
		print("Anda memasak selama ", timer, " detik dengan suhu ", temp, " celcius. Tekan Ctrl + C untuk mematikan microwave.")

		for x in range(timer, 0, -1):
			print(x)
			time.sleep(1)

	elif mode == 'c':
		print("Anda memasak selama 100 detik dengan suhu 160 celcius. Tekan Ctrl + C untuk mematikan microwave.")
		for x in range(120, 0, -1):
			print(x)
			time.sleep(1)

	elif mode == 's':
		print("Anda memasak selama 60 detik dengan suhu 100 celcius. Tekan Ctrl + C untuk mematikan microwave.")
		for x in range(60, 0, -1):
			print(x)
			time.sleep(1)

	elif mode == 'd':
		print("Anda memasak selama 100 detik dengan suhu 60 celcius. Tekan Ctrl + C untuk mematikan microwave.")
		for x in range(100, 0, -1):
			print(x)
			time.sleep(1)

	elif mode == 'r':
		print("Anda memasak selama 40 detik dengan suhu 40 celcius. Tekan Ctrl + C untuk mematikan microwave.")
		for x in range(40, 0, -1):
			print(x)
			time.sleep(1)

	print("Makanan sudah matang!")

	tambah = input("Makanan sudah matang! Apakah anda mau menambah waktu? [Ya (y)])")