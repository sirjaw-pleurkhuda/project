import time

import pyfiglet

banner = pyfiglet.figlet_format("bot-calculator")
print(banner)


try:
    print("halo saya adalah robot kalkulator")
    print("silahkan tunggu")
    time.sleep(8)
    print("silahkan masukan angka")

    user_input = int(input("masukan angka pertama yang ingin anda hitung: "))
    user_input_2 = int(input("masukan angka kedua yang ingin anda hitung: "))

    print("silahkan pilih opsi dibawah: ")

    print("1. tambah (+)")
    print("2. kurang (-)")
    print("3. kali (x)")
    print("4. bagi (:)")

    user_choice = input("tolong masukan pilihan (contoh: 1): ")

    if user_choice == "1":
        print(f"hasilnya adalah: {user_input} + {user_input_2} = {user_input + user_input_2}")

    elif user_choice == "2":
        print(f"hasilnya adalah: {user_input} - {user_input_2} = {user_input - user_input_2}")

    if user_choice == "3":
        print(f"hasilnya adalah: {user_input} x {user_input_2} = {user_input * user_input_2}")

    elif user_choice =="4":
        print(f"hasilnya adalah: {user_input} : {user_input_2} = {user_input / user_input_2}")

    else:
        print("error: harap masukan opsi yang sesuai")
    

except:
    print("error: tolong masukan angka saja") 