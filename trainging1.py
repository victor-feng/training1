#!/usr/bin/env python
#_*_coding:utf-8_*_
import sys,tab

match_file = 'match.txt'
locked_file = 'locked.txt'

user_list = []
dic_user = {}


while True:
    input_user = raw_input("Please input username:")
    if len(input_user) == 0:continue
    with open(locked_file,'r') as l_f: #读出被锁的用户
        for i in l_f.readlines():
            i_user = i.strip('\n')
            user_list.append(i_user)  #将用户添加到列表中
            
        if input_user in user_list:  #判断输入的用户名在被锁的列表中
            print "Sorry the %s user is locked!" % input_user
            continue
        with open(match_file,'r') as m_f: #读出用户名和密码进行匹配
            for j in m_f.readlines():
                user,pwd = j.strip().split()
                dic_user[user] = pwd.strip('\n')      #将用户名和密码存入字典中
#            print dic_user              
            if input_user not in dic_user.keys():
                print "Sorry,the %s user is not exist!" % input_user
                continue
            else:
                for i in range(3): #循环3次
                    input_pwd = raw_input("Please input the password:")
                    if input_pwd != dic_user[input_user]: #判断输入对应用户的密码是否正确
                        j = 2-i
                        print "Sorry wrong password,you have %s times to input password!" % j
                        if i == 2: 
                            with open(locked_file,'a') as lock_f: #密码错误3次  锁账号 
                                lock_f.write(input_user)
                            sys.exit("Sorry password wrong 3 times the user is locked!")
                        continue
                    else:
                        print "Welcome %s login my system!" % input_user
                        sys.exit("Success!")
