'''
Introduction
The Snap Games team needs your help in implementing a matchmaking system for friend based games! 
Your system will be provided with two inputs(format below); the first provides the social graph 
information and the second is a list of matching requests (games) to simulate the realtime function 
of your system. Your task will be to develop a functioning friend matchmaking system based on the
 requirements below. Please use the language that you’re most proficient in.
The Snap Engineering team takes code quality and user experience very seriously so please include 
unit tests or other ways to prove correctness in your code, and add any comments to the code that 
would be useful for other software engineers who would need to work on your system in the future. 
A meaningful portion of your time should be spent on ensuring your code is correct and workable for 
other engineers. Please include in your readme(or comments) a description of your memory usage and 
your matching runtimes using Big O notation
The goal of your system is to match game players together based on certain rules. We strongly 
suggest breaking down the system setup and each of the rules into several phases so we will outline 
them that way. Note your system will not care about which game(s) users are playing, it is just 
concerned who is playing with who

Deliverables
Please include a readme(or comments) with instructions on how to run and test your code.  
At the end of the interview. We’ll use Codepair and the codepair link is the final deliverable.

Phase 1 - Reading the Social Graph

You are provided with friendgraph, which contains a list of friend relationships. Just like in Snapchat, 
friend relationships can be unidirectional (User A adds User B, but User B hasn’t added User A) 
or bidirectional (User A and User B have both added each other). The format of “friendgraph” has 
each unidirectional relationship listed on each line, with space delimited usernames. The first 
username represents the friend who added the second username on each line. 

Example “friendgraph” input
-------------------
shreya bob
bob yang
bob shreya
yang shreya
bob cecilia
cecilia michael
cecilia bob

In this graph, shreya and bob are bidirectional friends, bob and yang are unidirectional friends 
(bob has added yang, but yang hasn’t added bob) and yang and shreya are unidirectional friends 
(yang has added shreya but shreya hasn’t added yang). 

Your code should parse “friendgraph” and build the social graph in memory. It is up to you how 
you construct and store the information.

Phase 2 - Reading the Games
After the social graph is constructed, your system should read the list of games that need to 
have players matched to it. You are provided with games. Each line represents a new game, and 
games are unrelated to each other meaning a player can be matched to multiple games. 
Each line will have a username, the person who is initiating the game, and a non-zero 
positive integer, the number of players in the game. The rules for doing the matching 
will be detailed in Phase 3.

Example “games” input
----------------------
shreya 5
bob 4
yang 3


Phase 3 - Friend Based Game Matching Part 1 - Unidirectional Friends
In this phase, modify your system so that it generates the game matches based on the degrees 
of friendship, the lower the better. If User A has added User B as a friend their degree of 
friendship is 1, regardless of whether User B has added User A or not. If User B has added 
User C and User A has not added User C then User A’s degree of friendship to User C is 2. 

In this phase, create an output “matches-phase3”, in which each line represents the game listed 
in “games” in Phase 2  with the following rules in mind --
The first name on each line should be the person who is starting the game (the person listed in “games”)
the order of the players matched into the game does not matter. 
If a game has room for more players than someone has available friends, then other users in the 
system should be matched in even if there is no degree of friendship relationship available. 
Users can be matched into more than one game.

Example Output, using the same friendgraph and games from above:

matches-phase3
----------------------
shreya bob cecilia michael yang
bob shreya cecilia yang
yang bob shreya

shreya bob
bob yang
bob shreya
yang shreya
bob cecilia
cecilia michael
cecilia bob

Phase 4 - Friend Based Game Matching Part 2 - Bidirectional Friends
In Phase 3 you matched players into a game based on the unidirectional friend relationships 
i.e. User B did not have to add User A as a friend in order to be matched into a game with them. 
In this phase, modify the system so that it only matches users into a game as long as they have 
at least 1 bidirectional friend already matched into the game. Thus the order of the players 
matched into the game matters and this should be reflected in your output. If there are more 
spots into a game than friends that meet this requirement then do not fill up the match with other 
players. Using the “friendgraph” and “games” input above you would generate:

matches-phase4
----------------------
shreya bob cecilia
bob shreya cecilia --OR-- bob cecilia shreya
yang

Phase 5 - Users Going Online & Offline
In the previous phases we assumed all users were online at the same time (and thus eligible to 
be matched and play a game) and stayed online. In this phase we will add support for users going 
offline and online. To start with, assume all users in the system are online at the same time. 
We will use the bidirectional friend matching logic from phase 4. You are provided with 
online-offline, where each line in the input file has a name and a new user online state 
(“online” or “offline”). For each new state of a user, rerun the matching algorithms for the games 
they’re matched into, or games that need more players. If a user is currently matched into a game 
and goes offline, another user should be tried to match into the game if that user fits the matching 
rules from phase 4. For each change of user state, print out the matches that have changed. 
The output format should list the name of the change e.g. “cecilia offline” and then on each 
subsequent line list any matches that have changed, one per line, in the same format as 
“matches-phase4”. After each online/offline change and the group of matches that change leave an 
empty line in the output file before the next online/offline change and associated matching changes. 

online-offline
----------------------
cecilia offline
cecilia online


online-offline-changes
----------------------
cecilia offline
shreya bob 
bob shreya --OR-- bob shreya
yang

cecilia online
shreya bob cecilia
bob shreya cecilia --OR-- bob cecilia shreya
Yang
'''

