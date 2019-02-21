# -*- coding: UTF-8 -*-


def adduser(username, name, password):
    a = 0
    userlist[:] = [username]
    namelist[:] = [name]
    passwordlist[:] = [password]


def usercheck(username,name):
    print(userlist)
    print(username and name in userlist)

userlist = ["deneme"]
namelist = ["deneme"]
passwordlist = ["deneme"]