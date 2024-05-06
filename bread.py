# ROCK PAPER SCISSORS TOURNAMENT, DOUBLE ELIMINATION
import time
from random import randint


def singles(content):
    width = len(content)
    print("-" * width)
    print(content)
    print("-" * width)
    
    
def doubles(content):
    width = len(content)
    print("=" * width)
    print(content)
    print("=" * width)


def print_winner(player):
    doubles(f"{player.name} WINS!")
    time.sleep(1)
    singles(f"{player.win_quote}")
    time.sleep(1)
    
def print_rock(player):
    singles(f"{player.name} CHOOSES ROCK")
    time.sleep(1)

def print_paper(player):
    singles(f"{player.name} CHOOSES PAPER")
    time.sleep(1)

def print_scissors(player):
    singles(f"{player.name} CHOOSES SCISSORS")
    time.sleep(1)


def battle(p1, p2, winners_bracket, losers_bracket):
    doubles(f"{p1.name} VS {p2.name}")
    time.sleep(2)
    
    p1_move = int(p1.make_move())
    p2_move = int(p2.make_move())
    
    if p1_move == p2_move:
        doubles("DRAW")
        battle(p1, p2, winners_bracket, losers_bracket)
        
    if p1_move == 0 and p2_move == 1:
        print_rock(p1)
        print_paper(p2)
        time.sleep(1.5)
        print_winner(p2)
        losers_bracket.append(p1)
        winners_bracket.remove(p1)
    if p1_move == 0 and p2_move == 2:
        print_rock(p1)
        print_scissors(p2)
        time.sleep(1.5)
        print_winner(p1)
        losers_bracket.append(p2)
        winners_bracket.remove(p2)
        
    if p1_move == 1 and p2_move == 0:
        print_paper(p1)
        print_rock(p2)
        time.sleep(1.5)
        print_winner(p1)
        losers_bracket.append(p2)
        winners_bracket.remove(p2)
    if p1_move == 1 and p2_move == 2:
        print_paper(p1)
        print_scissors(p2)
        time.sleep(1.5)
        print_winner(p2)
        losers_bracket.append(p1)
        winners_bracket.remove(p1)
        
    if p1_move == 2 and p2_move == 1:
        print_scissors(p1)
        print_paper(p2)
        time.sleep(1.5)
        print_winner(p1)
        losers_bracket.append(p2)
        winners_bracket.remove(p2)
    if p1_move == 2 and p2_move == 0:
        print_scissors(p1)
        print_rock(p2)
        time.sleep(1.5)
        print_winner(p2)
        losers_bracket.append(p1)
        winners_bracket.remove(p1)
        
        
def losers_battle(p1, p2, losers_bracket):
    doubles(f"LOSERS BRACKET")
    time.sleep(2)
    
    doubles(f"{p1.name} VS {p2.name}")
    time.sleep(2)
    
    p1_move = int(p1.make_move())
    p2_move = int(p2.make_move())
    
    if p1_move == p2_move:
        doubles("DRAW")
        losers_battle(p1, p2, losers_bracket)
        
    if p1_move == 0 and p2_move == 1:
        print_rock(p1)
        print_paper(p2)
        time.sleep(1.5)
        print_winner(p2)
        losers_bracket.remove(p1)
    if p1_move == 0 and p2_move == 2:
        print_rock(p1)
        print_scissors(p2)
        time.sleep(1.5)
        print_winner(p1)
        losers_bracket.remove(p2)
        
    if p1_move == 1 and p2_move == 0:
        print_paper(p1)
        print_rock(p2)
        time.sleep(1.5)
        print_winner(p1)
        losers_bracket.remove(p2)
    if p1_move == 1 and p2_move == 2:
        print_paper(p1)
        print_scissors(p2)
        time.sleep(1.5)
        print_winner(p2)
        losers_bracket.remove(p1)
        
    if p1_move == 2 and p2_move == 1:
        print_scissors(p1)
        print_paper(p2)
        time.sleep(1.5)
        print_winner(p1)
        losers_bracket.remove(p2)
    if p1_move == 2 and p2_move == 0:
        print_scissors(p1)
        print_rock(p2)
        time.sleep(1.5)
        print_winner(p2)
        losers_bracket.remove(p1)


