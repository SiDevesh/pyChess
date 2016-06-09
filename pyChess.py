#!/usr/bin/python
#--chess board class with
class ChessBoard:
	width = 8
	height = 8

	def __init__(self,height=8,width=8):
		#print 'init test'
		assert (((width<8)or(height<5)) == False),"Insufficient board size for chess"
		self.width = width
		self.height = height
		self.board_matrix = [[None for x in range(width)] for y in range(height)]
		self.deadpool = [None for x in range((width)*(height))]
		#Representation of pieces:
		#  PW-Pawn White
		#  KW-King White
		#  QW-Queen White
		#  BW-Bishop White
		#  NW-Knight White
		#  RW-Rook White
		#
		#  PB-Pawn Black
		#  KB-King Black
		#  QB-Queen Black
		#  BB-Bishop Black
		#  NB-Knight Black
		#  RB-Rook Black

		pc_pawn pawnW1
		pc_pawn pawnW2
		pc_pawn pawnW3
		pc_pawn pawnW4
		pc_pawn pawnW5
		pc_pawn pawnW6
		pc_pawn pawnW7
		pc_pawn pawnW8

		pc_rook rookW1
		pc_rook rookW2

		pc_bishop bishopW1
		pc_bishop bishopW2

		pc_knight knightW1
		pc_knight knightW2

		pc_king kingW

		pc_queen queenW

		pc_pawn pawnB1
		pc_pawn pawnB2
		pc_pawn pawnB3
		pc_pawn pawnB4
		pc_pawn pawnB5
		pc_pawn pawnB6
		pc_pawn pawnB7
		pc_pawn pawnB8

		pc_rook rookB1
		pc_rook rookB2

		pc_bishop bishopB1
		pc_bishop bishopB2

		pc_knight knightB1
		pc_knight knightB2

		pc_king kingB
					
		pc_queen queenB

		#print_ordered_pieces = [{'role':'R', 'color':'B'}, {'role':'K', 'color':'B'}, {'role':'B', 'color':'B'}, {'role':'Q', 'color':'B'}, {'role':'K', 'color':'B'}, {'role':'B', 'color':'B'}, {'role':'K', 'color':'B'}, {'role':'R', 'color':'B'}, {'role':'P', 'color':'B'}, {'role':'P', 'color':'B'}, {'role':'P', 'color':'B'}, {'role':'P', 'color':'B'}, {'role':'P', 'color':'B'}, {'role':'P', 'color':'B'}, {'role':'P', 'color':'B'}, {'role':'P', 'color':'B'}, {'role':'P', 'color':'W'}, {'role':'P', 'color':'W'}, {'role':'P', 'color':'W'}, {'role':'P', 'color':'W'}, {'role':'P', 'color':'W'}, {'role':'P', 'color':'W'}, {'role':'P', 'color':'W'}, {'role':'P', 'color':'W'}, {'role':'R', 'color':'W'}, {'role':'K', 'color':'W'}, {'role':'B', 'color':'W'}, {'role':'Q', 'color':'B'}, {'role':'K', 'color':'W'}, {'role':'B', 'color':'W'}, {'role':'K', 'color':'W'}, {'role':'R', 'color':'W'} ]
		print_ordered_pieces = [rookB2, knightB2, bishopB2, queenB, kingB, bishopB1, knightB1, rookB1, pawnB8, pawnB7, pawnB6, pawnB5, pawnB4, pawnB3, pawnB2, pawnB1,  pawnW1, pawnW2, pawnW3, pawnW4, pawnW5, pawnW6, pawnW7, pawnW1, rookW1, knightW1, bishopW1, queenW, kingW, bishopW2, knightW2, rookW2 ]
		pc_i = 0
		for i in range(height):
			for j in range(width):
				if((i<2)or(i>=(height-2))):
					#if width of board is more than 8, extra spaces are put empty on left
					
					if(j<8):
						self.board_matrix[i][j] = print_ordered_pieces[pc_i]
						pc_i+=1	
					else:
						self.board_matrix[i][j] = {'role':'E', 'color':'E'}
				else:
					self.board_matrix[i][j] = {'role':'E', 'color':'E'}

	def board_print(self):
		for i in range(self.height):
			for j in range(self.width):
				print self.board_matrix[i][j].symbol

