with open("input.txt", "r") as f:
    # with open("input.txt", "r") as f:
    scratchcards = [line.strip() for line in f]

# print(scratchcards)
totalpoints = 0

for card in scratchcards:
    # print(card)
    cardno = card.split(":")[0].split("Card ")[1]

    cardnumbers = card.split(":")[1].split("|")[0].strip().split(" ")
    cardnumbers = list(filter(None, cardnumbers))
    cardwinners = card.split(":")[1].split("|")[1].strip().split(" ")
    cardwinners = list(filter(None, cardwinners))

    # print(cardno)
    # print(cardnumbers)
    # print(cardwinners)

    wins = 0
    for cardnumber in cardnumbers:
        if cardnumber in cardwinners:
            wins = wins + 1
            print(f"{cardnumber} WINS")

    points = 0
    for i in range(wins):
        if points == 0:
            points = 1
        else:
            points = points * 2
    # print("Points", points)
    totalpoints = totalpoints + points
print(totalpoints)
