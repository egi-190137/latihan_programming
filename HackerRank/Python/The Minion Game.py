def minion_game(string):
    vowels = "AIUEO"
    scores = {
        "Kevin": 0,
        "Stuart": 0
    }
    for i in range(len(string)):
        if string[i] in vowels:
            scores["Kevin"] += len(string)-i
        else:
            scores["Stuart"] += len(string)-i
    
    if scores["Kevin"] > scores["Stuart"]:
        print(f"Kevin {scores['Kevin']}")
    elif scores["Kevin"] < scores["Stuart"]:
        print(f"Stuart {scores['Stuart']}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)