import random

suits = ('Clubs','Spades','Hearts','Diamonds')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 
          'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    
    def __init__(self):

        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                temp_card = Card(suit,rank)
                self.all_cards.append(temp_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

class Player:
    
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.total_points = 0
        self.num_of_aces = 0
        
    def hitMe(self,a_card):
        self.hand.append(a_card)
        self.total_points += a_card.value
        
        if a_card.rank == 'Ace':
            self.num_of_aces += 1
    
    def checkBust(self):
        
        while self.total_points > 21 and self.num_of_aces > 0:
            
            for card in range(len(self.hand)):
                if self.hand[card].rank == 'Ace' and self.hand[card].value == 11:
                    self.hand[card].value = 1
                    self.total_points -= 10
                    self.num_of_aces -= 1
                    break
            
        if self.total_points > 21:
            return True
        else:
            return False
            
    def __str__(self):
        my_hand_text = []
        
        for card in range(len(self.hand)):
            my_hand_text.append(str(self.hand[card]))
            
        return '{} \n {} \n Total Points: {} \n'.format(self.name,my_hand_text,self.total_points)