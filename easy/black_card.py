#!/usr/bin/env python3

"""https://www.codeeval.com/open_challenges/222/

Black card

Challenge Description:

You must have heard about pirates, their customs, pirates code, and the “black
spot”. If a pirate is presented with a “black spot”, he is officially pronounced
guilty, meaning he will soon be expulsed from the pirate brotherhood or even be
dead.
We don’t have as strict rules as pirates have, and a person who receives a
black spot simply leaves the game.
For example, we have a list of three players: John, Tom, Mary, and a number 5.
Starting with the first player (in our case, it’s John), we start to count all
players: John – 1, Tom – 2, Mary – 3, and then again starting from the first one
John – 4, Tom – 5. As Tom gets number 5, he should leave. Now, we have John and
Mary and start counting again. John gets number 5, so he leaves. Thus, the
winner is Mary.

Input sample:

The first argument is a path to a file. Each line includes a test case with
names of players and a number for a “black spot”. Players and a number are
separated by a pipeline '|'.

For example:

John Sara Tom Susan | 3
John Tom Mary | 5

Output sample:

Print the name of a winner.

For example:

Sara
Mary

Constraints:

   1 Always start counting from the first name in a list.
   2 Number of players can be from 3 to 10.
   3 Number of turns can be from 3 to 15.
   4 The number of test cases is 40.

"""

import sys

def main(dfile):
    """Black Card
    @param dfile: data file path
    @type of dfile: str
    """

    with open(dfile, 'r') as dfld:
        for l in dfld:
            l = l.strip('\n')
            players, turn = l.split(' | ')
            players = players.split()
            turn = int(turn)

            while len(players) > 1:
                i = turn % len(players)

                if not i:
                    players.pop()
                    continue
                    
                players = players[0 : i - 1] + players[i : len(players)]

            print(players[0])
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    

