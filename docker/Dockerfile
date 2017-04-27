FROM kalilinux/kali-linux-docker

MAINTAINER calee

RUN yes | apt-get update
RUN yes | apt-get upgrade
RUN yes | apt-get install vim git python python-pip wireshark
RUN git clone https://github.com/zardus/ctf-tools.git
RUN git clone https://github.com/calee0219/.dotfiles
RUN ~/.dotfiles/app_install.sh
RUN pip install Crypto pwn