def final_battle(p1, p2, final_bracket):
    if p1.finals_score == 1:
        doubles(f"{p1.name} WINS THE TOURNAMENT")
        return
    if p2.finals_score == 2:
        doubles(f"{p2.name} WINS THE TOURNAMENT")
        return
    
    doubles("GRAND FINALS")
    
    print(f"{p1.name} SCORE: {p1.finals_score} - {p2.name} SCORE: {p2.finals_score}")
    time.sleep(2)
    
    singles(f"{p1.name} in winners bracket needs 1 win!")
    time.sleep(3)
    singles(f"{p2.name} must knock {p1.name} into losers bracket, then win again!")
    time.sleep(3)
    
    doubles(f"{p1.name} VS {p2.name}")
    time.sleep(2)
    
    p1_move = int(p1.make_move())
    p2_move = int(p2.make_move())
    
    if p1_move == p2_move:
        doubles("DRAW")
        final_battle(p1, p2, final_bracket)
        
    if p1_move == 0 and p2_move == 1:
        print_rock(p1)
        print_paper(p2)
        time.sleep(1.5)
        print_winner(p2)
        p2.finals_score += 1
        if p2.finals_score == 1:
            doubles(f"{p2.name} knocks {p1.name} into losers bracket!")
        if p2.finals_score == 2:
            doubles(f"{p2.name} WINS THE TOURNAMENT!")
    if p1_move == 0 and p2_move == 2:
        print_rock(p1)
        print_scissors(p2)
        time.sleep(1.5)
        print_winner(p1)
        p1.finals_score += 1
        doubles(f"{p1.name} WINS THE TOURNAMENT!")
        
    if p1_move == 1 and p2_move == 0:
        print_paper(p1)
        print_rock(p2)
        time.sleep(1.5)
        print_winner(p1)
        p1.finals_score += 1
        doubles(f"{p1.name} WINS THE TOURNAMENT!")
    if p1_move == 1 and p2_move == 2:
        print_paper(p1)
        print_scissors(p2)
        time.sleep(1.5)
        print_winner(p2)
        p2.finals_score += 1
        if p2.finals_score == 1:
            doubles(f"{p2.name} knocks {p1.name} into losers bracket!")
        if p2.finals_score == 2:
            doubles(f"{p2.name} WINS THE TOURNAMENT!")
        
    if p1_move == 2 and p2_move == 1:
        print_scissors(p1)
        print_paper(p2)
        time.sleep(1.5)
        print_winner(p1)
        p1.finals_score += 1
        doubles(f"{p1.name} WINS THE TOURNAMENT!")
    if p1_move == 2 and p2_move == 0:
        print_scissors(p1)
        print_rock(p2)
        time.sleep(1.5)
        print_winner(p2)
        p2.finals_score += 1
        if p2.finals_score == 1:
            doubles(f"{p2.name} knocks {p1.name} into losers bracket!")
        if p2.finals_score == 2:
            doubles(f"{p2.name} WINS THE TOURNAMENT!")
        
        
class Enemy:
    used_names = set()
    
    def __init__(self):
        self.names = ["Kermit The Frog", "Datboi", "Dale Gribble", "Demon Boots", "Grandmaster Lane", "Asznard The Lua Guy", "Asznard The C# Guy", "Asznard The Gopher", "Allan The Swordmaster", "Dave The Necromancer"]
        self.name = self.unique_name()
        self.win_quotes = ["That's how you guess bitch", "Get shit on mf", "HTML is not a programming language scrub", "Try aiming scrub", "All skill"]
        self.win_quote = self.win_quotes[randint(0, len(self.win_quotes)-1)]
        self.lose_quotes = ["You beginners luck", "Can't believe I lost to a scrub", "At least I don't *program* in HTML", "Lucky ass bitch"]
        self.lose_quote = self.lose_quotes[randint(0, len(self.lose_quotes)-1)]
        self.finals_score = 0
        
    def unique_name(self):
        name = self.names[randint(0, len(self.names)-1)]
        while name in Enemy.used_names:
            name = self.names[randint(0, len(self.names)-1)]
        Enemy.used_names.add(name)
        return name
        
    def make_move(self):
        return randint(0, 2)
        
        
class Player:
    def __init__(self):
        self.name = input("Enter Name: ")
        self.win_quotes = ["That's how you guess bitch", "Get shit on mf", "HTML is not a programming language scrub", "Try aiming scrub", "All skill"]
        self.win_quote = self.win_quotes[randint(0, len(self.win_quotes)-1)]
        self.lose_quotes = ["You beginners luck", "Can't believe I lost to a scrub", "At least I don't *program* in HTML", "Lucky ass bitch"]
        self.lose_quote = self.lose_quotes[randint(0, len(self.lose_quotes)-1)]
        self.finals_score = 0
        
    def make_move(self):
        move = input("r/p/s ")
        if move not in ["r", "p", "s"]:
            self.make_move()
        if move == "r":
            return 0
        if move == "p":
            return 1
        if move == "s":
            return 2


def main():
    winners_bracket = [Player(), Enemy(), Enemy(), Enemy()]
    
    for dude in winners_bracket:
        singles(f"{dude.name} ENTERS")
        time.sleep(1)
    
    losers_bracket = []
    grand_finals = []
    
    doubles("DOUBLE ELIMINATION R/P/S")
    time.sleep(2)
    
    while len(winners_bracket) != 1:
        if len(winners_bracket) == 4:
            battle(winners_bracket[0], winners_bracket[1], winners_bracket, losers_bracket)
        if len(winners_bracket) == 3:
            battle(winners_bracket[1], winners_bracket[2], winners_bracket, losers_bracket)
        if len(winners_bracket) == 2:
            battle(winners_bracket[0], winners_bracket[1], winners_bracket, losers_bracket)
        time.sleep(2.2)
    
    grand_finals.append(winners_bracket[0])
    
    while len(losers_bracket) != 1:
        losers_battle(losers_bracket[0], losers_bracket[1], losers_bracket)
        
    grand_finals.append(losers_bracket[0])
    
    while grand_finals[0].finals_score != 1 and grand_finals[1].finals_score != 2:
        final_battle(grand_finals[0], grand_finals[1], grand_finals)


main()
