import random
import unittest

# SI 206 Fall 2017
# Homework 3 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time: Thursday 8:30
# People you worked with: 

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison 

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list 
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


def play_war_game(testing=False):
	# Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:
			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")


######### DO NOT CHANGE CODE ABOVE THIS LINE #########

## You can write any additional debugging/trying stuff out code here... 
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

#########







##**##**##**##@##**##**##**## # DO NOT CHANGE OR DELETE THIS COMMENT LINE -- we use it for grading your file
###############################################

### Write unit tests below this line for the cards code above.

class CardTests(unittest.TestCase):
	#Test 1: rank 12 = queen
	def test_cardrank12(self):
		c = Card(rank=12)
		self.assertEqual(c.rank, "Queen")
	#Test 2: rank 1 = ace
	def test_cardrank1(self):
		c = Card(rank = 1)
		self.assertEqual(c.rank, "Ace")
	#Test 3: rank 3 = 3
	def test_cardrank3(self):
		c = Card(rank = 3)
		self.assertEqual(c.rank, 3)
	#Test 4: suit 1 = clubs
	def test_cardsuitclubs(self):
		c = Card(suit = 1)
		self.assertEqual(c.suit, "Clubs")
	#Test 5: suit 2 = Hearts
	def test_cardsuithearts(self):
		c = Card(suit = 2)
		self.assertEqual(c.suit, "Hearts")
	#Test 6: access to suit_names
	def test_cardsuit_names(self):
		c = Card()
		self.assertEqual(c.suit_names, ["Diamonds","Clubs","Hearts","Spades"])
	#Test 7: test str method
	def test_cardstrmethod(self):
		c = Card(suit = 2, rank = 7)
		self.assertEqual(str(c), "7 of Hearts")
	#Test 8: test deck size
	def test_decksize(self):
		d = Deck()
		self.assertEqual(len(d.cards), 52)
	#Test 9: testpop_card return card
	def test_popcard(self):
		d = Deck()
		c = d.pop_card()
		knownc = Card()
		self.assertEqual(type(c), type(knownc))
	#Test 10: play_war_method
	def test_wargame(self):
		game = play_war_game(testing = True)
		tple = (1, 2, 3)
		strng = "play"
		self.assertEqual(type(game), type(tple))
		self.assertEqual(len(game), len(tple))
		self.assertEqual(type(game[0]), type(strng))
	#Test 11: tests that a card can be reassigned
	def test_reassignment(self):
		c = Card(suit = 1, rank = 1)
		c = Card(suit = 3, rank = 2)
		self.assertEqual(str(c), "2 of Spades")
	#Test 12: tests deck str method
	def test_deskstr(self):
		d = Deck()
		self.assertEqual(str(d), "Ace of Diamonds\n2 of Diamonds\n3 of Diamonds\n4 of Diamonds\n5 of Diamonds\n6 of Diamonds\n7 of Diamonds\n8 of Diamonds\n9 of Diamonds\n10 of Diamonds\nJack of Diamonds\nQueen of Diamonds\nKing of Diamonds\nAce of Clubs\n2 of Clubs\n3 of Clubs\n4 of Clubs\n5 of Clubs\n6 of Clubs\n7 of Clubs\n8 of Clubs\n9 of Clubs\n10 of Clubs\nJack of Clubs\nQueen of Clubs\nKing of Clubs\nAce of Hearts\n2 of Hearts\n3 of Hearts\n4 of Hearts\n5 of Hearts\n6 of Hearts\n7 of Hearts\n8 of Hearts\n9 of Hearts\n10 of Hearts\nJack of Hearts\nQueen of Hearts\nKing of Hearts\nAce of Spades\n2 of Spades\n3 of Spades\n4 of Spades\n5 of Spades\n6 of Spades\n7 of Spades\n8 of Spades\n9 of Spades\n10 of Spades\nJack of Spades\nQueen of Spades\nKing of Spades")





#############
## The following is a line to run all of the tests you include:
unittest.main(verbosity=2) 
## verbosity 2 to see detail about the tests the code fails/passes/etc.