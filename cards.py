from random import shuffle
# Need to add rules: if player does not pick same number or
# or same suit they cannot place card
#Need to add the crazy 8 card 
#Need to add a want to play again? input 

#challenges: could not get the value of the flipcard to test if it matches with player1's card



class Card(object): 
    def __init__(self, suit, value, image=None):
        self.suit = suit
        self.value = value
        self.image = image

class Deck(object): 
    def __init__(self, suits, values):
        self.suits = suits
        self.values = values
        self.deck = []
        self.buildDeck()

    def buildDeck(self): 
            for suit in self.suits:
                for value in self.values:
                    self.deck.append(Card(suit, value))
            self.shuffle() 

    def shuffle(self): 
        shuffle(self.deck)
        return self

    def deal(self): 
        if self.deck: 
            return self.deck.pop()
        else:
            print "No more cards"
            return self
    # def resetDeck(self):
    #     self.deck = []
    #     self.buildDeck()
    #     return self

class Player(object):
    def __init__(self, deck, name):
        self.hand = [] 
        self.name = name

    def draw(self):
        flipy = deck.deck.pop()
        self.hand.append(flipy)

    def flipCard(self): 
        flip = deck.deck.pop()
        print '\n',"Beginning Card" , flip.value, 'of', flip.suit

    def playerDeal(self):
        for i in range(1,9):
            card = deck.deal()
            self.hand.append(card)
        return self
            
    def view(self):
        count = 1
        for j in self.hand:
            print  count, '-', 'Card', j.value, 'of', j.suit
            count+=1

    def pick(self):
        self.view()
        play = True
        while play == True:
            drawing = True
            while drawing == True:
                card = (raw_input("Pess d  to draw  //  s to select "))
                if (card == 'd '):
                    self.draw()
                    self.view()
                if (card =='s '):
                    drawing = False
            select = input("Select Your Card: ")
            selection = self.hand[select-1]
            if (selection.value == selection.value or selection.suit == selection.suit):
                self.hand.remove(selection)
                print self.name, "played:", selection.value, "of", selection.suit
                print "Match to:", selection.value, "of", selection.suit,'\n'
                play = False
                drawing = False
            else:
                print 'Not a Match'
                drawing = True

    def eva(self):
        if len(self.hand) == 0:
            print 'player1 WINS!'
            return True
        else:
            return False

class getGame(Deck):
    def __init__(self, deck):
        playGame = True
        Turn = True
        player1 = Player(deck, 'Player 1')
        player2 = Player(deck, 'Player 2')
        answer = True
        while answer == True:
            answer = (raw_input('Do you want to play a game? Y/N:  '))
            if (answer == 'y'):
                playGame = True
                answer = False
            elif (answer =='n'):
                playGame = False
                answer = False
            else:
                print 'Not an option'
                answer = True
        player1.playerDeal()
        player2.playerDeal()
        player1.flipCard()
        while playGame == True:
            while Turn == True:
                print "Player 1's Hand\n"
                player1.pick()
                if player1.eva() == True:
                    playGame = False
                    break
                Turn = False
            while Turn == False:
                print "Player 2's Hand"
                player2.pick()
                if player2.eva() == True:
                    playGame = False
                    break
                Turn = True

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
deck = Deck(suits, values)
game1= getGame(deck)      

