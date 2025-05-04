'''
Subject: Cricket Book Game through Data Handling 2.O
Created By: Anup Kumar.
Date: 16-April-2025.
'''

import random

class Cricket:
    def __init__(self):
        self.player = 0
        self.balls = 0
        self.team_names = ["", ""]
        self.team_scores = [0, 0]

    def file_read(self):
        file.seek(0)  # Set pointer to the start
        file_content = file.read()  # Read file content
        print(file_content)  # Print file content
        file.seek(0, 2)  # Move pointer to the end

    def inning(self):
        print(f"{self.team_names[0]} Vs {self.team_names[1]} {over} Over Match\n")
        file.write(f"{self.team_names[0]} Vs {self.team_names[1]} {over} Over Match\n")
        for team in range(2):
            print("-" * 10)
            print(f"\nTeam: {self.team_names[team]}")
            file.write(f"\nTeam: {self.team_names[team]}\n")
            self.batting(0, 0, team)

    def get_winner(self):
        if self.team_scores[0] > self.team_scores[1]:
            score_difference = self.team_scores[0] - self.team_scores[1]
            print(f"\nWinner: {self.team_names[0]} by {score_difference} Runs")
            file.write(f"\nWinner: {self.team_names[0]} by {score_difference} Runs")
        elif self.team_scores[0] < self.team_scores[1]:
            score_difference = self.team_scores[1] - self.team_scores[0]
            print(f"\nWinner: {self.team_names[1]} by {score_difference} Runs")
            file.write(f"\nWinner: {self.team_names[1]} by {score_difference} Runs")
        else:
            print("\nMatch Draw")
            file.write("\nMatch Draw")

    def batting(self, ball, current_run, team):
        for players in range(1, self.player + 1):
            print("PLAYER =", players)
            player_run = 0
            while self.balls > ball and players <= self.player:
                random_integer = random.randint(0, 6)
                if random_integer > 0:
                    print("." * 10)
                    print("Ball =", ball + 1)
                    print(random_integer)
                    current_run += random_integer
                    player_run += random_integer
                    print("player_run", player_run)
                    ball += 1
                    input("Press any button to continue next ball: ")
                else:
                    ball += 1
                    print("Ball =", ball)
                    print("OUT!" * 4)
                    print(f"Player {players} Run {player_run}")
                    file.write(f"\nPlayer {players} Run {player_run}")
                    input("Press any button to continue next ball: ")
                    break  # Player out, move to next player
            else:
                print(f"\nPlayer {players} Run {player_run} (NOT OUT)")
                file.write(f"\nPlayer {players} Run {player_run} (NOT OUT)\n")

        self.team_scores[team] = current_run
        print(f"\nTotal Score = {current_run}")
        file.write(f"\nTotal Score = {current_run}\n")  # Write final score of the team

if __name__ == "__main__":
    try:
        file = open("make.txt \file\with\the\name\of\score_board\and\paste\the\file\location\like\this", "w+")  #Paste file location here

        new_match = Cricket()
        new_match.file_read()  # Read and print old data
        new_match.team_names[0] = input("Team 1: Enter your team name: ")
        new_match.team_names[1] = input("Team 2: Enter your team name: ")
        over = int(input("How many overs you want to play : "))
        new_match.player = int(input("How many players in team: "))
        if new_match.player > 10:
            print("Maximum 10 Player are allowed in One Team: ")

        else:
            new_match.balls = over * 6
            new_match.inning()
            new_match.get_winner()
            new_match.file_read()  # Print final result
            print("Match Highlight available on Score_Board.txt")

    except Exception as e:
        print(f"An error occurred: {e}")