class pc_rook:
	symbol = 'R'
	name = 'rook'
	info = 'can only move in straight lines, upto any distance, can\'t jump over pieces'
	def moves_pos(self, board, pos, color):
		moves_ret = []

		adder = 1
		while (((pos['x']+adder)<board.width)or(board.board_matrix[pos['x'+adder]][pos['y']]['color']!=color)):
			moves_ret.append({'x':pos['x']+adder, 'y':pos['y']})
			if(board.board_matrix[pos['x']+adder][pos['y']]['color']!='E'):
				break
			adder+=1
		
		adder = 1
		while (((pos['x']-adder)>=0)or(board.board_matrix[pos['x'-adder]][pos['y']]['color']!=color)):
			moves_ret.append({'x':pos['x']-adder, 'y':pos['y']})
			if(board.board_matrix[pos['x']-adder][pos['y']]['color']!='E'):
				break
			adder+=1
		
		adder = 1
		while (((pos['y']+adder)<board.height)or(board.board_matrix[pos['x']][pos['y']+adder]['color']!=color)):
			moves_ret.append({'x':pos['x'], 'y':pos['y']+adder})
			if(board.board_matrix[pos['x']][pos['y']+adder]['color']!='E'):
				break
			adder+=1
		
		adder = 1
		while (((pos['y']-adder)>=0)or(board.board_matrix[pos['x']][pos['y']-adder]['color']!=color)):
			moves_ret.append({'x':pos['x'], 'y':pos['y']-adder})
			if(board.board_matrix[pos['x']][pos['y']-adder]['color']!='E'):
				break
			adder+=1
		
		return moves_ret

class pc_bishop:
	symbol = 'R'
	name = 'bishop'
	info = 'can only move in diagonals, upto any distance, can\'t jump over pieces'
	def moves_pos(self, board, pos, color):
		moves_ret = []

		adder = 1
		while (((pos['x']+adder)<board.width)or((pos['y']+adder)<board.height)or(board.board_matrix[pos['x']+adder][pos['y']+adder]['color']!=color)):
			moves_ret.append({'x':pos['x']+adder, 'y':pos['y']+adder})
			if(board.board_matrix[pos['x']+adder][pos['y']+adder]['color']!='E'):
				break
			adder+=1

		adder = 1
		while (((pos['x']+adder)<board.width)or((pos['y']-adder)>=0)or(board.board_matrix[pos['x']+adder][pos['y']-adder]['color']!=color)):
			moves_ret.append({'x':pos['x']+adder, 'y':pos['y']-adder})
			if(board.board_matrix[pos['x']+adder][pos['y']-adder]['color']!='E'):
				break
			adder+=1

		adder = 1
		while (((pos['x']-adder)>=0)or((pos['y']-adder)>=0)or(board.board_matrix[pos['x']-adder][pos['y']-adder]['color']!=color)):
			moves_ret.append({'x':pos['x']-adder, 'y':pos['y']-adder})
			if(board.board_matrix[pos['x']-adder][pos['y']-adder]['color']!='E'):
				break
			adder+=1

		adder = 1
		while (((pos['x']-adder)>=0)or((pos['y']+adder)<board.height)or(board.board_matrix[pos['x']-adder][pos['y']+adder]['color']!=color)):
			moves_ret.append({'x':pos['x']-adder, 'y':pos['y']+adder})
			if(board.board_matrix[pos['x']-adder][pos['y']+adder]['color']!='E'):
				break
			adder+=1

		return moves_ret


