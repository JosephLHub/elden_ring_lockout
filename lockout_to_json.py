import random

def filter_by_format(format):
    challenges = []
    f = open("lockout_challenges.txt", "r")
    
    for entry in f:
        if entry.endswith("\n"):
            entry = entry[:-1]
        
        challenge = entry.split(", ")

        if (format % 2 == 0 and int(challenge[2]) <= format) or (format % 2 == 1 and int(challenge[2]) == format): #Appropriately assigns challenge
            challenges.append([challenge[0], challenge[1]])
    f.close()

    g = open("collections.txt", "r")

    for entry in g:
        if entry.endswith("\n"):
            entry = entry[:-1]

        challenge = entry.split(", ")
        bounds = challenge[2:]
        for x in range(0, len(bounds), 3): #Ensures proper spacing
            if str(format) == bounds[x]:
                value = random.randint(int(bounds[x + 1]), int(bounds[x + 2])) #Generate random number for challenge
                desc = challenge[1].split(" ")
                desc.insert(1, str(value)) #Insert into the challenge string
                challenge[1] = ' '.join(desc)
                challenges.append([challenge[0], challenge[1]])
    return challenges

def filter_by_restriction(challenges):
    npcs = set({})
    restricted_list = []
    conflicts = []
    f = open("restrictions.txt")

    for entry in f: #Extract restrictions from file & format them
        if entry.endswith("\n"):
            entry = entry[:-1]
        restricted_list.append(entry.split(", "))

    random.shuffle(restricted_list)

    for challenge in restricted_list:
        if len(npcs.intersection(set(challenge[1:]))) > 0: #If any NPC is already in the set
            conflicts.append(challenge[0]) #Add to pool of conflicting challenge
        else:
            npcs = npcs.union(set(challenge[1:])) #Add NPCs to the set

    challenges = [x for x in challenges if x[1] not in conflicts] #Remove conflicts from challenge list
    return challenges, npcs

def limit_by_tag(challenges):
    temp = challenges.copy()
    new_challenges = []
    limits = {
        "Restricted Specific Boss": 4,
        "Specific Boss": 2,
        "Any Boss": 2,
        "Restricted Enemy": 1,
        "Enemy": 2,
        "Weapon": 4,
        "Armour": 2,
        "Talisman": 3,
        "Ash of War": 2,
        "Spell": 3,
        "Spirit Ashes": 2,
        "Misc": 2,
        "Quest": 2,
        "Item": 2,
        "Item Collection": 1,
        "Misc Collection": 1,
        "Weapon Collection": 1
    }

    while len(new_challenges) < 25:
        rand = random.randint(0, len(temp) - 1)
        new_challenges.append(temp[rand])
        limits[temp[rand][0]] -= 1 #Reduce the appropriate limit by 1

        if limits[temp[rand][0]] == 0:
            temp = [x for x in temp if x[0] != temp[rand][0]] #Remove all other challenges in the category
        else:
            temp.remove(temp[rand])
        
        if len(temp) == 0:
            print("list is under")
            challenges = [x for x in challenges if challenges[x] not in new_challenges]
            new_rand = random.randint(0, len(challenges) - 1)
            new_challenges.append(challenges[new_rand])
    return new_challenges

def resolve_alternatives(challenges):
    for x in range(len(challenges)) :
        if '/' in challenges[x][1]:
            options = challenges[x][1].split("/")
            challenges[x][1] = options[random.randint(0, 1)]
    return challenges

def main():
    format = 0
    values = [1, 2, 3, 4]
    while format not in values: #Repeatedly ask user until format is entered
        format = int(input("\nChoose format:\n1. Pre-Leyndell\n2. Entire Base Game\n3. DLC only\n4. Base Game + DLC\n"))
    
    race_start = "undecided"
    options = ["y", "n"]
    while race_start not in options: #Repeatedly ask user until race start is decided on, one way or the other
        race_start = input("\nEnable Race Start (mandatory first objective)?\nEnter 'y' or 'n': ")

    challenges = filter_by_format(format) #Ensure only challenges for selected format are included
    random.shuffle(challenges)
    challenges, npcs = filter_by_restriction(challenges) #Ensure challenges don't conflict with each other

    challenges = limit_by_tag(challenges) #Ensure only a certain number of challenges from each category can be selected

    challenges = resolve_alternatives(challenges) #Choose one from the options when challenges contain a '/'

    challenges = [x[1] for x in challenges] #Removes category, leaving only the challenge

    if race_start == "y":
        starts = []
        f = open("race_start.txt")
        for entry in f:
            if entry.endswith("\n"):
                entry = entry[:-1]
            starts.append(entry.split(", "))
        random.shuffle(starts)

        starts = [x for x in starts if (x[1] == "3" and format == 3) or (x[1] == "1" and format != 3)]

        if (format % 2 == 0 and int(starts[0][1]) <= format) or (format % 2 == 1 and int(starts[0][1]) == format): #Appropriately assigns challenge
            challenges[12] = starts[0][0]

    output = "["
    for challenge in challenges: #Ensure there are only 25 challenges (5x5 grid)
        output += "{"
        output += f"\"name\": \"{challenge}\""
        output += "}, "
    output = output[:-2]
    output += "]"
    print("Challenges: ")
    print(output)

    g = open("restrictions.txt")
    restrictions = []
    for entry in g:
        if entry.endswith("\n"):
            entry = entry[:-1]
        restrictions.append(entry.split(", "))
    restrictions = [x for x in restrictions if x[0] in challenges]
    npcs = {y[1] for y in restrictions if "!" not in y[1]}
        
    print("NPCs: ")
    print(npcs)
main()