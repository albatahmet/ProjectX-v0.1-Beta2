# -*- coding: UTF-8 -*-
import os
import user
import login


def singin():
    while True:
        print("""
  ┌[ProjectX]─────────İpucu─────────[_][o][x]┐
                                             
      Çıkmak İçin 'x', Geri Gelmek İçin 'g'
                 Tuşuna Basınız!              
          
  └──────────────────────────────────────────┘
┌[ProjectX]──────────Kayıt Ol──────────[_][o][x]┐

    Kullanıcı Adı:
    Şifre:
    Şifre Onayı:
    İsim:

└───────────────────────────────────────────────┘""")

        username = input("[Kullanıcı Adı]>>")
        if username == "x" or username == "X":
            os.system('cls' if os.name == 'nt' else 'clear')
            quit()
        elif username == "g" or username == "G":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        password = input("[Şifre]>>")
        if password == "x" or password == "X":
            os.system('cls' if os.name == 'nt' else 'clear')
            quit()
        elif password == "g" or password == "G":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        repassword = input("[Şifre Onayı]>>")
        if repassword == "x" or repassword == "X":
            os.system('cls' if os.name == 'nt' else 'clear')
            quit()
        elif repassword == "g" or repassword == "G":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        name = input("[İsim]>>")
        if name == "x" or name == "X":
            os.system('cls' if os.name == 'nt' else 'clear')
            quit()
        elif name == "g" or name == "G":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        while True:
            if password == repassword:
                user.adduser(username, name, password)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("""
  ┌[ProjectX]─────────Uyarı─────────[_][o][x]┐
        
            Başarıyla Kayıt Oldunuz!         
      Giriş Sayfasına Yönlendiriliyorsunuz!
          
  └──────────────────────────────────────────┘""")
                login.login()
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("""
  ┌[ProjectX]─────────Uyarı─────────[_][o][x]┐
        
        Şifre Onayı Şifre İle Eşleşmiyor!     
          
  └──────────────────────────────────────────┘""")
                break