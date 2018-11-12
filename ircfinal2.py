#!/usr/bin/python3
import socket
import random
import sys

sys.path.insert(0,"\HOME\Desktop")
import dictmotivational
from dictmotivational import motivational
socket.getaddrinfo("182.73.209.206",6665)
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.net" # Server
channel = "##testabotforme" # Channel
botnick = "chatterzz" #  bots nick
adminname = "bot123" 
exitcode = "bye " + botnick
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "\n", "UTF-8")) #We are basically filling out a form with this line and saying to set all the fields to the bot nickname.
ircsock.send(bytes("NICK "+ botnick +"\n", "UTF-8")) # assign the nick to the bot
def joinchan(chan): # join channel(s).
  ircsock.send(bytes("JOIN "+ chan +"\n", "UTF-8")) 
  ircmsg = ""
  while ircmsg.find("End of /NAMES list.") == -1:  
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)
def ping(): # respond to server Pings.
  ircsock.send(bytes("PONG :pingis\n", "UTF-8"))
def sendmsg(msg, target=channel): # sends messages to the target.
  ircsock.send(bytes("PRIVMSG "+ target +" :"+ msg +"\n", "UTF-8"))
def main():
  joinchan(channel)
  while 1:
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)
    if ircmsg.find("PRIVMSG") != -1:
      name = ircmsg.split('!',1)[0][1:]
      message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
    if ircmsg.find("PRIVMSG") != -1:
      name = ircmsg.split('!',1)[0][1:]
      message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
      if message.rstrip()=="Hi":
        sendmsg("Hello!")
      if message.rstrip()=="Bill Gates":
        sendmsg(random.choice(motivational["Bill Gates"]))
      if name.lower() == adminname.lower() and message.rstrip() == exitcode:
        sendmsg("oh...okay. :'(")
        ircsock.send(bytes("QUIT \n", "UTF-8"))
        return
    else:
      if ircmsg.find("PING :") != -1:
        ping()
main()