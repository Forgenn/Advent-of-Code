import os


def input(filename) -> list:
    with open(filename) as f:
        return f.read().splitlines() 


def solve1(filename):
    lines = input(filename)
    games = {}

    for line in lines:
        game_id = line.split(" ")[1][:-1]
        
        sets = line.partition(':')[2].split(";")




def main():
    print(solve1("input.txt"))

main()