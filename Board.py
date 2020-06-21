# Connect 4 Game Board

class Board:
    """Class that defines a Connect 4 Board."""

    def __init__(self, width = 7, height = 6):
        """The constructor for objects of type Board"""
        self.width = width
        self.height = height
        self.data = [[' ']*width for r in range(height)]

    def getWidth():
        return self.width

    def getHeight():
        return self.height

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board
        """
        s = ''                  # The string to return
        for row in range(self.height):
            s += '|'            # Add the spacer character
            for col in range(self.width):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '--'*self.width    # Add the bottom of the board
        s += '-\n'
        for col in range(self.width):
            s += ' ' + str(col%10)
        s += '\n'
        return s                # The board is complete, return it

    def addMove(self, col, ox):
        '''
        INPUT: Takes a self board object, a column to add in, and the symbol of the move.
        OUTPUT: Adds the move to the board and updates the data.
        '''
        rangeNum = list(range(self.height))
        rangeNum.reverse()

        for i in rangeNum:
            if(self.data[i][col] == ' '):
                self.data[i][col] = ox
                break

    def clear(self):
        '''
        INPUT: Takes a self board object.
        OUTPUT: Clears the board, and makes everything ' ' value.
        '''
        for i in range(self.height):
            for s in range(self.width):
                self.data[i][s] = ' '

    def setBoard(self, moves):
        """Set the board using an input string representation."""
        '''
        INPUT: Takes a self board object, and a string of moves.
        OUTPUT: Places O's and X's alternatively, on the columns specified in moves.
        '''
        newBoard = Board(self.width,self.height)

        for i in range(len(moves)):

            if (i%2 == 0):
                newBoard.addMove(int(moves[i]),'X')
            else:
                newBoard.addMove(int(moves[i]),'O')
        self.data = newBoard.data
        
    def allowsMove(self, col):
        """Return True if adding a game piece in the given column is 
           permitted and return False otherwise."""
        '''
        INPUT: Takes a self board object, and a column to check.
        OUTPUT: Returns True if the game piece can be added into col, and False if not.
        '''
        if(self.data[0][col] == ' '):
            return True
        return False

    def isFull(self):
        """Return True if the game board is full and False otherwise."""
        '''
        INPUT: Takes a self board object.
        OUTPUT: Returns True if the board is full, and False if it is not.
        '''
        for i in range(self.width):

            if (self.data[0][i] == ' '):
                return False

        return True

    def delMove(self, col):
        """Delete the topmost game piece from the given column."""
        '''
        INPUT: Takes a self board object, and a column to delete a move from.
        OUTPUT: Deletes the topmost move from the board and updates the data.
        '''
        for i in range(self.height):

            if(not self.data[i][col] == ' '):
                self.data[i][col] = ' '
                break

    def winsFor(self, ox):
        """Return True if the game has been won by player ox where ox
           is either 'X' or 'O'."""
        '''
        INPUT: Takes a self board object, and a game piece.
        OUTPUT: Checks horizontal, vertical, and diagonal right and left to see if the specified piece has won.
        '''
        return (self.checkVictory('V',ox) or self.checkVictory('H',ox) or self.checkVictory('DL',ox) or self.checkVictory('DR',ox))

    def checkVictory(self, direction, ox):
        ''' HELPER FUNCTION
        INPUT: Takes a self board object, direction to check, and a game piece.
        OUTPUT: Checks if there are four ox pieces in a row, in vertical, horizontal, diagonal-left, or diagonal-right orientation.
        '''
        rangedH = list(range(self.height - 3))
        rangedW = list(range(self.width - 3))
        if (direction == 'H'):
            x,y=0,1
            rangedH = list(range(self.height))
        elif (direction == 'V'):
            x,y=1,0
            rangedW = list(range(self.width))
        elif (direction == 'DL'): x,y=1,1
        else:
            x,y=1,-1
            rangedH = list(range(self.height-3))
            rangedW = list(range(3,self.width))
            rangedH.reverse()
            rangedW.reverse()         

        for i in rangedH:
            for s in rangedW:

                if (self.data[i][s] == ox):
                    adjacents = [self.data[i][s], self.data[i+x][s+y],self.data[i+(x*2)][s+(y*2)],self.data[i+(x*3)][s+(y*3)]]
                    if (adjacents == [ox,ox,ox,ox]):
                        return True
                        
        return False
    
    def shallowCopy(self):
        '''
        INPUT: Takes a self board object.
        OUTPUT: Makes a shallow copy of the board and returns it.
        '''
        newBoard = Board(self.width,self.height)
        for i in range(self.height):
            for s in range(self.width):
                newBoard.data[i][s] = self.data[i][s]
        return newBoard
