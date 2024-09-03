import random
class WumpusWorld:
    def __init__(self,size=4):
        self.size=size
        self.agent_pos=(0,0)
        self.wumpus_pos=None
        self.gold_pos=None
        self.pit_prob=0.2
        self.agent_direction=random.choice(['up', 'down', 'left', 'right']) 
        self.grid=[[None for _ in range(size)]for _ in range(size)]
    def initialize_grid(self):
        self.wumpus_pos=(random.randint(0,self.size-1),random.randint(0,self.size-1))
        while True:
            x,y=random.randint(0,self.size-1),random.randint(0,self.size-1)
            if (x,y)!=self.wumpus_pos:
                self.gold_pos=(x,y)
                break
        for i in range(self.size):
            for j in range(self.size):
                if (i,j)!=self.wumpus_pos and (i,j)!=self.gold_pos:
                    if random.random()<self.pit_prob:
                        self.grid[i][j]='P'
        self.agent_pos=(0,0)
    def is_valid(self,x,y):
        return 0<=x<self.size and 0<=y<self.size
    def move_forward(self):
        x,y=self.agent_pos
        if self.agent_direction=='up':
            x=x-1
        elif self.agent_direction == 'down':
            x += 1
        elif self.agent_direction == 'left':
            y -= 1
        elif self.agent_direction == 'right':
            y += 1
        if self.is_valid(x, y):
            self.agent_pos = (x, y)
            return True
        else:
            return False
    def direction(self):
        self.agent_direction=random.choice(['up', 'down', 'left', 'right'])
    def percieve(self):
        x,y=self.agent_pos
        percieve=[]
        if (x,y)==self.wumpus_pos:
            percieve.append('Stench')
        elif self.grid[x][y]=='P':
            percieve.append('Breeze')
        elif self.gold_pos==(x,y):
            percieve.append('Glitter')
        return percieve
    def display_percept(self, percept):
        print("Percept:", ", ".join(percept))
    def main(self):
        self.initialize_grid()
        while True:
            percept = self.percieve()
            self.display_percept(percept)
            if 'Glitter' in percept:
                print("Found gold! Agent has won!")
                break
            action = random.choice(['move', 'direction']) 
            if action == 'move':
                if self.move_forward():
                    print("Agent moves forward.")
                else:
                    print("Agent bumps into the wall.")
            elif action == 'direction': 
                self.direction()
                print("Agent changes direction.")
            if 'Stench' in percept:             
                print("There is a stench nearby!")
            if 'Breeze' in percept:
                print("There is a breeze nearby!")
if __name__ == "__main__":
    world = WumpusWorld()
    world.main()