#Nama   : Juventia Adelia Putri
#NIM    : 2209116032
#Kelas  : A Sistem Informasi 2022
#Matkul : Algoritma dan Struktur Data

import os
os.system ("cls")

class Node:
    def __init__(self,akun,pencarian,history):
        self.akun = akun
        self.pencarian = pencarian
        self.history = history
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None :
            print("Riwayat Kosong")
        else:
            y = self.head
            while y is not None :
                print(f"{y.akun} {y.pencarian} {y.history}")

                y= y.next

    def addfirst(self):
        akun= (input("Masukkan akun anda: "))
        pencarian = (input("Masukkan video yang ingin anda cari: "))
        history = (input("Masukkan history video yang ingin anda cari: "))
        data_baru2 = Node(akun,pencarian,history)
        if self.head is None:
            self.head = data_baru2
        else:
            data_baru2.next = self.head
            self.head = data_baru2
        print("berhasil ditambahkan.")

    def delete (self):
        akun = (input("masukkan akun youtube anda: "))
        if self.head is None:
            print("Tidak ada History.")
        elif self.head.akun == akun:
            self.head = self.head.next
            print("History berhasil dihapus.")
        else:
            current = self.head
            while current.next is not None:
                if current.next.akun == akun:
                    current.next = current.next.next
                    print("History berhasil dihapus.")
                    return
                current = current.next
            print("History tidak ditemukan.")

    def start(self):
        while True:
            os.system("cls")
            print(" History Tontonan Youtube ".center(40))
            print ()
            print(" Menu: ")
            print("1. Lihat History")
            print("2. Tambah History")
            print("3. Hapus History")
            print("4. Keluar")
            pilihan = int(input("Masukkan pilihan: "))
            print ()
            if pilihan == 1:
                print (" History yang Tersedia ".center(20))
                print ()
                self.display()
                input ("*****".center(20))
            elif pilihan == 2:
                print (" Tambah History baru ".center(20))
                print ()
                self.addfirst()
                input ("=================================")
            elif pilihan == 3:
                print (" Hapus History yang tersedia ".center(20))
                print ()
                self.delete()
                input ("=================================")
            elif pilihan == 4:
                break
            else:
                print("Pilihan tidak valid.")

adel = LinkedList()
adel.start()