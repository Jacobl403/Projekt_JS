


class pawn(object):
    def __init__(self, x, y, type_piece):
        self.x = x
        self.y = y
        self.type_piece = type_piece
        self.center=0


    def list_of_moves(self):
        move_list=[]
        if self.type_piece=='B':
            move_list.append((self.x+1,self.y+1))
            move_list.append((self.x+1,self.y-1))
        if self.type_piece=='C':
            move_list.append((self.x-1,self.y+1))
            move_list.append((self.x-1,self.y-1))
        return move_list
    def list_of_jumps(self):
        jump_list=[]
        if self.type_piece=='B':
            jump_list.append((self.x+2,self.y+2))
            jump_list.append((self.x+2,self.y-2))
        if self.type_piece=='C':
            jump_list.append((self.x-2,self.y+2))
            jump_list.append((self.x-2,self.y-2))
        return jump_list

    def __repr__(self):
        return str(self.type_piece)


class Quin(pawn):
    def __init__(self,x,y,type_piece):
        super().__init__(x,y,type_piece)
    def list_of_moves(self):
        move_list=[]
        move_list.append((self.x+1,self.y+1))
        move_list.append((self.x+1,self.y-1))
        move_list.append((self.x-1,self.y+1))
        move_list.append((self.x-1,self.y-1))
        return move_list

    def list_of_jumps(self):
        jump_list=[]
        jump_list.append((self.x + 2, self.y + 2))
        jump_list.append((self.x + 2, self.y - 2))
        jump_list.append((self.x - 2, self.y + 2))
        jump_list.append((self.x - 2, self.y - 2))
        return jump_list


