if __name__ == "__main__":
    items = [["Soda (2)","Water (1)","Juice (2)"],["Chocolate (5)","Chips (4)","Fruit bar (3)"]]
    cost = [[2,1,2],[5,4,3]]
    print ("--Vending Machine--")
    for row in items:
        print (row)
    
    successful = False
    while successful == False:
        try:
            coins = int(input("Insert coins (1s, 2s or 5s only. Input non-number to end transaction) "))
            while coins != 1 and coins != 2 and coins != 5:
                print ("Coin not recognised")
                coins = int(input("Insert coin (1s, 2s or 5s only. Input non-number to end transaction) "))
            itemrow = int(input("Select row (1 or 2). "))
            while itemrow != 1 and itemrow != 2:
                itemrow = int(input("Select row (1 or 2). "))
            item = int(input("Which item? (1-3)" ))
            while item != 1 and item != 2 and item != 3:
                item = int(input("Which item? (1-3) "))
            total = cost[itemrow-1][item-1]
            print (f"Selected: {items[itemrow-1][item-1]}, Cost: {total}")
            print (f"Balance: {coins}")
            if coins > total:
                print (f"Transaction successful. Change given: {coins-total}")
            elif coins == total:
                print ("Transaction successful. No change given")
            else:
                print ("Transaction failed. Not enough coins")
            successful = True

        except:
            print ("Ending transaction.")
            successful = True
