from Board import *
from Player import *

def main():
    '''
    INPUT: Takes no input.
    OUTPUT: Plays a game of Connect Four, depending on user input.
    '''
    """Human versus AI game.  No code to write here!"""
    k = int(input("Enter ply (level from 0 to 5): "))
    px = "human"
    po = Player("O", "LEFT", k)
    b = Board(7, 6)
    playGame(b, px, po)
    
def playGame(b, px, po):
    """Plays a game of Connect Four.
       p1 and p2 are objects of type Player OR
       the string 'human'.
    """
    '''
    INPUT: Takes a board b, a player px, and a player po.
    OUTPUT: Plays a game of Connect Four, depending on AI or human player input.
    '''
    # Game starts with "X" moving, but this will alternate and thus
    # the nextPieceToMove will alternate during game play, so the
    # nextPieceToMove at the end of the game will be the winner which
    # could be "X" or "O".
    nextPieceToMove = "X"  
    nextPlayerToMove = px


    # FILL IN CODE HERE
    while (not b.isFull()):
        print(b)
        if (nextPlayerToMove == px):
            if(px == 'human'):
                move = int(input("Next col for X: "))
            else:
                move = px.nextMove(b)
            b.addMove(move,'X')
            nextPieceToMove = 'O'
            nextPlayerToMove = po
    
        else:
            if(po == 'human'):
                move = int(input("Next col for O: "))
            else:
                move = po.nextMove(b)
            b.addMove(move,'O')
            nextPieceToMove = 'X'
            nextPlayerToMove = px
        
        if(b.isFull()):
            print("Board is full!")
            break
        elif(b.winsFor('X')):
            print("X Wins! Congratulations!")
            break
        elif(b.winsFor('O')):
            print("O Wins! Congratulations!")
            break

    return(b.data, nextPieceToMove)
    