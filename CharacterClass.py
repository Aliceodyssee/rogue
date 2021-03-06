class Character:
    def __init__(self, name, x, y):
        self.name = name
        self.vp=10 #Le personnage commence le jeu à 3 vies
        self.purse = 0
        self.listItems = []
        self.x = x
        self.y = y
      
    
    def add_item(self,item):
        self.listItems.append(item)

    def add_money(self, value, boolEarn):
        if boolEarn:
            self.purse += value
        else:
            self.purse -= value

    def add_pv(self, value, boolEarn):
        if self.vp < 15: #Le personage à 5 vies maximum
            if boolEarn:
                self.vp += value
            else:
                self.vp -= value
        else:
            if not(boolEarn):
                self.vp -= value
    
    def move(self,dx,dy):
        self.x += dx
        self.y += dy

class Item:
    def __init__(self, name, char):
        self.name= name
        self.char= char


