# Gives an example on how to use Round Robin in a tournament
# There are some Players playing a generic tournament and getting score
# by random chance. The program assigns all matches in advance, then plays the
# tournament and finally prints the final score
# The number of matches needed for n players is (n/2)*(n-1)

import math
import sys
import collections
import random

class Player:
    rounds = 0
    wins = 0
    losses = 0
    dummyrounds = 0
    number = 0
    finishedGames = dict()
    isDummy = False

    def __init__(self, nr, dummy):
        self.number = nr
        self.isDummy = dummy

    def playGame(self, otherPlayer, result):
        if (self.isDummy):
            self.finishedGames[otherPlayer.number] = 0
            self.rounds += 1
            self.dummyrounds += 1
            #print("Player #" + str(self.number) + " is dummy, skipping")
            return
        if (otherPlayer.isDummy == True):
            self.dummyrounds += 1
            self.rounds += 1
            self.finishedGames[otherPlayer.number] = 0
            #print("Player #" + str(self.number) + " faced dummy, skipping")
            return
        self.finishedGames[otherPlayer.number] = result
        self.rounds += 1
        if (result == 1):
            self.wins += 1
        else:
            self.losses += 1

        #print("Player #" + str(self.number) + " ended a game with #" + str(otherPlayer.number) + " with score of " + str(result))

    def pprint(self):
        print("Player #" + str(self.number) + " wins: " + str(self.wins) + "/" + str(self.rounds) + ", dummies: " + str(self.dummyrounds))

class Tournament:

    roundsToPlay = 0
    roundsPlayed = 0
    roundsPerPlayer = 0
    players = []
    fixedPlayer = 0
    pairings = dict()
    scores = collections.defaultdict(list)

    def __init__(self, playerList):
        self.players = playerList

    def doPairing(self):
        # If we have an odd number of players, add one dummy player
        if (len(self.players) % 2 != 0):
            print("Uneven number of players, adding one dummy")
            temp_player = Player(len(self.players)+1, True)
            self.players.append(temp_player)
        self.roundsToPlay = (int)(math.ceil(len(self.players))/2.0) * (len(self.players) - 1)
        self.roundsPerPlayer = len(self.players)-1
        self.fixedPlayer = self.players[0].number
        print("We will play " + str(self.roundsToPlay) + " rounds and player #" + str(self.fixedPlayer) + " is fixed")
        print("Each player plays " + str(self.roundsPerPlayer) + " rounds")

        # Create a dict containing round number and pairings
        # Ie. [0] = {(1,10), (2,9), (3,8) ...}
        #     [1] = {(1, 9), (10,8), (2, 7) ... }

        # First split the list in two
        top_list = self.players[0 : len(self.players)/2]
        bottom_list = self.players[len(self.players)/2 : len(self.players)]

        # Then reverse the bottom row
        bottom_list.reverse()

        #sys.stdout.write("Top row:\t\t ")
        #for p in top_list:
        #    sys.stdout.write(str(p.number) + " ")
        #sys.stdout.write("\nBottom row:\t\t ")
        #for p in bottom_list:
        #   sys.stdout.write(str(p.number) + " ")
        #sys.stdout.write("\n")

        self.pairings[0] = (top_list, bottom_list)

        for r in range(1, self.roundsToPlay):

            #print("Round #" + str(r))

            # Copy the data
            self.pairings[r] = self.pairings[r-1]
            l = self.pairings[r]

            # The last element of the first row hops to the bottom row
            # The first element of the second row hops to the top row
            # Copy these to temp variables for storage
            temp1 = l[0][len(l[0])-1]
            temp2 = l[1][0]

            #print(str(temp1.number) + " " + str(temp2.number))

            # Move all elements of the top list right, except the first static one
            top = collections.deque(l[0])
            top.rotate(1)

            # Add the new value from row 2 and copy the static player back
            top[0] = top[1]
            top[1] = temp2

            #for p in top
            #    sys.stdout.write(str(p.number) + " ")
            #sys.stdout.write("\n")

            # Same for bottom row, but left
            bottom = collections.deque(l[1])
            bottom.rotate(-1)

            # Copy the missing member from row 1 to row 2 end
            bottom[len(bottom)-1] = temp1
            
            #for p in bottom:
            #    sys.stdout.write(str(p.number) + " ")
            #sys.stdout.write("\n")

            # Now simply copy the data back in
            l = (top, bottom)
            self.pairings[r] = l


    def play(self):
        for roundNr in self.pairings:
            #print("Round #" + str(roundNr) + " starting")
            count = 0
            for player in self.pairings[roundNr][0]:

                # For easier reading, assign other player to temp variable
                opponent = self.pairings[roundNr][1][count]
                # Get random result
                result = 1
                if (random.random() > 0.5):
                    result = 0

                self.scores[player.number].append(result)
                
                # Report result for both players
                player.playGame(opponent, result)
                if (result == 0):
                    result = 1
                elif (result == 1):
                    result = 0

                opponent.playGame(player, result)
                self.scores[opponent.number].append(result)
                count += 1

    def score(self):

        self.players.sort(key=lambda x: x.wins, reverse=True)
        print("Player #" + str(self.players[0].number) + " wins")

        for x in self.scores:
            sys.stdout.write("Player #" + str(x) + " ")
            for pscore in self.scores[x]:
                sys.stdout.write(str(pscore) + "|")
            sys.stdout.write("\n")

        for p in self.players:
            print("Player #" + str(p.number) + " has score of " + str(p.wins) + "/" + str(p.rounds))

if __name__ == "__main__":
    playerList = []

    for x in range(1,8):
        playerList.append(Player(x, False))

    t = Tournament(playerList)
    t.doPairing()

    t.play()
    t.score()
 
