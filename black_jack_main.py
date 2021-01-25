from classes import Card
from classes import Deck
from classes import Player

if __name__ == '__main__':

    play_again = True

    while play_again:
        new_deck = Deck()
        new_deck.shuffle()
        player_one = Player('Kyle')
        player_two = Player('Computer')
        player_one_bust = False
        player_one_bust = False
        
        # Deal cards
        player_one.hitMe(new_deck.deal_one())
        player_two.hitMe(new_deck.deal_one())
        player_one.hitMe(new_deck.deal_one())
        player_two.hitMe(new_deck.deal_one())
        
        # Prevents bust on double Aces
        player_one.checkBust()
        
        print(player_one)
        print(player_two.name + ': ' + str(player_two.hand[0]))
        
        while player_one_bust == False:   
            
            action = input("Make a choice: (Hit/Stay): ")
            
            if action != 'Hit' and action != 'Stay':
                print("Incorrect value given. Please specify 'Hit' or 'Stay'")
            else:
                print("Action Accepted \n")
                
                if action == 'Hit':
                    dealt_card = new_deck.deal_one()
                    player_one.hitMe(dealt_card)
                    print(player_one.name + ' draws a ' + str(dealt_card) + '\n')     
                    player_one_bust = player_one.checkBust()
                    print(player_one)  
                   
                    if player_one_bust:
                        print(player_one.name + " has busted. " + player_two.name + " wins!")
                else:
                    break
                    
        if not player_one_bust:
            
            while player_two.total_points < 18:
                dealt_card = new_deck.deal_one()
                player_two.hitMe(dealt_card)
                print(player_two.name + ' draws a ' + str(dealt_card) + '\n')
                player_two_bust = player_two.checkBust()

            print(player_two)

            if player_two_bust:
                print("Player " + player_two.name + " has busted. Player " + player_one.name + " wins!")
            elif player_one.total_points > player_two.total_points:
                print(player_one.name + " has a higher score than " + player_two.name)
                print(player_one.name + " wins!")
            elif player_two.total_points > player_one.total_points:
                print(player_two.name + " has a higher score than " + player_one.name)
                print(player_two.name + " wins!")
            else:
                print(player_one.name + " and " + player_two.name + " have an equal score.")
                print("Dealer wins the draw!")
            
        replay = input("Do you wish to play again? (Y/N): ")
        print('\n')
        
        if replay == 'N':
            play_again = False