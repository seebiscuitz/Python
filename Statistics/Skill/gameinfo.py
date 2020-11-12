# gameinfo
class game:
    def __init__(self, initialmean):
        #initialmean = 25
        self.dp = 0.1
        self.beta = initialmean / 6
        self.stdv = initialmean / 3
        self.dyn = initialmean / 300
        return
    def printinfo(self):
        print(self.dp)
        return