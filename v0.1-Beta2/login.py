# -*- coding: UTF-8 -*-
import os
import user
import greeting


def login():
    while True:
        print("""
  ┌[ProjectX]─────────İpucu─────────[_][o][x]┐
                                             
       Çıkmak İçin 'x', Bir Önceki Menüye    
         Dönmek İçin 'g' Tuşuna Basınız!      
          
  └──────────────────────────────────────────┘
┌[ProjectX]──────────Giriş Yap─────────[_][o][x]┐
    
    Kullanıcı Adı:
    Şifre:
    
└───────────────────────────────────────────────┘""")

        username = input("[Kullanıcı Adı]>>")
        if username == "x" or username == "X":
            os.system('cls' if os.name == 'nt' else 'clear')
            quit()
        elif username == "g" or username == "G":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        password = input("[Şifre]>>")

        if username == user.userlist[0] and password == user.passwordlist[0]:
            os.system('cls' if os.name == 'nt' else 'clear')
            greeting.greeting()
            break
        elif password == "x" or password == "X":
            os.system('cls' if os.name == 'nt' else 'clear')
            quit()
        elif password == "g" or password == "G":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("""
  ┌[ProjectX]─────────Uyarı─────────[_][o][x]┐
        
        Kullanıcı Adı Veya Şifre Hatalı!    
          
  └──────────────────────────────────────────┘""")

