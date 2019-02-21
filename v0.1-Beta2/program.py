# -*- coding: UTF-8 -*-
import os
import login
import singin



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        choice = input("""
  ┌[ProjectX]─────────İpucu─────────[_][o][x]┐
                                             
         Çıkmak İçin 'x' Tuşuna Basınız!                    
          
  └──────────────────────────────────────────┘
┌[ProjectX]────────Hoş Geldiniz────────[_][o][x]┐

    Ne Yapmak İstiyorsunuz?                       

    1-Giriş Yap                                 
    2-Kayıt Ol                                  

└───────────────────────────────────────────────┘
[ProjectX]>>""")

        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            login.login()

        elif choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            singin.singin()

        elif choice == "x" or choice == "X":
            os.system('cls' if os.name == 'nt' else 'clear')
            quit()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("""
  ┌[ProjectX]─────────Uyarı─────────[_][o][x]┐
     
     Lütfen Seçiminizi Düzgün Girdiğinizden   
                  Emin Olunuz! 
                                
  └──────────────────────────────────────────┘""")


main()