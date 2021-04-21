import random


def display():
    print("What would you like to do? \n")
    print("1. Play again?")
    print("2. View Statistics")
    print("3. Quit \n")
    gc = int(input("Enter Choice: "))
    return gc


def load():
    n = input("Enter your name: ")
    try:
        f = open(n+".rps", "r")
        data = {"name": "", "wins": 0, "loss": 0, "tie": 0}
        i = 0
        for line in f:
            if i == 0:
                data['name'] = line.strip()
            elif i == 1:
                data['wins'] = int(line)
            elif i == 2:
                data['loss'] = int(line)
            elif i == 3:
                data['tie'] = int(line)
            i = i+1
        return data
    except:
        print("Hello "+n + "your game file is not found")
        data = load()
        return data


def quit(d):
    f = open(d["name"]+".rps", "w")
    f.write(d['name']+"\n"+str(d['wins'])+"\n" +
            str(d['loss'])+"\n"+str(d['tie']))
    f.close
    print(d['name']+", your game has been saved.")


def view(n, d):
    print(d['name']+", here are your game statistics ->")
    print("Wins: "+str(d['wins']))
    print("Losses: "+str(d['loss']))
    print("Ties: "+str(d['tie']))
    if d['loss'] == 0:
        print("\nWins/Loss Ratio: 0")
    else:
        print("\nWin/loss Ratio: " + str(round(d['wins']/d['loss'], 2)))

    gc = display()
    if gc == 1:
        play_game(n+1, d)
    elif gc == 2:
        view(n, d)
    elif gc == 3:
        quit(d)
    else:
        print("Enter valid entry")
        view(n, d)


def check(x):
    if x == 1:
        return "Rock"
    elif x == 2:
        return "Paper"
    elif x == 3:
        return "Scissors"


def win(u, c):
    if u == 1 and c == 2:
        return "c"
    elif u == 1 and c == 3:
        return "u"
    elif u == 2 and c == 1:
        return "u"
    elif u == 2 and c == 3:
        return "c"
    elif u == 3 and c == 1:
        return "c"
    elif u == 3 and c == 2:
        return "u"
    else:
        return "tie"


def play_game(n, data):
    print("Round "+str(n))
    print("\n1. Rock")
    print("\n2. Paper")
    print("\n3. Scissors\n")
    choice = int(input("What do you pick? "))
    if choice <= 3 and choice >= 1:
        comp = random.randint(1, 3)
        s = win(choice, comp)
        if s == "u":
            print("You chose " + check(choice) +
                  ". The computer chose " + check(comp) + ". You Win!")
            data['wins'] = data['wins']+1
        elif s == "c":
            print("You chose " + check(choice) +
                  ". The computer chose " + check(comp) + ". You loose!")
            data['loss'] = data['loss']+1
        elif s == "tie":
            print("You chose " + check(choice) +
                  ". The computer chose " + check(comp) + ". The Game Tied!")
            data['tie'] = data['tie']+1
    else:
        print("Please enter a number that is in the range of 1 to 3")
        play_game(n, data)
    gc = display()
    if gc == 1:
        play_game(n+1, data)
    elif gc == 2:
        view(n, data)
    elif gc == 3:
        quit(data)
    else:
        print("Enter a valid coice Please!")


def new_game():
    name = input("What is your name? ")
    print("Hello "+name + " Lets Play!")
    data = {"name": name, "wins": 0, "loss": 0, "tie": 0}
    play_game(1, data)


print("Welcome to Rock, Paper Scissors\n")
print("1. Start New Game")
print("2. Load Game")
print("3. Quit\n")
game_choice = int(input("Please enter choice:"))

if game_choice == 1:
    new_game()
elif game_choice == 2:
    data = load()
    print("Welcome back, "+data['name'] + " lets play again!")
    n = data['wins']+ data['loss']+ data['tie']
    gc = display()
    if gc == 1:
        play_game(n+1,data)
    elif gc == 2:
        view(n,data)
    elif gc == 3:
        quit(data)
    else:
        print("Please Enter a valid choice!")