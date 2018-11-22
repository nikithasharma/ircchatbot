#!/usr/bin/python3
import socket
import random
import sys

sys.path.insert(0,"\HOME\Desktop")
import dictionary
from dictionary import motivational,literature,philosophical,jokes

socket.getaddrinfo("182.73.209.206",6665)
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.net" # Server
channel = "##testabotforme" # Channel
botnick = "pybot" #  bots nick
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
        sendmsg("Hello! my name is pybot . I'm an IRC bot that can bombard your life with quotes! Right now I've got three types of quotes,1.Motivational 2.Philosophical 3.Literary. What kind of quote would you like to see?.If you are not interested in quotes I have some funny jokes also.")
      if message.rstrip()=="jokes":
        sendmsg(random.choice(jokes))
      if message.rstrip()=="motivational":
        sendmsg("With whose quote can i inspire you ? Bill Gates ,Confusius,Paulo Coelho,Nelson Mandela or Abdul Kalam?")
      if message.rstrip()=="literary":
        sendmsg("Would you like to see quotes by Margaret Atwood ,Ezra Pound ,Nelson Mandela,John Updike or Italo Calvino?")
      if message.rstrip()=="philosophical":
        sendmsg("Would you like to see quotes by Nietzche, Freud, Karl Marx, Kant or Kierkegaard?")
      if message.rstrip()=="Bill Gates":
        sendmsg(random.choice(motivational["Bill Gates"]))
      if message.rstrip()=="Confusius":
        sendmsg(random.choice(motivational["Confusius"]))
      if message.rstrip()=="Paulo Coelho":
        sendmsg(random.choice(motivational["Paulo Coelho"]))
      if message.rstrip()=="Nelson Mandela":
        sendmsg(random.choice(motivational["Nelson Mandela"]))
      if message.rstrip()=="Abdul Kalam":
        sendmsg(random.choice(motivational["A.P.J.Abdul Kalam"]))
      if message.rstrip()=="Margaret Atwood":
        sendmsg(random.choice(literature["Margaret Atwood"]))
      if message.rstrip()=="Ezra Pound":
        sendmsg(random.choice(literature["Ezra Pound"]))
      if message.rstrip()=="John Updike":
        sendmsg(random.choice(literature["John Updike"]))
      if message.rstrip()=="Italo Calvino":
        sendmsg(random.choice(literature["Italo Calvino"]))
      if message.rstrip()=="Forster":
        sendmsg(random.choice(literature["Forster"]))
      if message.rstrip()=="Nietzsche":
        sendmsg(random.choice(philosophical["Nietzsche"]))
      if message.rstrip()=="Freud":
        sendmsg(random.choice(philosophical["Frued"]))
      if message.rstrip()==" Karl Marx":
        sendmsg(random.choice(philosophical["Marx"]))
      if message.rstrip()=="Kant":
        sendmsg(random.choice(philosophical["Kant"]))
      if message.rstrip()=="Kierkegaard":
        sendmsg(random.choice(philosophical["Kiekegaard"]))
      if message.rstrip() == exitcode:
        sendmsg("oh...okay. :'(")
        ircsock.send(bytes("QUIT \n", "UTF-8"))
        return
    else:
      if ircmsg.find("PING :") != -1:
        ping()
main()