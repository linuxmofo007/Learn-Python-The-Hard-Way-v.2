#!/usr/local/bin/python

# VERY simple drug dealer game. #

#
# Variables
#

cash = 2000
weapon = "Bare Hands"
drugs = "None"
drug_kilos = 0

#
# Functions #
#

# main room
def main_room():
  print "Welcome to Drug Wars v. 1"
  print "Enter your hood rat, drug dealin', gangsta' ass name: "
  player_name = raw_input("> ")

  print "Welcome to Chicago %r" % player_name
  print "Your player current has the following stats..."
  player_stats()
  print "You can always type 'help' to view your available commands."
  player_prompt()

# help menu
def help():
  print "You can use the following commands..."
  print "'buy drugs', 'help', 'stats'"
  player_prompt()

# player stats
def player_stats():
  print "Weapon: %r" % weapon
  print "Money: %r" % cash  
  print "Drugs: %r" % drugs

# quit game 
def player_quit():
  print "What, the game too hard for you?"
  print "Type 'yes' or 'no'"
  too_hard = raw_input("> ")
  if too_hard == "yes":
    print "Okay little girl, go back home to your mommy."
    print "You are leaving with the pathetic stats of..."
    player_stats()
    exit(0)
  elif too_hard == "no":
    print "Oh that must have been a mistake then right?"
    print "You current have the following stats..."
    player_stats()
    player_prompt()

# player prompt / main control of the game
def player_prompt():
  command = raw_input("> ")
  if command == "help":
    help()
  elif command == "stats":
    player_stats()
  elif command == "buy drugs":
    buy_drugs(cash)
  elif command == "quit":
    player_quit()
  else:
    print "Command not found. Try again."
  player_prompt()

def drug_deal(xcash, xcost, xdrugs, xkilos):
  if xcost > xcash:
    print "Sorry Homie, that aint enough"
    print "You have %r dollars and you need %r dollars to purchase." % (xcash, xcost)
  elif xcost <= xcash:
    cash = xcash - xcost
    drugs = xdrugs
    drug_kilos = xkilos
    print "You now have %r dollars, %r kilos of %r." % (cash, drug_kilos, drugs)
    return cash
    player_prompt()
  else:
    die("Something went wrong.")
  
def buy_drugs(xcash):
  print "Drug Dealer >>> \"Pssst, you need somethin?"
  print "Type 'yes' or 'no'"
  answer = raw_input("> ")
  if answer == "no":
    print "Get out of here, don't waste my time any more!"
    player_prompt()
  else:
    print "Here's what I got!"
    print "weed:   1 kilo:  $500"
    print "meth:   1 kilo:  $1500"
    print "crack:  1 kilo:  $3000"
    print "heroin: 1 kilo:  $5000"
    print "What do you want?"
    drugs = raw_input("> ")
    if drugs == "weed":
      cost = 500
      print "How many kilos do you want?"
      kilos = raw_input("> ")
      print "This is going to cost you ", int(kilos) * cost, "."
      print "Is this what you want? ('yes' or 'no')"
      answer = raw_input("> ")
      if answer == "no":
        print "Drug Dealer >>> I don't like people wasting my time..."
        print "** The drug dealer takes all your money! **"
        cash = 0
        return cash
        player_prompt()
      if answer == "yes":
        drug_deal(xcash, cost, drugs, kilos)
      else:
        print "Command not found"
        player_prompt()
       
# Start this game! #
main_room()
