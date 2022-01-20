# Project-Longbow
By:Collin Wiley and Jose Navarro

The goal of our project was to create a python script that could make or suggest changes to Apache Web Servers to configure them for best practice security standards. We each worked on a part of the script, splitting it by OS, Collin wrote the Linux portion and Jose wrote the Windows portion. Each OS has different approaches to how the config files are organized and work, so splitting it this way seemed like the best idea. In this document we will break down why we changed the setting we did and what they protect the server from. 


It is recommended to properly configure a firewall and/or a WAF to help secure the Apache server, but this was deemed out of the scope of this project as we decided to focus on best practice configurations for apache itself.
Linux

The script will auto install or update apache if it is already installed. The two main files that control the security configurations in linux are /etc/apache2/apache2.conf and /etc/apache2/conf-enabled/ security.conf. In Linux systems, Apache is modular, which means you are able to load and unload different modules that allow for different configurations. I wrote the script to give the user the option of directly making the changes, though I know doing that comes with risks, so they can also get a copy of the recommended changes placed in their respective directories. 


Linux

Apache.conf

I  changed the default security model of the server to not allow directory listings so that people accessing the server can not see all of the possible directories. This is the file where you can change timeout durations as well as to keep connections alive, both of which I left untouched as changing them both come with their own problems.

Security.conf

First, I changed the ServerSignature to off and set ServerTokens to prod which stops the server from displaying its version as a footer when erroring on a web page as well as displaying OS type and included modules in the server. 

In order to add some security measures the header module was added, which allows apache to check for things like XSS attacks. 

Header always set X-XSS-Protection "1;  mode=block"

Header set X-Frame-Options: "sameorigin"

These are the twp lines of code in which use the header module. The first is XSS protection, which stops pages from loading when an XSS attack takes place. The second protects against clickjacking attacks by preventing embedding pages from this site as frames. 

Windows

To start ,an apache server  is pretty easy to get up and running on windows. Download the zip file from https://httpd.apache.org/download.cgi
Then drag that to root c\. Then you can rename the folder that you unzip to Apache24. Then using the cmd you can go to the bin folder and download the httpd.exe. This will allow us to restart,start,stop the apache server with a simple cmd command.

/Apache24/conf/

In this directory you can find 5 files you can open using any text editor and two other directories. The main configuration file for the windows version of Apache is the httpd.conf file. Using python a script was made so that two lines are added to that file to ensure that the version of Apache we are using is not easily obtained.This change is also made to the httpd-default.conf file in the extra folder. But in this file these lines already exist so all it does is makes sures that they are set to the correct mode. 
