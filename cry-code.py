## -*- coding: utf-8 -*-
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Date: Decembre 20, 2017 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%% Weather: It's always cool in the lab %%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%% Health: Overweight %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%% Caffeine: 12975 mg %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%% Hacked: All the things %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# By :     Lamani Fodil Hani (VEGETA-LFH)      &        Hirokazo Nagata
# Fb : Lamani Fodil Hani              &           Hirokazo Nagata
# Github : www.github.com/lamanihani      &      www.github.com/
# Gmail :   lamanihani1@gmail.com        &    ziadabouelfarah2@gmail.com
#                           
from Crypto.Cipher import XOR
import base64
import os
import smtplib
import random
import time
os.system('clear')
print("\033[94m[✘] \033[97minstalling the \033[91mpackage \033[97m, Please wait :")
os.system('pip install pycryptodome')
print(" ")
print('\033[94m[✔]\033[92m Start :') 
time.sleep(3)
os.system('clear')
os.system('clear')
rania1 = ("            #do you even \033[91mexist\033[97m ")
rania2 = ('''          #Im \033[92mgood\033[97m at reading \033[93mpeople
          \033[97mMy \033[91msecret\033[97m ? I look for the \033[96mworst\033[97m in them\033[97m''')
rania3 = ("            #'\033[91mlove \033[97mis foreever' \033[97mbullshit\033[97m")
rania4 = ("            #we live in a kingdom of \033[91mbullshit\033[97m")
rania5 = ("            #LEAVE ME \033[91mHERE \033[97m!")
rania6 = ("            #LEAVE ME \033[91mHERE \033[97m!")
def kf_art():
    arts = [rania1, rania2, rania3,rania4,rania5,rania6]
    return random.choice(arts)
os.system('clear')
print('''\033[1;31m \033[97m
          _________                         _________            .___      
          \_   ___ \_______ ___.__.         \_   ___ \  ____   __| _/____  
          /    \  \/\_  __ <   |  |  ______ /    \  \/ /  _ \ / __ |/ __ \ 
          \     \____|  | \/\___  | /_____/ \     \___(  <_> ) /_/ \  ___/ 
           \______  /|__|   / ____|          \______  /\____/\____ |\___  >
                  \/        \/                      \/            \/    \/    
                                                             By : \033[93mLamani Hani\033[97m ツ
''')
print(kf_art())
print(" ")
print("\033[95m1- \033[91mEncryption\033[97m")
print("\033[95m2- \033[92mDecode\033[97m")
print(" ")
fodil = raw_input("\033[93m+>>")
if fodil == ('1') :
          print(" ")
          key = raw_input("\033[95m[?] \033[97mEnter your \033[97m\033[91mKEY \033[97m:\033[93m")
          cipher= XOR.new(key)
          fille = input("\033[95m[?] \033[97mDrag the \033[91mfile\033[97m:\033[93m")
          filles = open(fille,"r")
          read = filles.read()
          filles.close()
          new = base64.b64encode(cipher.encrypt(read))
          os.remove(fille)
          lylia = open(fille,"w")
          lylia.write(new)
          filles.close()
          print("\033[97m[✔] The file has been encrypted ツ")
          print(" ")
          
if fodil == ('2') :
          print(" ")
          key = raw_input("\033[95m[?] \033[97mEnter the \033[91mKEY\033[97m to decode :\033[93m ")
          cipher= XOR.new(key)
          fille = input("\033[95m[?] \033[97mDrag the \033[91mfile\033[97m :\033[93m")
          filles = open(fille,"r")
          read = filles.read()
          filles.close()
          new = cipher.decrypt(base64.b64decode(read))
          #os.remove(fille)
          os.system('mkdir original-file')
          os.system('mv '+(fille)+' original-file')
          lylia = open(fille,"w")
          lylia.write(new)
          filles.close()
          print("\033[97m[✔] The file has been decrypted ツ")

if fodil == ('Decode') :
          print(" [✘] This is not metasploit, type a number (1 / 2)")
if fodil == ('Encryption') : 
          print(" [✘] This is not metasploit , type a number (1 / 2)")
if fodil == ('help') :
          print(" ツ  watch the tuturial : ")




