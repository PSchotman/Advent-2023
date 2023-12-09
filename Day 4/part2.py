with open("input.txt", "r") as f:
    # with open("input.txt", "r") as f:
    scratchcards = [line.strip() for line in f]

# print(scratchcards)
cardresults = {}

# Prepare set
for card in scratchcards:
    cardno = int(card.split(":")[0].split("Card ")[1])
    cardresults[cardno] = {"cardno": cardno, "amount": 1, "wins": 0}


# Process wins, process card amounts
for card in scratchcards:
    # print(card)
    cardno = int(card.split(":")[0].split("Card ")[1])
    cardnumbers = card.split(":")[1].split("|")[0].strip().split(" ")
    cardnumbers = list(filter(None, cardnumbers))
    cardwinners = card.split(":")[1].split("|")[1].strip().split(" ")
    cardwinners = list(filter(None, cardwinners))

    # print(cardno)
    # print(cardnumbers)
    # print(cardwinners)

    wins = 0
    # foreach number in scratchcard
    for cardnumber in cardnumbers:
        # check for winner
        if cardnumber in cardwinners:
            # print(f"card:{cardno} - {cardnumber} WINS")
            wins = wins + 1
            # update relevant card
            cardresults[cardno]["wins"] = wins
            # print("...")

    # Process each of the duplicates
    for i in range(cardresults[cardno]["amount"]):
        # Go over the wins
        for winloop in range(cardresults[cardno]["wins"]):
            winloop = winloop + 1
            # Update the corresponding card
            cardresults[cardno + winloop]["amount"] = (
                cardresults[cardno + winloop]["amount"] + 1
            )


totalcards = 0
for cardno, card in cardresults.items():
    print(card)
    totalcards = totalcards + card["amount"]

print("TOTAL CARDS: ", totalcards)
