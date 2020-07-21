import random

def showBoard(board, matrix):
	for row in matrix:
		s = ''
		for box in row:
			if box == '|':
				s = s + '|'
			else:
				s = s + board.get(box)
		print(s)		 

def isValid(move, board):
	if board.get(move) == ' ':
		return True
	else:
		return False

def boardFull(board, boxes):
	for box in boxes:
		if board[box] == ' ':
			return False;
	return True;

def checkWin(board):
	if (board['tl'] == board['tm'] == board['tr']) and (board['tl'] != ' '):
		return board['tl']
	elif board['ml'] == board['mm'] == board['mr'] and (board['ml'] != ' '):
		return board['ml']
	elif board['ll'] == board['lm'] == board['lr'] and (board['ll'] != ' '):
		return board['ll']
	elif board['tl'] == board['mm'] == board['lr'] and (board['tl'] != ' '):
		return board['tl']
	elif board['tr'] == board['mm'] == board['ll'] and (board['tr'] != ' '):
		return board['tr']
	elif board['tr'] == board['mr'] == board['lr'] and (board['tr'] != ' '):
		return board['tr']
	elif board['tm'] == board['mm'] == board['lm'] and (board['tm'] != ' '):
		return board['tm']
	elif board['tl'] == board['ml'] == board['ll'] and (board['tl'] != ' '):
		return board['tl']
	else:
		return 0;
	

board = {
	  'tl': ' ',
	  'tm': ' ',
	  'tr': ' ',
	  'ml': ' ',
	  'mm': ' ',
	  'mr': ' ',
	  'll': ' ',
	  'lm': ' ',
	  'lr': ' '
	  }
	  
matrix = [
	 ['tl','|', 'tm','|', 'tr'],
	 ['ml','|', 'mm','|', 'mr'], 
	 ['ll','|', 'lm','|', 'lr']
	 ]
boxes = ['tl', 'tm', 'tr', 'ml', 'mm', 'mr', 'll', 'lm', 'lr']
player = input("What do you want to play with?(x/o): ")
if player == 'x':
	comp = 'o'
else:
	comp = 'x'

while(True):
	move = input("Select Move(tl, tm, tr, ml, mm, mr, ll, lm, lr): ")
	if isValid(move, board):
		board[move] = player
	else:
		print("That is an Invalid move! TRY AGAIN.")
		continue
	compMove = 0
	while(True):
		compMove = random.choice(boxes)
		if isValid(compMove, board):
			board[compMove] = comp;
			break
		if boardFull(board, boxes):
			break
	#check for a win
	win = checkWin(board)
	if win != 0:
		if win == 'x':
			if player == 'x':
				print('You won!')
				showBoard(board, matrix)
				break;
			else:
				print('You lost! Try again later....')
				showBoard(board, matrix)
				break;
		else:
			if player == 'o':
				print('You won!')
				showBoard(board, matrix)
				break;
			else:
				print('You lost! Try again later....')
				showBoard(board, matrix)
				break;
				
	if boardFull(board, boxes):
		print("Game ends!")
		showBoard(board, matrix)
		break
	showBoard(board, matrix)







