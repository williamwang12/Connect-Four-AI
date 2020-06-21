from Board import *
import random
class Player:
    """Class that defines a Connect 4 player."""

    def __init__(self, ox, tbt, ply):
        self.symbol = ox
        self.tieRule = tbt
        self.ply = ply

    def __repr__(self):
        output = ""
        output += "Player for " + self.symbol + "\n"
        output += "  with tiebreak: " + self.tieRule + "\n"
        output += "  and ply == " + str(self.ply) + "\n"
        return output
    
    def oppChar(self):
        """Return the opposite game piece character."""
        if self.symbol == "O": return "X"
        else: return "O"

    def scoreBoard(self, b):
        """Return the score for the given board b."""
        '''
        INPUT: Takes a self object, and a board b.
        OUTPUT: Returns 100.0 if the board is won by the player, 0.0 if lost, and 50.0 if neither.
        '''
        if(b.winsFor(self.symbol)):
            return 100.0
        elif(b.winsFor(self.oppChar())):
            return 0.0
        else:
            return 50.0
    def tiebreakMove(self, scores):
        """Return column number of move based on self.tbt."""
        '''
        INPUT: Takes an array of scores integers.
        OUTPUT: Depending on the tieRule, returns the col to choose.
        '''
        maxNum = max(scores)
        colNums = []
        for i in range(len(scores)):
            if(scores[i] == maxNum):
                colNums.append(i)

        if (self.tieRule == 'LEFT'):
            return colNums[0]
        elif (self.tieRule == 'RIGHT'):
            return colNums[len(colNums) - 1]
        else:
            return random.choice(colNums)


    def scoresFor(self, b):
        """Return a list of scores for board d, one score for each column
            of the board."""
        '''
        INPUT: Takes a self object, and a board b.
        OUTPUT: Finds the scores array for the current board, seeing ply turns into the future, and deciding optimally.
        '''
        scores = []
        for s in range(b.width):
            scores.append(50.0)
            copyB = b.shallowCopy()
            if(copyB.winsFor(self.symbol)):
                scores[s] = 100.0
                continue
            elif(copyB.winsFor(self.oppChar())):
                scores[s] = 0.0
                continue               

            if(self.ply == 0):
                continue
            else:
                if (not copyB.isFull() and not copyB.winsFor(self.symbol) and not copyB.winsFor(self.oppChar())):
                    copyB.addMove(s,self.symbol)
                    op = Player(self.oppChar(),self.tieRule,self.ply - 1)
                    opScore = max(op.scoresFor(copyB))
                    selfScore = 100 - opScore
                    scores[s] = selfScore
        
        return scores
    def nextMove(self, b):
        '''
        INPUT: Takes a self object, and a board b.
        OUTPUT: Finds the next move to use, using scoresFor() and tieBreakMove()
        '''
        """Accepts a board input and returns the next move for this player,
           where a move is a column in which the player should place its
           game piece."""

        scoresList = self.scoresFor(b)
        return self.tiebreakMove(scoresList)
	