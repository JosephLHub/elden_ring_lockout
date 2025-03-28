# Elden Ring Lockout Bingo Randomiser

JSON generator for Elden Ring Lockout Bingo grids.

## Description

This program generates a JSON output for use in custom lockout bingo games on https://bingosync.com.

Upon running the .py file, you will be presented with a choice of 4 different formats for the lockout bingo, these are:
- Pre-Leyndell
- Entire Base Game
- DLC only
- Base Game + DLC

25 challenges are semi-randomly selected from a list of over 400. They are categorised by the formats they are applicable to, as well as by the rough objective of the challenge. (e.g. obtain a specific weapon)

You will also be presented with the choice to enable a 'Race Start' - this replaces the challenge at the centre of the 5x5 grid with a different challenge that is intended to be completed first. (the winner of the race receiving an early advantage)

After the program selects the challenges, it also outputs a list of in-game NPCs whose questlines the players should heed, lest they accidentally lock themselves out of completing a challenge. The program has a procedure in order to avoid conflicts that may result from this.

For further clarification, the Pre-Leyndell format includes the areas:
- Limgrave
- Weeping Peninsula
- Siofra River
- Liurnia
- Ainsel River
- Caelid
- Nokron
- Altus Plateau
- Shaded Castle
- Mt Gelmir
- Volcano Manor

but does not include the areas:

- Leyndell
- Subterranean Shunning Grounds
- Nokstella
- Lake of Rot
- Dragonbarrow
- Deeproot Depths
- Forbidden Lands
- Mountaintops of the Giants
- Consecrated Snowfields
- Mohgwyn Palace
- Miquella's Haligtree
- Farum Azula
- Ashen Capital

## Getting Started

### Dependencies

* Created on Python 3.10.9

### Executing program

* Should be as simple as running the following in a terminal:
```
python lockout_to_json.py
```
* Raise an issue if any arise.

## Planned Updates

* Challenges handling DLC NPC questlines
* Challenges handling other DLC-unique mechanics
* Challenges involving more DLC-base game interactions
* If you have suggestions for further challenges, raise an issue.

## Authors

JosephLHub

## Version History

* 1.0
    * Initial Release
