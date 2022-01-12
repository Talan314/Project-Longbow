#!/usr/bin/env python3
### IMPORT STATEMENTS ###
import subprocess
import sys
import os
import platform

                      ### Linux Systems ###

def install_update():
  ## Updates and/or installs Apache2
  print('This may take some time')
  os.system('apt upgrade && apt-get install Apache2')

def apache_conf():
  os.chdir('/etc/apache2')
  file = open('apache2.conf', 'r')
  data = ''
  ## Creates a copy of the file assigned to data
  for line in file:
    data = data + line
  #print(data)
  backup = data
  ## Makes the nessesairy changes to the data variable
  data = data.replace('Options FollowSymLinks', 'Options None', 1)
  data = data.replace('AllowOverride None', 'Order allow,deny' , 1)
  data = data.replace('Require all denied', 'Allow from all', 1 )
  
  #print(data)

  file.close()
  ## Creates a backup file of defualt configurations
  os.system('touch apache2.conf.backup')
  file = open('apache2.conf.backup', 'w')
  file.write(backup)
  file.close()
  ## Opens the file in Write mode and writes the new data to it
  file = open('apache2.conf', 'w')
  file.write(data)
  file.close()

def apache_rec():
  os.chdir('/etc/apache2')
  file = open('apache2.conf', 'r')
  data = ''
  ## Creates a copy of the file assigned to data
  for line in file:
    data = data + line
  #print(data)
  ## Makes the nessesairy changes to the data variable
  data = data.replace('Options FollowSymLinks', 'Options None', 1)
  data = data.replace('AllowOverride None', 'Order allow,deny' , 1)
  data = data.replace('Require all denied', 'Allow from all', 1 )
  
  #print(data)

  file.close()
  ##Creates a new file and writes the data to it 
  os.system('touch apache2.conf.recomended')
  file = open('apache2.conf.recomended', 'w')
  file.write(data)
  file.close()
  


def sec_conf():
  os.chdir('/etc/apache2/conf-enabled')
  os.system('a2enmod headers')
  file = open("security.conf", 'r')
  data=file.read()
  backup = data
  #print(data)
  ## Replaces incorrect settings with secure ones
  data = data.replace('ServerTokens OS','ServerTokens Prod')
  data = data.replace('#ServerSignature Off', 'ServerSignature Off')
  data = data.replace('ServerSignature On', '#ServerSignature On')
  data = data.replace('#Header set X-Frame-Options: "sameorigin"', 'Header set X-Frame-Options: "sameorigin"')
  data = data + '\n\n# The following lines protect the server form XXS attacks\nHeader always set X-XSS-Protection "1;  mode=block"'
  #print(data)
  file.close()
  ## Creates a backup file of of default configurations
  os.system('touch security.conf.backup')
  file = open('security.conf.backup', 'w')
  file.write(backup)
  file.close()
  ## Opens the file in Write mode and writes the new data to it
  file = open('security.conf', 'w')
  file.write(data)
  file.close()



def sec_rec():
  os.chdir('/etc/apache2/conf-enabled')
  file = open("security.conf", 'r')
  data=file.read()
  #print(data)
  ## Replaces incorrect settings with secure ones
  data = data.replace('ServerTokens OS','ServerTokens Prod')
  data = data.replace('#ServerSignature Off', 'ServerSignature Off')
  data = data.replace('ServerSignature On', '#ServerSignature On')
  data = data + '\n\n# The following lines protect the server form XXS attacks\nHeader always set X-XSS-Protection "1;  mode=block"\n Make sure to use "sudo a2enmod headers" to enable the module.'
  data = data.replace('#Header set X-Frame-Options: "sameorigin"', 'Header set X-Frame-Options: "sameorigin"')
  data = data.replace('#Header set X-Content-Type-Options: "nosniff"', 'Header set X-Content-Type-Options: "nosniff"')
  #print(data)
  file.close() 
  ##Creates a new file and writes the data to it 
  os.system('touch security.conf.recomended')
  file = open('security.conf.recomended','w')
  file.write(data)
  file.close

def apache_restart():
  ## Restarts the system to allow changes to take place

  
  os.system('systemctl restart apache2')





                       ### Windows Systems ###

def httpd_conf():
  # going to the location of the configuration files in a windows machine 
  os.chdir("C:\Apache24\conf")
  # this is a list of the commands i want to add to the main configuration file
  new_text = [' ','ServerSignature Off' ,'ServerTokens Prod',"Header always set X-XSS-Protection '1;  mode=block'"]
  
  # im openning the configuration file 
  with open("httpd.conf", 'a') as f:
    f.write("\nServerSignature Off\nServerTokens Prod\n<IfModule mod_headers.c>\n Header set X-XSS-Protection '1; mode=block'\n</IfModule>")
  
def default_conf():
  os.chdir("C:\Apache24\conf\extra")
  file = open("httpd-default.conf","r")
  replacement = ""
  
  for line in file:
    line = line.strip()
    changes = line.replace("ServerTokens Full", "ServerTokens Prod").replace("KeepAliveTimeout 5","KeepAliveTimeout 1")
    replacement += changes + "\n"
  
  file.close()
  fout = open("httpd-default.conf", "w")
  fout.write(replacement)
  fout.close    