from collections import defaultdict
from typing import List


class FriendsGraph:
    def __init__(self):
        # Dictionary to store the Vertices and Edges of the graph 
        self.graph = defaultdict(list)
        # Dictionary to store a user and number of players
        self.games = defaultdict(int)

    # populate the friend's graph using adjacency list 
    def add_friends(self, friends: List[List[str]]) -> None:
        # Time: O(V + E)
        for f1, f2 in friends:
            self.graph[f1].append(f2)

    def print_friends(self):
        # Method to print the graph 
        for i in self.graph.keys():
            print(i, '->', ' -> '.join([str(j) for j in self.graph[i]]))

    def start_new_game(self, g):
        # Store a new game in the dictionary 
        # Time: O(n)
        for user, no_of_games in g:
            self.games[user] = no_of_games
        return self.games

    def all_games(self):
        """
        Come back to this method.
        """
        match_phases = []
        for player in self.games.keys():
            match_phases.append(self.generate_games(player))
        return match_phases

    def generate_games(self, player: str) -> List[str]:
        # BFS: Breadth First Search Algorithm
        # Time: O(V)
        explored = set()
        queue = [player]
        res = []
        while len(explored) < self.games[player]:
            v = queue.pop(0)
            for w in self.graph[v]:
                if w not in explored:
                    explored.add(w)
                    queue.append(w)
                    res.append(w)
        return res

    def have_bidirectional_relationship(self, f1, f2) -> bool:
        # check if two friends have bidirectional relation
        return f2 in self.graph[f1] and f1 in self.graph[f2]

    def generate_bidirectional(self, friends):
        res = set()
        # Time: O(n) because we are checking in the dictionary 
        # Space: O(n) use of the set data structure
        for f1, f2 in friends:
            if self.have_bidirectional_relationship(f1, f2):
                res.add(f1)
        return list(res)

    def phase4(self, friends):
        # Time: O(n) We are looping in the self.games dictionary 
        # Space: O(n) Use of the output array
        output = []
        print("matches-phase4")
        print("----------------")
        for user in self.games.keys():
            # print(user)
            if user in self.generate_bidirectional(friends):
                output.append(self.generate_bidirectional(friends))
            else:
                output.append([user])
        return output

    @staticmethod
    def online_offline(status_update, current_online_players):
        # Time: O(n^2) We could've optimized this algorithm by using Dictionary and quickly
        # finding the user we need to change the status for. It would've changed the Time
        # complexity to O(n), but since our input is small, I opted using this algorithm
        print("matches-phase5")
        print("----------------")
        user, status = status_update
        user_idx = 0
        # check list of current online players
        output = current_online_players[:]
        for players in current_online_players:
            for i in range(len(players)):
                # check if current player is the user we need to change the 'status'
                if players[i] == user:
                    user_idx = i
        i = 0
        while i < len(curr_online_players):
            if len(output[i]) > 1 and status == "offline":
                output[i].pop(user_idx)
            i += 1

        return output


class Game:
    def __init__(self, ):
        self.games = defaultdict(int)

    def start_new_game(self, g):
        for user_name, n_of_games in g:
            self.games[user_name] = n_of_games
        return self.games

    def get_games_data(self):
        return self.games

    def generate_friends(self):
        res = []
        friends = FriendsGraph()
        for user_name, no_of_games in self.games:
            res.append((user_name, no_of_games))
        return res


friends = [["shreya", "bob"],
           ["bob", "yang"],
           ["bob", "shreya"],
           ["yang", "shreya"],
           ["bob", "cecilia"],
           ["cecilia", "michael"],
           ["cecilia", "bob"]]

graph = FriendsGraph()
graph.add_friends(friends)
# graph.printFriends()
g = [("shreya", 5), ("bob", 4), ("yang", 3)]
graph.start_new_game(g)

# print(graph.all_games())

curr_online_players = graph.phase4(friends)
print(curr_online_players)

on_off_players1 = ("cecilia", "online")
print(graph.online_offline(on_off_players1, curr_online_players))

on_off_players2 = ("cecilia", "offline")
print(graph.online_offline(on_off_players2, curr_online_players))
