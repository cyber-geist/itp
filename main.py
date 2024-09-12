def query(a, b):
    chars = list(["A", "B", "C", "D", "E"])
    print(a)
    response = ""
    for i in range(len(b)):
        response += f"{chars[i]}) {b[i]}\n"
    print(response)
    user = input("> ")
    if user.upper() in chars:
        return user.upper()
    elif user.upper() == "STOP":
        exit()
    else:
        return "QUERY ERROR"

print("You are a knight under king Demarcus Bartholomew James III and you have been charged with protecting the king's crown for 24 hours.\nUnbeknownst to him, the evil forces of the warlock smelvin have been commanded to steal the crown at any cost.\nRemember, if you fail, the king will not be happy, and you will likely face a very painful and very public execution.")
x = query("You arrive at the king's personal vault in the middle of the great forest, prepared to protect the crown, when you realize that it’s a little past midnight.\nYou’re tired, hungry, and scared.", ["Stay awake near the crown", "Take a nap", "Sneak into the forest to fill your canteen", "Go back to the castle for a snack"])
if x == "A":
    print("You have been awake for exactly 2 hours and 30 minutes when you hear a low growling outside, but once it hears you moving around in the vault, it runs away, and you can peacefully watch the crown for another hour and a half.")
    x = query("You’ve been watching the crown for 4 hours and you hear another strange noise outside.\nYou peer out of the vault but see nothing but the darkness of the forest.", ["Investigate the noise", "Stay inside", "Steal a sword from the armory"])
    if x == "A":
        print("As soon as you open the vault door, an orc jumps out of the darkness and eats you alive")
    elif x == "B":
        print("You hear more noises outside the door, but overall everything seems normal.")
        x = query("As you sit there, watching the crown, you hear more noises outside.\nIt sounds as if someone is trying to beat the door down with a club.", ["Stay exactly where you are", "Brace yourself against the door", "Take the crown and run through the underground passageway into the castle"])
        if x == "A":
            print("An orc breaks down the door, surprising you.\nThere's no time to react as he grabs you and eats you.")
        elif x == "B":
            print("You brace yourself against the door, but they’re just too strong.\nThey force the door open, sending you flying back against the wall.\nYou manage to rise, but you see the smiling face of an orc in the doorway.")
            x = query("For a moment, you and the orc just stare at each other.\nYou value your life, and the orc would surely kill you.\nBut if you lose that crown, the king will have you publicly executed.", ["Run away", "Reason with orc"])
            if x == "A":
                print("You attempt to run down the secret passageway back to the castle.\nYou hear the orc laugh behind you, but you’re not sure if it’s following.\nWhen you arrive at the castle, you feel an overwhelming sense of safety.\nYou did it.\nYou escaped.\nExcept the monster was able to find the secret passageway too.\nLater that night, it breaks into the castle, eating everyone, including you.")
            elif x == "B":
                print("You try to convince the orc that there’s nothing worth having in the vault.\n“Everything in here is fake” you say “all of this is for show, none of this is valuable” but the orc just shakes its head.\n“Lord Smelvin told me to come here and take the hat and eat anyone in my way.”\nThe orc obeys the instructions of his master and eats you on the spot.")
        elif x == "C":
            print("When you arrive at the castle, you feel an overwhelming sense of safety.\nYou did it.\nYou escaped.\nExcept the monster was able to find the secret passageway too.\nLater that night, it breaks into the castle, eating everyone, including you.")
    elif x == "C":
        print("You sneak back to the castle to grab a sword from the armory and when you get back, thankfully nothing has changed.")
        x = query("As you sit there, watching the crown, you hear more noises outside.\nIt sounds as if someone is trying to beat the door down with a club.", ["Stay exactly where you are", "Brace yourself against the door", "Take the crown and run through the underground passageway into the castle"])
        if x == "A":
            print("An orc breaks down the door, surprising you.\nThere's no time to react as he grabs you and eats you.")
        elif x == "B":
            print("You brace yourself against the door, but they’re just too strong.\nThey force the door open, sending you flying back against the wall.\nYou manage to rise, but you see the smiling face of an orc in the doorway.")
            x = query("For a moment, you and the orc just stare at each other.\nYou value your life, and the orc would surely kill you.\nBut if you lose that crown, the king will have you publicly executed.", ["Run away", "Reason with orc", "Fight orc"])
            if x == "A":
                print("You attempt to run down the secret passageway back to the castle.\nYou hear the orc laugh behind you, but you’re not sure if it’s following.\nWhen you arrive at the castle, you feel an overwhelming sense of safety.\nYou did it.\nYou escaped.\nExcept the monster was able to find the secret passageway too.\nLater that night, it breaks into the castle, eating everyone, including you.")
            elif x == "B":
                print("You try to convince the orc that there’s nothing worth having in the vault.\n“Everything in here is fake” you say “all of this is for show, none of this is valuable” but the orc just shakes its head.\n“Lord Smelvin told me to come here and take the hat and eat anyone in my way.”\nThe orc obeys the instructions of his master and eats you on the spot.")
            elif x == "C":
                print("You heft your sword, and you miraculously gain incredible sword skills.\nYou cut off the orc’s arms, and as it yells in pain, you chuckle heartily.\n“No orcs are taking this crown.”")
                x = query("With the orc now lying eviscerated at the entrance of the vault, you can finally calm down enough to think logically.\nIf the orc knew the crown was here, there’s no telling what else does too.", ["Set up defenses around vault", "Do nothing", "Let the king's personal guard know about the orc"])
                if x == "A":
                    print("You spend hours building trenches and spike traps around the vault\nBy the time you finish, you are very satisfied with your work.")
                    x = query("With the vault completely surrounded by traps and protections, you feel prepared enough to face anything that comes your way\nNow there’s only one choice left.", ["Head back to the castle with the crown", "Watch your handiwork take out all the monsters as they try to enter the vault"])
                    if x == "A":
                        print("You decide that no matter how amazing your traps are, there's no guarantee that they won’t get in, so you head back to the castle to present the king with his crown.")
                        print("You arrive at the castle to greet the king\nPleased with your ability to protect the crown through all of these shenanigans\nWhen you walk into the throne room, though, the king seems surprised to see you\n“How on earth are you still alive?” when you look at him, confused, he elaborates\n“This was designed to be a public execution! My middle name is smelvin, I sent the orcs! I stole the crown! It was all planned!” the king places his head in his palms and gives a heavy sigh\n“But I suppose if you managed to protect the crown through all of this, then you do actually have some worthwhile skills\nYou may live.” And with that, you are escorted out of the castle with nothing to show for your efforts but sleep deprivation and trust issues.")
                    elif x == "B":
                        print("You decide to stay in the vault, after all it would be a shame to spend so many hours on those traps just to have no one witness them go off.")
                        print("You’re peering out the window of the vault, waiting for the first orc to show up\nWhen you realize that it has been 24 hours, and that you are officially done protecting the crown\nYou are so overjoyed by this fact that you don’t notice the first trap going off\nYou let out a hearty chuckle\nThose orcs don’t stand a chance\nAn hour passes without another trap going off, which seems odd, so you decide to check the first trap\nWhen you peer into the spike pit, surprise turns to horror as you realize that the king himself has fallen in and died\nThere is only one option now\nRun away, and never return.")
                elif x == "B":
                    print("As you stare at the crown, you hear more rustling outside, but something tells you not to worry about it\nUnfortunately, that voice was completely incorrect and you are eaten alive by orcs.")
                elif x == "C":
                    print("You sprint back to the castle to find the king’s guard, but none of them believe you\n“You fought off an orc? Yeah right, and I’m the king of the land.” Feeling defeated, you return to the vault, bracing yourself for the last few hours of protecting the crown.")
                    x = query("When you arrive back at the vault\nYou realize that there will almost certainly be more monsters coming for the crown\nIf an orc was able to find it, something else surely will be able to as well\nNow only one choice remains.", ["Admit defeat and run away", "Arm yourself to fight"])
                    if x == "A":
                        print("You run down the secret passageway into the castle to return the king’s crown, which he accepts and thanks you for\nMaybe running away wasn’t such a bad idea, you think, as you settle down in the castle for the night\nBut unfortunately, the orcs did manage to breach the vault and find the secret passageway, which they follow back to the castle\nEveryone within the castle wall has been eaten by the orcs before the sun rises.")
                    elif x == "B":
                        print("You grab a sword and prepare to fight off whatever may try to come for the crown\nYou are determined not to let anything get past you\nYou wait for what feels like an eternity, when you hear the door start to open\nYou brace yourself for a fight, but it’s not an orc that walks through the door, it’s the king! In all the excitement, you didn't notice that your 24 hours were up\nThe king stops a few steps in front of you\n“Thank you for guarding the crown for all this time\nI was settling a disagreement with the warlock smelvin, and he has a particular disliking with my crown.” the king smiles\n“Come with me, I want to show you something.” you follow the king back to his throne room, where he sits in his throne, turns around, and pushes a button\nThe world swirls around you and you can barely hear the king say “ you were supposed to die protecting that crown” but the surprise doesn’t have time to register, as your memories of the past 24 hours are erased, and you are sent back in time.")
        elif x == "C":
            print("When you arrive at the castle, you feel an overwhelming sense of safety.\nYou did it.\nYou escaped.\nExcept the monster was able to find the secret passageway too.\nLater that night, it breaks into the castle, eating everyone, including you.")
