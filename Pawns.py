


class pawn(object):
    def __init__(self, x, y, type_piece):
        self.x = x
        self.y = y
        self.type_piece = type_piece

    def list_of_moves(self):
        move_list=[]

        if self.type_piece=='B':
            move_list.append([self.x+1,self.y+1])
            move_list.append([self.x+1,self.y-1])
        if self.type_piece=='C':
            move_list.append([self.x-1,self.y+1])
            move_list.append([self.x-1,self.y-1])
        tmp_list=move_list
        for move in reversed(move_list):
            if 0 > move[0] or move[0] > 7 or 0 > move[1] or move[1] > 7:
                tmp_list.remove(move)
        return move_list

    def list_of_jumps(self):
        jump_list=[]
        if self.type_piece=='B':
            jump_list.append([self.x+2,self.y+2,self.x+1,self.y+1])
            jump_list.append([self.x+2,self.y-2,self.x+1,self.y-1])

        if self.type_piece=='C':
            jump_list.append([self.x-2,self.y+2,self.x-1,self.y+1])
            jump_list.append([self.x-2,self.y-2,self.x-1,self.y-1])

        tmp_list=jump_list

        for move in reversed(jump_list):
            if 0>move[0] or move[0]>7 or 0>move[1] or move[1]>7 :
                tmp_list.remove(move)

        return tmp_list

    def __repr__(self):
        return str(self.type_piece)


class Quin(pawn):
    def __init__(self,x,y,type_piece):
        super().__init__(x,y,type_piece)
    def list_of_moves(self):
        move_list=[]
        move_list.append([self.x+1,self.y+1])
        move_list.append([self.x+1,self.y-1])
        move_list.append([self.x-1,self.y+1])
        move_list.append([self.x-1,self.y-1])
        tmp_list=move_list
        for move in reversed(move_list):
            if 0 > move[0] or move[0] > 7 or 0 > move[1] or move[1] > 7:
                tmp_list.remove(move)

        return tmp_list

    def list_of_jumps(self):
        jump_list=[]
        jump_list.append([self.x + 2, self.y + 2,self.x+1,self.y+1])
        jump_list.append([self.x + 2, self.y - 2,self.x+1,self.y-1])
        jump_list.append([self.x - 2, self.y + 2,self.x-1,self.y+1])
        jump_list.append([self.x - 2, self.y - 2,self.x-1,self.y-1])

        tmp_list=jump_list
        for jump in reversed(jump_list):
            if 0 > jump[0] or jump[0] > 7 or 0 > jump[1] or jump[1] > 7:
                tmp_list.remove(jump)
        return tmp_list


