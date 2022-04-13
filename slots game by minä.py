import random
symbols = ["@", "#", "¤"]

while True:
    tokens = 100
    print("Tervetuloa slots peliin!")
    while tokens > 0:
        print("Sinulla on", tokens, "kolikkoa.")
        try:
            bet = int(input("Panoksen määrä "))
        except:
            print("Ole hyvä ja syötä kokonais määrä kolikkoja.")
            continue
        if bet > tokens:
            print("Ei tarpeeksi kolikoita.")    
        else:
                tokens -= bet
                sq_one = random.choice(symbols)
                sq_two = random.choice(symbols)
                sq_three = random.choice(symbols)
                
                print()
                
                print("I", random.choice(symbols), "I", random.choice(symbols), "I" ,random.choice(symbols), "I")
                print("-------------")
                
                print("I", sq_one, "I", sq_two, "I", sq_three, "I")
                print("-------------")
                
                print("I", random.choice(symbols), "I", random.choice(symbols), "I" ,random.choice(symbols), "I")
                print()
                
                if sq_one == sq_two and sq_two == sq_three:
                    amountwon = bet*2
                    print("Sinä voitit", amountwon, "kolikkoa!")
                    tokens += amountwon
                else:
                    print("Hävisit tälläkertaa.")
    print("Kolikkosi eivät riitä.")
    print()
    print("Kiitos kun pelasit!")
    print()
    print()
    print()
    print()
    print()
    print()
    pro_tips = ("***Jos sinulla alkaa mennä hermot lopeta pelaaminen hetkeksi!***", "      ***Kokeile ulkona käyntiä.***", "      ***Suosi happihyppelyä!***", "        ***Juo vettä!***", "     ***Oletko koukussa???***")
    print(random.choice(pro_tips))
    print("      **Hävisit aloita uusiksi.**")
    print()