class pc_queen:
	symbol = 'Q'
	name = 'queen'
	info = 'has move set of both rook and bishop'
	def moves_pos(self, board, pos, color):
		moves_ret = []
		def moves_pos_bishop(self, board, pos, color):
			moves_ret = []

			adder = 1
			while (((pos['x']+adder)<board.width)or((pos['y']+adder)<board.height)or(board.board_matrix[pos['x']+adder][pos['y']+adder]['color']!=color)):
				moves_ret.append({'x':pos['x']+adder, 'y':pos['y']+adder})
				if(board.board_matrix[pos['x']+adder][pos['y']+adder]['color']!='E'):
					break
				adder+=1

			adder = 1
			while (((pos['x']+adder)<board.width)or((pos['y']-adder)>=0)or(board.board_matrix[pos['x']+adder][pos['y']-adder]['color']!=color)):
				moves_ret.append({'x':pos['x']+adder, 'y':pos['y']-adder})
				if(board.board_matrix[pos['x']+adder][pos['y']-adder]['color']!='E'):
					break
				adder+=1

			adder = 1
			while (((pos['x']-adder)>=0)or((pos['y']-adder)>=0)or(board.board_matrix[pos['x']-adder][pos['y']-adder]['color']!=color)):
				moves_ret.append({'x':pos['x']-adder, 'y':pos['y']-adder})
				if(board.board_matrix[pos['x']-adder][pos['y']-adder]['color']!='E'):
					break
				adder+=1

			adder = 1
			while (((pos['x']-adder)>=0)or((pos['y']+adder)<board.height)or(board.board_matrix[pos['x']-adder][pos['y']+adder]['color']!=color)):
				moves_ret.append({'x':pos['x']-adder, 'y':pos['y']+adder})
				if(board.board_matrix[pos['x']-adder][pos['y']+adder]['color']!='E'):
					break
				adder+=1

			return moves_ret


		def moves_pos_rook(self, board, pos, color):
			moves_ret = []

			adder = 1
			while (((pos['x']+adder)<board.width)or(board.board_matrix[pos['x'+adder]][pos['y']]['color']!=color)):
				moves_ret.append({'x':pos['x']+adder, 'y':pos['y']})
				if(board.board_matrix[pos['x']+adder][pos['y']]['color']!='E'):
					break
				adder+=1
			
			adder = 1
			while (((pos['x']-adder)>=0)or(board.board_matrix[pos['x'-adder]][pos['y']]['color']!=color)):
				moves_ret.append({'x':pos['x']-adder, 'y':pos['y']})
				if(board.board_matrix[pos['x']-adder][pos['y']]['color']!='E'):
					break
				adder+=1
			
			adder = 1
			while (((pos['y']+adder)<board.height)or(board.board_matrix[pos['x']][pos['y']+adder]['color']!=color)):
				moves_ret.append({'x':pos['x'], 'y':pos['y']+adder})
				if(board.board_matrix[pos['x']][pos['y']+adder]['color']!='E'):
					break
				adder+=1
			
			adder = 1
			while (((pos['y']-adder)>=0)or(board.board_matrix[pos['x']][pos['y']-adder]['color']!=color)):
				moves_ret.append({'x':pos['x'], 'y':pos['y']-adder})
				if(board.board_matrix[pos['x']][pos['y']-adder]['color']!='E'):
					break
				adder+=1
			
			return moves_ret

		moves_ret = moves_pos_rook(board, pos, color)
		moves_ret.extend(moves_pos_bishop(board, pos, color))

		return moves_ret


class pc_king:
	symbol = 'K'
	name = 'king'
	info = 'same moveset as queen but all are limited to one step'
	def moves_pos(self, board, pos, color):
		moves_ret = []
		def moves_pos_bishop_one(self, board, pos, color):
			moves_ret = []

			adder = 1
			if (((pos['x']+adder)<board.width)or((pos['y']+adder)<board.height)or(board.board_matrix[pos['x']+adder][pos['y']+adder]['color']!=color)):
				moves_ret.append({'x':pos['x']+adder, 'y':pos['y']+adder})

			adder = 1
			if (((pos['x']+adder)<board.width)or((pos['y']-adder)>=0)or(board.board_matrix[pos['x']+adder][pos['y']-adder]['color']!=color)):
				moves_ret.append({'x':pos['x']+adder, 'y':pos['y']-adder})

			adder = 1
			if (((pos['x']-adder)>=0)or((pos['y']-adder)>=0)or(board.board_matrix[pos['x']-adder][pos['y']-adder]['color']!=color)):
				moves_ret.append({'x':pos['x']-adder, 'y':pos['y']-adder})

			adder = 1
			if (((pos['x']-adder)>=0)or((pos['y']+adder)<board.height)or(board.board_matrix[pos['x']-adder][pos['y']+adder]['color']!=color)):
				moves_ret.append({'x':pos['x']-adder, 'y':pos['y']+adder})

			return moves_ret


		def moves_pos_rook_one(self, board, pos, color):
			moves_ret = []

			adder = 1
			if (((pos['x']+adder)<board.width)or(board.board_matrix[pos['x'+adder]][pos['y']]['color']!=color)):
				moves_ret.append({'x':pos['x']+adder, 'y':pos['y']})
			
			adder = 1
			if (((pos['x']-adder)>=0)or(board.board_matrix[pos['x'-adder]][pos['y']]['color']!=color)):
				moves_ret.append({'x':pos['x']-adder, 'y':pos['y']})
			
			adder = 1
			if (((pos['y']+adder)<board.height)or(board.board_matrix[pos['x']][pos['y']+adder]['color']!=color)):
				moves_ret.append({'x':pos['x'], 'y':pos['y']+adder})
			
			adder = 1
			if (((pos['y']-adder)>=0)or(board.board_matrix[pos['x']][pos['y']-adder]['color']!=color)):
				moves_ret.append({'x':pos['x'], 'y':pos['y']-adder})
			
			return moves_ret

		moves_ret = moves_pos_rook_one(board, pos, color)
		moves_ret.extend(moves_pos_bishop_one(board, pos, color))

		return moves_ret