elif x == "B":
    print("You have been asleep for exactly 2 hours and 30 minutes when an orc breaks into the kings vault and eats you alive.")
elif x == "C":
    print("Your throat burns as you sneak out of the kings vault into the forest in search of water, but you only make it 2 steps before an orc lunges out of the shadows and eats you alive.")
elif x == "D":
    print("You take the underground passage back to the castle in search of a snack, and lucky for you, someone left their blackberries out.\nOnce you’ve finished eating, you head back to the vault, but once you arrive, you find the door bashed in, and the crown missing.")
    x = query("With the crown gone and daybreak approaching, you must go after the crown or risk the king’s wrath.\nYou leave the king’s vault and immediately notice a path of broken branches to the left, and a trail to the right.", ["Follow the broken branches", "Follow the trail", "Charge into the forest like a maniac"])
    if x == "A":
        print("As you follow the trail of broken branches, you worry about how the king might execute you when he finds out his crown is missing, but you’re so distracted, you don’t notice the tripwire set across the path, which causes a giant log to fall on your head, killing you instantly.")
    elif x == "B":
        print("You follow the well traveled path for hours until you see the castle come into view.\nHow could you have forgotten that this was the trail back home? By the time you make it back to the vault, all traces of the broken branch path have vanished.")
        x = query("With all traces of the crown gone, there's nothing you can do to find it.", ["Wait until morning and beg for the king's mercy", "Try to make a new crown", "Try to leave town"])
        if x == "A":
            print("The king is furious when he finds out you lost his crown.\nHe immediately schedules your very public, very painful execution for later today.")
        elif x == "B":
            print("As you’re looking around for materials, you find a gold nugget, then two.\nYou have accidentally stumbled upon a field rich with gold.\nYou spend all night gathering gold nuggets and offer them and the location they were found to the king in place of his crown.\nThe king accepts your gift and lets you live, but you are no longer a night.")
        elif x == "C":
            print("You manage to grab your things and leave town before the king notices, but you can never return to your home again.")
    elif x == "C":
        print("As you charge into the forest, you miraculously come across an orc camp.\nRight there, on a log in the middle of the camp, is the king’s crown, but it’s surrounded by sleeping orcs.")
        x = query("Now that you have the crown in your sights again, you must get it back.\nBut you must be careful not to disturb the orcs", ["Run in and grab the crown before they wake up", "Try to sneak and steal the crown back", "Create an overly elaborate contraption to get the crown back without ever stepping foot into the camp"])
        if x == "A":
            print("You make it about halfway through the camp before an orc wakes up and eats you without a second thought.")
        elif x == "B":
            print("You sneak over to the crown and manage to grab it.\nYou’re 2 steps back into the forest when you accidentally step on a dry branch, creating a loud snap and waking the orcs from their sleep, so naturally, you run as fast as you can back to the vault.")
            x = query("You’re sprinting through the forest with the crown, branches tearing at your arms, orcs hot on your trail, when you come across a small cave and an open field.", ["Continue running through forest to vault", "Crawl into a cave", "Run across the open field"])
            if x == "A":
                print("You continue tearing through the forest until you eventually reach the vault.\nYou barely have time to close the door before the orcs catch up to you.\nAs soon as the door is closed, you can hear them trying to break it down.")
                x = query("With the orcs trying to break into the vault, your options are limited\nThere's only one way out of the vault, which is the pathway back to the castle\nWith 8 hours left, you must make a decision.", ["Sprint back to the castle with the crown", "Try to barricade the vault door"])
                if x == "A":
                    print("You sprint through the passageway as fast as you can\nWhen you arrive at the castle, you feel an overwhelming sense of safety\nYou did it\nYou escaped\nExcept the orcs were able to find the secret passageway too\nJust a few minutes after you arrive, they break into the castle, eating everyone, including you.")
                if x == "B":
                    print("You pile bags of gold in front of the door, hoping the extra weight will be enough to hold the orcs back\nAfter about 20 minutes, it seems like the orcs have given up\nThe bags held.")
                    x = query("Now that the orcs are gone, you have to make a choice\nThere are no defenses around the vault, and the orcs will surely come back.", ["Admit defeat and run away", "Arm yourself to fight"])
                    if x == "A":
                        print("You run down the secret passageway into the castle to return the king’s crown, which he accepts and thanks you for\nMaybe running away wasn’t such a bad idea, you think, as you settle down in the castle for the night\nBut unfortunately, the orcs did manage to breach the vault and find the secret passageway, which they follow back to the castle\nEveryone within the castle wall has been eaten by the orcs before the sun rises.")
                    elif x == "B":
                        print("You grab a sword and prepare to fight off whatever may try to come for the crown\nYou are determined not to let anything get past you\nYou wait for what feels like an eternity, when you hear the door start to open\nYou brace yourself for a fight, but it’s not an orc that walks through the door, it’s the king! In all the excitement, you didn't notice that your 24 hours were up\nThe king stops a few steps in front of you\n“Thank you for guarding the crown for all this time\nI was settling a disagreement with the warlock smelvin, and he has a particular disliking with my crown.” the king smiles\n“Come with me, I want to show you something.” you follow the king back to his throne room, where he sits in his throne, turns around, and pushes a button\nThe world swirls around you and you can barely hear the king say “ you were supposed to die protecting that crown” but the surprise doesn’t have time to register, as your memories of the past 24 hours are erased, and you are sent back in time.")
            elif x == "B":
                print("As you crawl into the dark, moist cave, the floor gives out under you and you fall into a massive cavern.\nAs you’re falling, you think to yourself, wow this is a beautiful cave, and then you hit the ground with lethal force.")
            elif x == "C":
                print("You attempt to sprint across the field in hopes of outrunning the orcs, but the forest was the only thing that was slowing them down and they catch up to you in seconds.\nYour death is slow and painful.")
        elif x == "C":
            print("You spend hours gathering branches and leaves in hopes of making a fishing rod, but before you can even begin construction, the orcs wake up and swarm you.")
print("GAME OVER")
