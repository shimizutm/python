def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         O         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   "
            ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
