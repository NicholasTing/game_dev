# # This is a sample Python script.
# # Press ⌃F5 to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from factories.board_factory import board_factory
import chess
import time
import random
import chess.engine
import chess.svg

engine = chess.engine.SimpleEngine.popen_uci("stockfish")

def main():
    board = board_factory()
    move_count = 0

    board = chess.Board()
    my_turn = True
    while not board.is_game_over():
        if my_turn:
            legal_count = board.legal_moves.count()
            move_list = list(board.legal_moves)  # Find legal moves
            print(str(move_list))
            which_move = random.randint(0, legal_count - 1)  # Random move index
            first_move = move_list[which_move]  # Select move
            move_holder = chess.Move.from_uci(str(first_move))
            board.push(move_holder)
            print(board)
            print(board.turn)
            print(chess.svg.piece(chess.Piece.from_symbol("R")))
            my_turn = False
        else:
            result = engine.play(board, chess.engine.Limit(time=0.1))
            board.push(result.move)
            print(board)
            print(board.turn)
            my_turn = True
        move_count += 1  # Make the move
        time.sleep(1)

    if not my_turn:
        print('game over random moves  won')
    else:
        print('game over stock fish won')
    print(move_count)
    return True

if __name__ == '__main__':
    main()

