class Player:
    person = ''
    win = 0
    loss = 0
    draw = 0

    def __init__(self, name):
        self.person = name

    def __str__(self):
        string = '{}'
        return string.format(self.person)

    def addwins(self):
        self.win = self.win + 1

    def addloss(self):
        self.loss = self.loss + 1

    def adddraw(self):
        self.draw = self.draw + 1

    def display(self):

        print(self.person, "Wins")
        print("wins", self.win)
        print("losses:", self.loss)
        print("draws:", self.draw)
        print()

    def reset(self):
        self.win = 0
        self.loss = 0
        self.draw = 0

    def percentwins(self):

        if self.win + self.loss + self.draw == 0:
            return 0

        else:

            self.winpercentage = round(((100 * self.win) / (self.win + self.draw + self.loss)), 2)
            t = self.winpercentage
            return t



class TicTacToe:


    def __init__(self):
        self.allplayers = []
        self.a = []


        return

    def menu(self):
        while True:
            print("Please select one of the following:","0. Exit Program", "1. Play New Game","2. Add new player","3. Display Leaderboard","4. Print Rules and Instructions", "5. Reset all player scores to zero",sep="\n")
            self.select = int(input())



            if self.select == 0:
                return






            elif self.select == 1:
                self.playgame()









            elif self.select == 2:
                self.addplayer()
            elif self.select == 3:
                self.leaderboard()


            elif self.select == 4:
                print("Instructions","Add at least two players to the game","Play Game","Choose Players","Choose size of Board",
                      "First player to get a full row or full ",
                      "column or diaganol wins", sep="\n")
            elif self.select == 5:
                self.reset()

    def playgame(self):
        if len(self.allplayers) >= 2:
            self.display_self()
        else:
            print("You must add 2 players to the game before you can play")
            return

        self.pickplayer()



        self.sizeboard()

        self.displayboard()
        self.toggleplayers()


    def reset(self):
        count = 0
        for self.gameboy in self.allplayers:
            p = self.allplayers[count]
            count = count + 1

            p.reset()
            p.display()

    def leaderboard(self):
        print("Leaderboard")
        s=[]
        count = 0
        for self.gameboy in self.allplayers:
            self.p = self.allplayers[count]
            count = count + 1
            tu = self.p.person, "percent wins:", self.p.percentwins()

            s.append(tu)

        t = sorted(s, key=lambda percent: percent[2], reverse=True)
        counting = 0

        for i in t:
            print (*i)
            counting = counting + 1
            if counting == 10:
                return

    def addplayer(self):

        while True:
            print("please input name of new player")
            r = input().capitalize()



            if r in self.a:
                print("2 players can't have the same name")
                continue

            self.a.append(r)










            self.allplayers.append(Player(r))



            self.display_self()
            print("would you like to input another player? 1. Yes 2. No")

            YN = int(input())
            if YN == 1:
                continue
            if YN == 2:
                break

    def all_players(self, name):

        self.allplayers.append(name)

    def display_self(self):
        print("players")
        v = 0
        for player in self.allplayers:
            v = v + 1
            print(v, ":", player)
        print()

    def pickplayer(self):
        print("pick player 1 (number near player)")

        self.player1 = (int(input()) - 1)

        print("player 1 is", self.allplayers[self.player1])
        print("pick player 2 (number near player)")

        self.player2 = (int(input()) - 1)
        if self.player2 == self.player1:
            print("player 2 cannot be the same player as player 1 please pick a new player")
            self.player2 = (int(input()) - 1)
        print("player 2 is", self.allplayers[self.player2])
        self.currentplayers = [self.allplayers[self.player1], self.allplayers[self.player2]]
        self.p1 = self.allplayers[self.player1]
        self.p2 = self.allplayers[self.player2]

    def sizeboard(self):
        print("please input size of board")
        self.n = int(input())
        self.board = []

        for i in range(self.n):
            self.board.append(["*"] * self.n)

    def displayboard(self):
        for i in (self.board):
            for j in i:
                print(j, end=" ")
            print()
        return self.board

    def makemove(self):
        try:


            self.coordinate1, self.coordinate2 = [int(x) for x in input("Enter two coordiantes (integers): ").split()]


            while self.coordinate1 <= 0 or self.coordinate2 <= 0:
                print("coordinates must be greater than 0")
                self.makemove()


            while self.board[self.coordinate1 - 1][self.coordinate2 - 1] == "x" or self.board[self.coordinate1 - 1][self.coordinate2 - 1] == "o":
                print("Spot Taken Input New Coordinates")
                self.makemove()
        except:

            print("out of bounds input new coordinates")
            self.makemove()

    def toggleplayers(self):

        for i in range((self.n * self.n)):
            if i % 2 == 0:
                print(self.allplayers[self.player1], "it's Your turn please input coordinates")
                self.makemove()
                self.board[self.coordinate1 - 1][self.coordinate2 - 1] = "x"
                g = 0

                while True:
                    ok = 0

                    for i in range(self.n):

                        if self.board[g][i] == "x":
                            ok = ok + 1
                        if ok == self.n:
                            print(self.allplayers[self.player1], "Wins")

                            self.displayboard()

                            self.p1.addwins()
                            self.p2.addloss()

                            self.p1.display()
                            self.p2.display()

                            return

                    g = g + 1
                    if g >= self.n:
                        break
                rock = 0
                while True:
                    smile = 0

                    for i in range(self.n):

                        if self.board[i][rock] == "x":
                            smile = smile + 1
                        if smile == self.n:
                            print(self.allplayers[self.player1], "Wins")
                            self.displayboard()
                            self.p1.addwins()
                            self.p2.addloss()

                            self.p1.display()
                            self.p2.display()
                            return
                    rock = rock + 1
                    if rock >= self.n:
                        break
                smiles = 0

                for i in range(self.n):

                    if self.board[i][i] == "x":
                        smiles = smiles + 1
                    if smiles == self.n:
                        print(self.allplayers[self.player1], "Wins")
                        self.displayboard()
                        self.p1.addwins()
                        self.p2.addloss()

                        self.p1.display()
                        self.p2.display()
                        return
                kid = 0
                pup = self.n

                for i in range(self.n):

                    if self.board[i][pup - 1] == "x":
                        pup = pup - 1
                        kid = kid + 1
                    if kid == self.n:
                        print(self.allplayers[self.player1], "Wins")
                        self.displayboard()
                        self.p1.addwins()
                        self.p2.addloss()

                        self.p1.display()
                        self.p2.display()
                        return

                self.displayboard()
            elif i % 2 == 1:
                print(self.allplayers[self.player2], "it's Your turn please input coordinates")
                self.makemove()
                self.board[self.coordinate1 - 1][self.coordinate2 - 1] = "o"
                g = 0
                while True:
                    ok = 0

                    for i in range(self.n):

                        if self.board[g][i] == "o":
                            ok = ok + 1
                        if ok == self.n:
                            print(self.allplayers[self.player2], "Wins")
                            self.displayboard()
                            self.p2.addwins()
                            self.p1.addloss()

                            self.p1.display()
                            self.p2.display()
                            return
                    g = g + 1
                    if g >= self.n:
                        break
                rock = 0
                while True:
                    smile = 0

                    for i in range(self.n):

                        if self.board[i][rock] == "o":
                            smile = smile + 1
                        if smile == self.n:
                            print(self.allplayers[self.player2], "Wins")
                            self.displayboard()
                            self.p2.addwins()
                            self.p1.addloss()

                            self.p1.display()
                            self.p2.display()
                            return
                    rock = rock + 1
                    if rock >= self.n:
                        break
                smiles = 0

                for i in range(self.n):

                    if self.board[i][i] == "o":
                        smiles = smiles + 1
                    if smiles == self.n:
                        print(self.allplayers[self.player2], "Wins")
                        self.displayboard()
                        self.p2.addwins()
                        self.p1.addloss()

                        self.p1.display()
                        self.p2.display()
                        return

                kid = 0
                pup = self.n
                for i in range(self.n):

                    if self.board[i][pup - 1] == "o":
                        pup = pup - 1
                        kid = kid + 1
                    if kid == self.n:
                        print(self.allplayers[self.player2], "Wins")
                        self.displayboard()
                        self.p2.addwins()
                        self.p1.addloss()

                        self.p1.display()
                        self.p2.display()

                        return

                self.displayboard()

        print("draw")

        self.p1.adddraw()
        self.p2.adddraw()
        self.p1.display()
        self.p2.display()


menu = TicTacToe()
menu.menu()



