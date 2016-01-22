#!/usr/bin/env python
#_*_coding:utf-8_*_
import json
import tab

def addinfo():
    backend = raw_input("backend:")
    context = "backend %s" % (backend)
    server = raw_input("server:")
    weight = raw_input("weight:")
    maxconn = raw_input("maxconn:")
    record = "        server %s weight %s maxconn %s\n" % (server,weight,maxconn)    
    with open('ha.py','r+') as f:
        add_f = f.readlines()
        for i in add_f:
            if 'backend test.oldboy.org' in i:
                add_index = add_f.index(i)
               
        add_f.insert(add_index+1,record)
    with open('ha','w') as f1:
        for item in add_f:
            f1.write(item)

def delinfo():
    with open('ha.py','r+') as f:
        add_f = f.readlines()
        for j in add_f:
            if 'server' in j:
                del j
    with open('ha','w') as f:
        for j in add_f:
            f.write(j)   
    f.close()

def menu():
    print '''
        1. add info
        2. del info
        3. exit
        4. return main menu'''
menu()
while True:
    choice = raw_input("Please choice the number:")
    if len(choice) == 0:continue
    elif int(choice) > 4:
        print "\033[31;1mSoory input wrong!\033[0m"
        continue
    elif choice == '3':
        exit()
    elif choice == '4':
        menu()
    elif choice == '1':
        addinfo()
        break
    else:
        delinfo()
        break



