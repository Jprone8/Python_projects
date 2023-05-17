# author Jacob
# Simple tic tac toe game to show the use of dictionaries and lists in pyhton

theBoard = {'TOP-L':' ','TOP-M':' ','TOP-R':' ','MID-L':' ','MID-M':' ',
           'MID-R':' ','LOW-L':' ','LOW-M':' ','LOW-R':' '}

def printBoard(board):
  print(board['TOP-L'] + '|' + board['TOP-M'] + '|' + board['TOP-R'])
  print('-+-+-')
  print(board['MID-L'] + '|' + board['MID-M'] + '|' + board['MID-R'])
  print('-+-+-')
  print(board['LOW-L'] + '|' + board['LOW-M'] + '|' + board['LOW-R'])

def hasWon(tb, l):
  return((tb['TOP-L']==l and tb['TOP-M']==l and tb['TOP-R']==l) or
        (tb['MID-L']==l and tb['MID-M']==l and tb['MID-R']==l)or 
        (tb['LOW-L']==l and tb['LOW-M']==l and tb['LOW-R']==l) or 
        (tb['TOP-L']==l and tb['MID-L']==l and tb['LOW-L']==l) or 
        (tb['TOP-M']==l and tb['MID-M']==l and tb['LOW-M']==l) or 
        (tb['TOP-R']==l and tb['MID-R']==l and tb['LOW-R']==l) or 
        (tb['TOP-L']==l and tb['MID-M']==l and tb['LOW-R']==l) or 
        (tb['TOP-R']==l and tb['MID-M']==l and tb['LOW-L']==l))

turn = 'X'

for i in range(9):
  printBoard(theBoard)
  print('Turn for ' + turn + '. Move on which space?')
  move = input()
  theBoard[move] = turn
  if hasWon(theBoard, turn):
    print(turn + ' has won the game!')
    break
  elif turn == 'X':
    turn = 'O'
  else:
    turn = 'X'

printBoard(theBoard)
  