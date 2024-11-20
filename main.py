# Microwave

import time

tambah = ''

while tambah != 'y':
	
	mode = input("Pilih Mode [Manual (m) / Cook (c) / Steam (s) / Defrost (d) / Reheat (r)]: ")

	if mode == 'm':
		temp = input("Masukkan temperatur: ")
		timer = int(input("Masukkan waktu (dalam detik): "))
		print("Anda memasak selama ", timer, " detik dengan suhu ", temp, " celcius. Tekan Ctrl + C untuk mematikan microwave.")
		for x in range(timer, 0, -1):
                        seconds = x % 60
                        minutes = int(x / 60) % 60
                        hours = int(x / 3600)
                        print(f"{hours:02}:{minutes:02}:{seconds:02}")
                        time.sleep(1)

	elif mode == 'c':
		temp = 160
		timer = 15
		print("Anda memasak selama ", timer, " detik dengan suhu ", temp, " celcius. Tekan Ctrl + C untuk mematikan microwave.")
		for x in range(timer, 0, -1):
                        seconds = x % 60
                        minutes = int(x / 60) % 60
                        hours = int(x / 3600)
                        print(f"{hours:02}:{minutes:02}:{seconds:02}")
                        time.sleep(1)
	elif mode == 's':
		temp = 100
		timer = 15
		print("Anda memasak selama ", timer, " detik dengan suhu ", temp, " celcius. Tekan Ctrl + C untuk mematikan microwave.")
		for x in range(timer, 0, -1):
                        seconds = x % 60
                        minutes = int(x / 60) % 60
                        hours = int(x / 3600)
                        print(f"{hours:02}:{minutes:02}:{seconds:02}")
                        time.sleep(1)

	elif mode == 'd':
		temp = 40
		timer = 10
		print("Anda memasak selama ", timer, " detik dengan suhu ", temp, " celcius. Tekan Ctrl + C untuk mematikan microwave.")
		for x in range(timer, 0, -1):
                        seconds = x % 60
                        minutes = int(x / 60) % 60
                        hours = int(x / 3600)
                        print(f"{hours:02}:{minutes:02}:{seconds:02}")
                        time.sleep(1)

	elif mode == 'r':
		temp = 60
		timer = 5
		print("Anda memasak selama ", timer, " detik dengan suhu ", temp, " celcius. Tekan Ctrl + C untuk mematikan microwave.")
		for x in range(timer, 0, -1):
                        seconds = x % 60
                        minutes = int(x / 60) % 60
                        hours = int(x / 3600)
                        print(f"{hours:02}:{minutes:02}:{seconds:02}")
                        time.sleep(1)

	else: # manual
		temp = input("Masukkan temperatur: ")
		timer = int(input("Masukkan waktu (dalam detik): "))
		print("Anda memasak selama ", timer, " detik dengan suhu ", temp, " celcius. Tekan Ctrl + C untuk mematikan microwave.")
		for x in range(timer, 0, -1):
                        seconds = x % 60
                        minutes = int(x / 60) % 60
                        hours = int(x / 3600)
                        print(f"{hours:02}:{minutes:02}:{seconds:02}")
                        time.sleep(1)

	tambah = input("Makanan sudah matang! Matikan microwave? [Ya (y) / Tidak (tombol lain)]: ")
