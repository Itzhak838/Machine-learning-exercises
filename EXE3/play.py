import alphaBetaPruning
import game
board_size=int(input("Enter board size: "))
board=game.create(board_size)
game.whoIsFirst(board)
while not game.isFinished(board):
    if game.isHumTurn(board):
        game.inputMove(board)
    else:
        board=alphaBetaPruning.go(board)
game.printState(board)