# this is a command to install a working executable version of the apache http service
def install():
  os.chdir("C:\Apache24\\bin")
  
  print("Reminder:Make sure to fix the Errors that are reported ")

  os.system('httpd -k install')
  

# its a good thing to restart the server when making changes so that they can be implemanted properly
def apache_rst(): 
  os.chdir('c:\Apache24\\bin')
  os.system("httpd -k restart")
      
def apache_version():
  os.chdir("C:\Apache24\\bin")
  apache_v = os.system('httpd -v')
  print(apache_v)



            ###Legacy Versions###

def A2_conf():
  os.chdir("C:\Apache2\conf")
  file = open("httpd.conf","r")
  replacement = ""
  for line in file:
    line = line.strip()
    changes = line.replace("#LoadModule info_module modules/mod_info.so", "#LoadModule info_module modules/mod_info.so")
    replacement += changes + "\n"
  file.close()
  fout = open("httpd.conf", "w")
  fout.write(replacement)
  fout.close   

def A2_default_conf():
  os.chdir("C:\Apache2\conf\extra")
  file = open("httpd-default.conf","r")
  replacement = ""
  for line in file:
    line = line.strip()
    changes = line.replace("ServerTokens Full", "ServerTokens Prod").replace("ServerSignature On","ServerSignature off")
    replacement += changes + "\n"
  file.close()
  fout = open("httpd-default.conf", "w")
  fout.write(replacement)
  fout.close   



### MAIN FUNCTION ###
def main():
  ##Checks for OS type 
  system = platform.system()
  
  ## Using system information and user input directs the script to the correct functions
  if system == 'Linux':

    #print('You are currently running')

    version = subprocess.run(['apache2', '-v'], stdout=subprocess.PIPE)
    
    version = version.stdout.decode('utf-8')
    print('You are currently running\n'+version)
    

    place = version.find(':')
    version = version[place +2:]
    place = version.find('4')
    version = version[:place + 1]
    #print(version)
     
    print('Would you like to install or updata Apache2 to the latest version? WARNING doing this may break some applications dependent on your current version [Y,n]')
    
    answer_update = input()
    if answer_update == 'y' or answer_update == 'Y':
      answer_update = 'y'
    elif answer_update == 'n' or answer_update == 'N':
      answer_update = 'n'
    else:
      print('Please enter a valid responce')
    
    if answer_update == 'y':
      install_update()

    
    ## Asks if changes would like to be made or recomendations only
    
    print('Would you like this script to make changes? If no it will create files that contain recomended changes. [Y/n]')
    answer = input()
    
    if answer == 'y' or answer == 'Y':
      answer = 'y'
    elif answer == 'n' or answer == 'N':
      answer = 'n'
    else:
      print('Please enter a valid responce')


    if answer == 'y' and version == 'Apache/2.4':
      apache_conf()
  
      sec_conf()

      apache_restart()

      print('Apache2 has been restarted')
    elif answer == 'n' and version == 'Apache/2.4':
      sec_rec()

      apache_rec()

      print('Copies of the recomended files have been placed in their respective conf directories')
    elif answer == 'y' and version != 'Apache/2.4':
        A2_conf()
        A2_default_conf()
        apache_restart()

      
  elif system == 'Windows':
    
    version = subprocess.run(['\Apache24\\bin\httpd', '-v'],shell=True, stdout=subprocess.PIPE)
    version = version.stdout.decode('utf-8')
    print('Hello you are running apache version:\n'+version)

    place = version.find(':')
    version = version[place +2:]
    place = version.find('4')
    version = version[:place + 1]
  
    if version == "Apache/2.4":
      print("Would you like to have your configuration files for version 2.4 to be modified.\ny n")
      answer = input()
      if answer == 'y' or answer == 'Y':
        httpd_conf()
        default_conf()
          
        print("Have you installed the httpd.exe.\ny n")
        answer = input()
          
        if answer == 'y' or answer == 'Y':
            apache_rst()
        elif answer == 'n' or answer == 'N':
            install()
            apache_rst()
        else:
              print('Please enter a valid responce')
          
      elif answer == 'n' or answer == 'N':
        print("If a more in depth explanation is needed, the recommend website is https://httpd.apache.org/docs/current/mod/core.html#options  ")
      else:
        print("Invalid input restart command")

    else:
      print("Would you like to have your configuration files for version 2.2 to be modified.\ny n")
      answer = input()
      if answer == 'y' or answer == 'Y':
        A2_conf()
        A2_default_conf()

        print("Have you installed the httpd.exe.\ny n")
        answer = input()
        if answer == 'y' or answer == 'Y':
            apache_rst()
        elif answer == 'n' or answer == 'N':
            install()
            apache_rst()
        else:
              print('Please enter a valid responce')
          
      elif answer == 'n' or answer == 'N':
        print("If a more in depth explanation is needed, the recommend website is https://httpd.apache.org/docs/current/mod/core.html#options ")
      else:
        print("Invalid input restart command")



### DUNDER CHECK ###
if __name__ == "__main__":
  main()
