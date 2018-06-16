#!/bin/bash

# Auto Install Tools <3
# Coded By Mr.Bro_Tx
# rizkyjovanka254@gmail.com

# Bersihkan Layar
clear

#This colour
blue='\e[0;34'
cyan='\e[0;36m'
green='\e[0;34m'
okegreen='\033[92m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'

###################################################
# CTRL C
###################################################
trap ctrl_c INT
ctrl_c() {
clear
echo -e $red"[#]> (Ctrl + C ) Detected, Trying To Exit ... "
sleep 1
echo ""
echo -e $yellow"[#]> Thank You For Using My Tools ... "
sleep 1
echo ""
echo -e $white"[#]> Mr.Bro_Tx Wuzz Here ... "
sleep 1
exit
}

# Isi oc :*
echo -e $red"   @@@@@@   @@@@@@@    @@@@@@    @@@@@@   @@@  @@@  @@@ @@@ "
echo -e $red"   @@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@ @@@ "
echo -e $red"   !@@       @@!  @@@  @@!  @@@  @@!  @@@  @@!  !@@  @@! !@@ "
echo -e $red"   !@!       !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!!  !@! @!! "
echo -e $red"   !!@@!!    @!@@!@!   @!@  !@!  @!@  !@!  @!@@!@!    !@!@! " 
echo -e $white"   !!@!!!   !!@!!!    !@!  !!!  !@!  !!!  !!@!!!      @!!! " 
echo -e $white"      !:!  !!:       !!:  !!!  !!:  !!!  !!: :!!     !!: "  
echo -e $white"     !:!   :!:       :!:  !:!  :!:  !:!  :!:  !:!    :!: "
echo -e $white" :::: ::    ::       ::::: ::  ::::: ::   ::  :::     :: "  
echo -e $white" :: : :     :         : :  :    : :  :    :   :::     : "   
echo -e $white"                  v1 tools for penetration "
echo ""
echo -e $white"         ***********************************************"
echo -e $white"         #                                             #"
echo -e $white"         # $cyan  Toolkit For$red Penetration$white                   #"
echo -e $white"         # $cyan  4WSec Tools Recoded by$red Mr.Bro_tx$white          #"
echo -e $white"         # $cyan  Follow Me On Github:$red @rzkyrmajvnka$white        #"
echo -e $white"         # $cyan  My Site:$red https://haxor-sec.ga$white             #"
echo -e $white"         # $cyan  Contact Me In:$red rizkyjovanka254@gmail.com$white  #"
echo -e $white"         # $cyan  Team: $red Anon Cyber Team$white                    #"
echo -e $white"         #                                             #"
echo -e $white"         ***********************************************"
echo ""
echo -e $yellow" 01) Red Hawk"
echo -e $yellow" 02) D-Tect"
echo -e $yellow" 03) JomScan"
echo -e $yellow" 04) WPScan"
echo -e $yellow" 05) opendoor"
echo -e $yellow" 06) Metasploit"
echo -e $yellow" 07) Ngrok"
echo -e $yellow" 08) Wp Brute "
echo -e $yellow" 09) Hydra "
echo -e $yellow" 10) Weevely "
echo -e $yellow" 11) SQLMap "
echo -e $yellow" 12) Dirbuster "
echo -e $yellow" 13) Pybelt "
echo -e $yellow" 14) Xattacker "
echo -e $yellow" 15) WAScan "
echo -e $yellow" 16) a2sv "
echo -e $red" 99) Exit "
echo -e $white""
read -p "[Spooky@Tools]> " act;

