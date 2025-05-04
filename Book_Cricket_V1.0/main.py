'''
Subject: Cricket Book Game through Data Handling
Created By: Anup Kumar.
Date: 14-April-2025.
'''

import random

class cricket:
    def __init__(self):
        pass

    def file_read(self):
        file.seek(0)  # Pointer will set on Zero
        file_content = file.read()  # Read the file content
        print(file_content)  # print the file content
        file.seek(0, 2)  # Moving the pointer from first position to the last position. (2 for end of the file)

    def inning(self):
        file.write(f"{team_1} Vs {team_2} {over} Over Match\n")
        for team in range(1, 2):
            print("-" * 10)
            print(team_1)
            file.write(f"\nTeam: {team_1}")
            self.batting(0,0)
        for team in range(1, 2):
            print("-" * 10)
            print(team_2)
            file.write(f"\n\nTeam: {team_2}")
            self.batting(0, 0)

    def batting(self, ball, current_run):
        if True:
            for players in range(1, player + 1):
                print("PLAYER = ",players)
                player_run = 0
                while (balls > ball):
                    while True:
                        random_integer = random.randint(0, 6)
                        if random_integer > 0:
                            print("." * 10)
                            print("Ball = ", ball + 1)
                            print(random_integer)
                            current_run = current_run + random_integer
                            player_run = player_run + random_integer
                            print("player_run", player_run)
                            ball = ball + 1
                            input("press any button to continue next ball: ")
                        else:
                            print("Ball = ", ball + 1)
                            print("out" * 4)
                            print("Player", players, "Run", player_run)
                            file.write(f"\nPlayer: {players},Run:{player_run}")
                            players = players + 1
                            ball = ball + 1
                            player_run = 0
                            input("press any button to continue next ball: ")
                        break
                file.write(f"\nPlayer: {players},Run:{player_run},(NOTOUT)")
                break
        file.write(f"\nTotal Score = {current_run}")#write in text file final score of the team
        return current_run

if __name__ == "__main__":
    try:
        file = open("make.txt \file\with\the\name\of\score_board\and\paste\the\file\location\like\this","w+")#text file location

        new_match = cricket()

        new_match.file_read() #for old data read and set pointer and print old data

        team_1 = input("Team 1 : Enter your team name: ")
        team_2 = input("Team 2 : Enter your team name: ")
        over = int(input("How many overs you want to play(choose overs between 1 to 5): "))
        player = int(input("How many players in team(input value should be less then or equal to 10 and not be 0): "))
        balls = over * 6

        new_match.inning()


        new_match.file_read()#Print Final Result

    except:
        pass
    finally:
        print("Programe Run Successfull")#Print "Programe Run Successfull" after the programe executed successfully