class pc_pawn:
	symbol = 'P'
	name = 'pawn'
	info = 'can only move in forward by one step or two in first move, can kill opponent by mmoving one step forward diagonally only'
	def moves_pos(self, board, pos, color):
		moves_ret = []
		if(color == 'W'):
			if(pos['y']==7):
				init_pos = True
			else:
				init_pos = False
			if(board.board_matrix[pos['x']][pos['y']-1]['role']!='E'):
				block_ahead = True
			else:
				block_ahead = False
			if(pos['x']==0):
				if(board.board_matrix[pos['x']+1][pos['y']-1]['role']=='B'):
					moves_ret.append({'x':pos['x']+1, 'y':pos['y']-1})
			if(pos['x']==7):
				if(board.board_matrix[pos['x']-1][pos['y']-1]['role']=='B'):
					moves_ret.append({'x':pos['x']-1, 'y':pos['y']-1})
			else:
				if(board.board_matrix[pos['x']+1][pos['y']-1]['role']=='B'):
					moves_ret.append({'x':pos['x']+1, 'y':pos['y']-1})
				if(board.board_matrix[pos['x']-1][pos['y']-1]['role']=='B'):
					moves_ret.append({'x':pos['x']-1, 'y':pos['y']-1})
			if(block_ahead == False):
					moves_ret.append({'x':pos['x'], 'y':pos['y']-1})
			if(init_pos == True):
				if(board.board_matrix[pos['x']][pos['y']+2]['role']!='W'):
					moves_ret.append({'x':pos['x'], 'y':pos['y']+2})			


		if(color == 'B'):
			if(pos['y']==1):
				init_pos = True
			else:
				init_pos = False
			if(board.board_matrix[pos['x']][pos['y']+1]['role']!='E'):
				block_ahead = True
			else:
				block_ahead = False
			if(pos['x']==0):
				if(board.board_matrix[pos['x']+1][pos['y']+1]['role']=='W'):
					moves_ret.append({'x':pos['x']+1, 'y':pos['y']+1})
			if(pos['x']==7):
				if(board.board_matrix[pos['x']-1][pos['y']+1]['role']=='W'):
					moves_ret.append({'x':pos['x']-1, 'y':pos['y']+1})
			else:
				if(board.board_matrix[pos['x']+1][pos['y']+1]['role']=='W'):
					moves_ret.append({'x':pos['x']+1, 'y':pos['y']+1})
				if(board.board_matrix[pos['x']-1][pos['y']+1]['role']=='W'):
					moves_ret.append({'x':pos['x']-1, 'y':pos['y']+1})
			if(block_ahead == False):
					moves_ret.append({'x':pos['x'], 'y':pos['y']+1})
			if(init_pos == True):
				if(board.board_matrix[pos['x']][pos['y']-2]['role']!='B'):
					moves_ret.append({'x':pos['x'], 'y':pos['y']-2})


		return moves_ret

class pc_knight:
	symbol = 'N'
	name = 'knight'
	info = 'gallops'
	def moves_pos(self, board, pos, color):
		moves_ret = []
		for i in 1..4:
			
		
		return moves_ret

def move_pc(board, init_pos, final_pos, color):
	assert (board.board_matrix[init_pos['x']][init_pos['y']]['color']==color),"Invalid init position selected"
	assert (board.board_matrix[final_pos['x']][final_pos['y']]['color']!=color),"Invalid final position selected"
	assert (final_pos in any_pc_moves_pos(board.board_matrix[init_pos['x']][init_pos['y']]['role'], board, init_pos, color)),"Invalid move for the selected piece"
	if(board.board_matrix[final_pos['x']][final_pos['y']]['role']!='E'):
		dead_pc = board.board_matrix[final_pos['x']][final_pos['y']]
		board.board_matrix[final_pos['x']][final_pos['y']] = board.board_matrix[init_pos['x']][init_pos['y']]
		board.board_matrix[init_pos['x']][init_pos['y']] = {'role':'E', 'color':'E'}
		board.deadpool.append(dead_pc)
		return
	else:
		dead_pc = {'role':'E', 'color':'E'}
		board.board_matrix[final_pos['x']][final_pos['y']] = board.board_matrix[init_pos['x']][init_pos['y']]
		board.board_matrix[init_pos['x']][init_pos['y']] = {'role':'E', 'color':'E'}
		return
	


#implement castling and first mov two pawn can move



#till here


class player:
	name = 'NoName'
	color = 'E'
	isAI = False
	movesList = [{'pc':'null', 'init_pos':'null', 'final_pos':'null', 'desc':'null'}]
	def __init__(name, color, isAI):
		self.name = name
		self.color = color
		self.isAI = isAI


class game:
	def __init__(self, ChessBoard, player1, player2):





first = ChessBoard(8,8)
first.board_print()

#I updated the array with pieces object rather than {'role':'E', 'color':'E'} type thingy, make respective changes in the pieces's moves_pos function and also in the move_pc function