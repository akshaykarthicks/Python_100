# https://pypi.org/project/prettytable/

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Character", ["Naruto Uzumaki", "Sasuke Uchiha", "Sakura Haruno", "Kakashi Hatake", "Itachi Uchiha", "Jiraiya", "Gaara", "Rock Lee", "Hinata Hyuga", "Shikamaru Nara"])
table.add_column("Village", ["Leaf", "Leaf", "Leaf", "Leaf", "Leaf", "Leaf", "Sand", "Leaf", "Leaf", "Leaf"])
table.add_column("Rank", ["Hokage", "Rogue/Ally", "Jonin", "Hokage", "Akatsuki", "Sannin", "Kazekage", "Jonin", "Jonin", "Hokage"])
table.add_column("Specialty", ["Rasengan", "Sharingan", "Medical", "Copy Ninja", "Tsukuyomi", "Sage Mode", "Sand Control", "Taijutsu", "Byakugan", "Shadow"])
table.align = "l"


print(table)
 