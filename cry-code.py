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
print('''     
  \033[1;31m \033[97m
                          0Mo..........':ldkO0KKXXKK0kxoc,..........kMd
                          0Ml......;d0WMMMMMMMMMMMMMMMMMMMWKx:......kMd
                          0Ml...cOWMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:...kMd         
                          0Ml.lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc.kMd               
                          0MdKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0OMd
                          0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd       
                          0MxcxWMMMMMNXXNMMMMMMMMMMMMMMMNXXNMMMMMWkcKMd                                 
0                         0Md..WMKo,.,'...:kWMMMMMMMNx;...',.;dXMl.'XMd
                          0Mx'.,O;dXMMMXl....:dWMNo;....oXMMMKd;0,.'KMd
                          0MO;.,NMWMMMMMMWk;...XMK...:OWMMMMMMWMN,.cNMd
                          0MxxNMX;KMMKdcclkWN0WMMMN0WNxc:lxXMMk;WMXdKMd
                          0MMMMMO;MMl.......KMXOMNkMk.......xMM.NMMMMMd       
                          0MMMMMMXKoclddl;.oWMdkMN,MN:.:ldolcdXNMMMMMMd      
                          0MMMMMMWXMMMMMMMW0KdoNMMdox0MMMMMMMMXMMMMMMMd
                          0MMMMXc'WMMMMMMMMkcWMMMMMMkcMMMMMMMMN'lXMMMMd
                          0MMMd..cMMMMMMMMNdoKMMMMM0x:XMMMMMMMM:..kMMMd
                          0MM0....d0KKOd:.....c0Kx'.....:d0NX0l....NMMd
                          0MMO.....................................WMMd
                          0Mdkc...................................0kOMd
                          0Ml.:Ol;........';;.......;,........':oX:.kMd
                          0Ml..,WMMMMWWWo...';;:c::;'...:WWMMMMMW;..kMd
                          0Ml...dMMMMMMMMKl...........c0MMMMMMMMd...kMd
                          0Ml...cMMMMMMMMMMMXOxdddk0NMMMMMMMMMMM'...kMd
                          0Ml....KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO....kMd
                          0Ml.....OMMMMMMMMMMMMMMMMMMMMMMMMMMMK.....kMd
                          0Ml......:XMMMMMMMMMMMMMMMMMMMMMMMNl......kMd
                          0Ml........lXMMMMMMMMMMMMMMMMMMMKc........kMd
                          0Ml..........:KMMMMMMMMMMMMMMM0,..........kMd
                                \033[97
''')
time.sleep(3)
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
print('''
          _________                         _________            .___      
          \_   ___ \_______ ___.__.         \_   ___ \  ____   __| _/____  
          /    \  \/\_  __ <   |  |  ______ /    \  \/ /  _ \ / __ |/ __ \ 
          \     \____|  | \/\___  | /_____/ \     \___(  <_> ) /_/ \  ___/ 
           \______  /|__|   / ____|          \______  /\____/\____ |\___  >
                  \/        \/                      \/            \/    \/    
                                                             By : Lamani Hani ツ
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
          zaky = raw_input("\033[95m[?]\033[97m Do you want to send \033[91mKEY\033[97m to your \033[96memail\033[97m (y/n) \033[97m:")
          if zaky == ('y') : 
                   # Sending the KEY to your email ;)
                   emails = raw_input("\033[95m[?]\033[97m Type your \033[91memail Address\033[97m :\033[93m")
# For Yahoo :
                   if emails.endswith('yahoo.com') :
                            print("\033[93m[*]\033[97m Sending the \033[92mKEY\033[97m to your \033[91mYahoo \033[97maccount \033[97m:")                           
                            yahoo_user = ("crycoder1@yahoo.com") 
                            yahoo_password = ("crycoder2017")
                            sent_from = yahoo_user  
                            to = (emails)  
                            subject = 'Hello , The KEY of your encrypted File'  
                            body = ('THE KEY IS :'+(key))
                            # i love you ' L' :(
                            email_text = """\  
                            From: %s  
                            To: %s  
                            Subject: %s
                            %s
                            """ % (sent_from, ", ".join(to), subject, body)
                            try:  
                                server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
                                server.ehlo()
                                server.login(yahoo_user, yahoo_password)
                                server.sendmail(sent_from, to, email_text)
                                server.close()
                                print(" ")
                                print ("\033[97m[✔] \033[92mEmail\033[97m sent")
                            except:  
                                print (" ")
                                print ("\033[97m[✘] \033[91mSomething went wrong...\033[97m ")
                                print("Just remember the \033[91mKEY \033[97m")
# For hotmail :
                   if emails.endswith('hotmail.com') :
                            print("\033[93m[*]\033[97m Sending the \033[92mKEY\033[97m to your \033[91mHotmail \033[97maccount \033[97m:")                           
                            hotmail_user = ("crycoder1@hotmail.com") 
                            hotmail_password = ("crycoder2017")
                            sent_from = hotmail_user  
                            to = (emails)  
                            subject = 'Hello , The KEY of your encrypted File'  
                            body = ('THE KEY IS :'+(key))
                            # i love you ' L' :(
                            email_text = """\  
                            From: %s  
                            To: %s  
                            Subject: %s
                            %s
                            """ % (sent_from, ", ".join(to), subject, body)
                            try:  
                                server = smtplib.SMTP_SSL('smtp.live.com', 587)
                                server.ehlo()
                                server.login(hotmail_user, hotmail_password)
                                server.sendmail(sent_from, to, email_text)
                                server.close()
                                print(" ")
                                print ("\033[97m[✔] \033[92mEmail\033[97m sent")
                            except:  
                                print (" ")
                                print ("\033[97m[✘] \033[91mSomething went wrong...\033[97m ")
                                print("Just remember the \033[91mKEY \033[97m")
                   
# for gmail :  
                   if emails.endswith('gmail.com') :
                            print("\033[91m[✘] \033[97mgmail.com is not \033[91msupported\033[97m")
                            print("[!] The supported : Yahoo , Hotmail")
# if he dont want to send the key
          if zaky == ('n') : 
                   print("OK, just remember the key ツ")

if fodil == ('2') :
          print(" ")
          key = raw_input("\033[95m[?] \033[97mEnter the \033[91mKEY\033[97m to decode :\033[93m ")
          cipher= XOR.new(key)
          fille = input("\033[95m[?] \033[97mDrag the \033[91mfile\033[97m :\033[93m")
          filles = open(fille,"r")
          read = filles.read()
          filles.close()
          new = cipher.decrypt(base64.b64decode(read))
          os.remove(fille)
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