if [ $act = 1 ] || [ $act = 01 ]
then
clear
echo -e $red" Installing Red Hawk "
sleep 1
apt update && apt upgrade
apt install php
apt install git
git clone https://github.com/Tuhinshubhra/RED_HAWK
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 2 ] || [ $act = 02 ]
then
clear
echo -e $red" Installing D-Tect "
sleep 1
apt-get update && apt-get upgrade
apt-get install git
apt-get install python2
git clone https://github.com/shawarkhanethicalhacker/D-TECT
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 3 ] || [ $act = 03 ]
then
clear
echo -e $red" Installing Joomscan "
sleep 1
apt-get update && apt-get upgrade
apt install perl
apt install git
git clone https://github.com/rezasp/joomscan
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 4 ] || [ $act = 04 ]
then
clear
echo -e $red" Installing Wpscan "
sleep 1
apt-get update && apt-get upgrade
apt install ruby
apt install curl
apt install git
git clone https://github.com/wpscanteam/wpscan
cd ~/wpscan
gem install bundle
bundle config build.nokogiri --use-system-libraries
bundle install
ruby wpscan.rb --update
cd ~/
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 5 ] || [ $act = 05 ]
then
clear
echo -e $red" Installing opendoor "
sleep 1
apt update && apt upgrade
apt install python3
git clone https://github.com/stanislav-web/OpenDoor
cd ~/opendoor
pip3 install -r requirements.txt
chmod +x opendoor.py
cd ~/
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 6 ] || [ $act = 06 ]
then
clear
echo -e $red" Installing Metasploit "
sleep 1
apt update && apt upgrade
apt install git
apt install wget
wget https://raw.githubusercontent.com/verluchie/termux-metasploit/master/install.sh
chmod 777 install.sh
sh install.sh
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 7 ] || [ $act = 07 ]
then
clear
echo -e $red" Installing Ngrok "
sleep 1
apt install wget
mkdir ngrok
cd ~/ngrokgit clone https://github.com/hahwul/a2sv.git
cd a2sv
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
cd ~/
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 8 ] || [ $act = 08 ]
then
clear
echo -e $red" Installing wpbf "
sleep 1
git clone https://github.com/atarantini/wpbf
cd ~/
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 9 ] || [ $act = 09 ]
then
clear
echo -e $red" Installing Hydra "
sleep 1
apt update && apt install -y wget
apt install hydra
wget http://scrapmaker.com/download/data/wordlists/dictionaries/rockyou.txt
cd ~/
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 10 ] || [ $act = 10 ]
then
clear
echo -e $red" Installing Weevely "
sleep 1
pkg update
pkg upgrade
git clone https://github.com/glides/Weevely
cd ~/
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 11 ] || [ $act = 11 ]
then
clear
echo -e $red" Installing SQLMap "
sleep 1
apt update && apt upgrade
apt install python2
git clone https://github.com/sqlmapproject/sqlmap.git
cd ~/
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 12 ] || [ $act = 12 ]
then
clear
echo -e $red" Installing Dirbuster "
sleep 1
apt-get update
apt-get install python
apt-get install git
git clone https://github.com/maurosoria/dirsearch.git
cd ~/
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 13 ] || [ $act = 13 ]
then
clear
echo -e $red" Installing Pybelt "
sleep 1
apt-get update
apt-get ugrade
git clone https://github.com/ekultek/pybelt.git
pip install –r requirements.txt
cd ~/
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 14 ] || [ $act = 14 ]
then
clear
echo -e $red" Installing Xattacker "
sleep 1
apt-get update
apt-get upgrade
apt install git
apt-install perlpip install argparse
pip install netaddr
git clone https://github.com/Moham3dRiahi/XAttacker
cd XAttacker
cd ~/
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 15 ] || [ $act = 15 ]
then
clear
echo -e $red" WAScan "
sleep 1
apt-get update
apt-get upgrade
git clone https://github.com/m4ll0k/WAScan.git
cd wascan 
pip install -r requirements.txt
cd ~/
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 16 ] || [ $act = 16 ]
then
clear
echo -e $red" a2sv "
sleep 1
git clone https://github.com/hahwul/a2sv.git
cd a2sv
cd ~/
echo -e $red" T E R I N S T A L L "
fi

if [ $act = 99 ] || [ $act = 99  ]
then
echo " Thanks For Using My Tools "
sleep 1
echo " Happy Hacking"
sleep 1
exit
fisleep 1
