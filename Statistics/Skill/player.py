class player:
    def __init__(self, id):
        # givens
        self.id = id
        # default trueskill values used for xbox live
        self.mean = 25.000
        self.stdv = self.mean / 6
        self.win = 0
        self.loss = 0
        self.gamesplayed = 0
        self.meanhist = [self.mean]
        self.stdvhist = [self.stdv]
        self.wlr = 0
        #self.fide = 0
        #self.uscf = 800

    def update(self, wld, newMean, newStdv):
        # assumed win = 1, loss = -1, draw => 0
        if wld==1:
            self.win += 1
        elif wld==-1:
            self.loss += 1
        else:
            self.draw += 1
        self.gamesplayed += 1
        if not(self.win==0 or self.loss==0):
            self.wlr = self.win/(self.loss + self.gamesplayed)
        # update skill
        self.mean = newMean
        self.stdv = newStdv
        self.meanhist.append(newMean)
        self.stdvhist.append(newStdv)
        return
    
    def get_wins(self):
        return self.win

    def get_loss(self):
        return self.loss

    def get_rating(self):
        return [self.mean, self.stdv] 
