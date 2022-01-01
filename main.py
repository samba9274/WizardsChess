import os
from pocketsphinx import LiveSpeech, get_model_path
import chess

keywords = {'A-ONE': 'a1', 'A-TWO': 'a2', 'A-THREE': 'a3', 'A-FOUR': 'a4', 'A-FIVE': 'a5', 'A-SIX': 'a6',
            'A-SEVEN': 'a7', 'A-EIGHT': 'a8', 'B-ONE': 'b1', 'B-TWO': 'b2', 'B-THREE': 'b3', 'B-FOUR': 'b4',
            'B-FIVE': 'b5', 'B-SIX': 'b6', 'B-SEVEN': 'b7', 'B-EIGHT': 'b8', 'C-ONE': 'c1', 'C-TWO': 'c2',
            'C-THREE': 'c3', 'C-FOUR': 'c4', 'C-FIVE': 'c5', 'C-SIX': 'c6', 'C-SEVEN': 'c7', 'C-EIGHT': 'c8',
            'D-ONE': 'd1', 'D-TWO': 'd2', 'D-THREE': 'd3', 'D-FOUR': 'd4', 'D-FIVE': 'd5', 'D-SIX': 'd6',
            'D-SEVEN': 'd7', 'D-EIGHT': 'd8', 'E-ONE': 'e1', 'E-TWO': 'e2', 'E-THREE': 'e3', 'E-FOUR': 'e4',
            'E-FIVE': 'e5', 'E-SIX': 'e6', 'E-SEVEN': 'e7', 'E-EIGHT': 'e8', 'F-ONE': 'f1', 'F-TWO': 'f2',
            'F-THREE': 'f3', 'F-FOUR': 'f4', 'F-FIVE': 'f5', 'F-SIX': 'f6', 'F-SEVEN': 'f7', 'F-EIGHT': 'f8',
            'G-ONE': 'g1', 'G-TWO': 'g2', 'G-THREE': 'g3', 'G-FOUR': 'g4', 'G-FIVE': 'g5', 'G-SIX': 'g6',
            'G-SEVEN': 'g7', 'G-EIGHT': 'g8', 'H-ONE': 'h1', 'H-TWO': 'h2', 'H-THREE': 'h3', 'H-FOUR': 'h4',
            'H-FIVE': 'h5', 'H-SIX': 'h6', 'H-SEVEN': 'h7', 'H-EIGHT': 'h8'}
board = chess.Board()
print(board)
for phrase in LiveSpeech(verbose=False, sampling_rate=16000, buffer_size=2048, no_search=False, full_utt=False,
                         kws_threshold=1e-50, hmm=os.path.join(get_model_path(), 'en-us'), kws='DICT/corpus.txt',
                         lm='DICT/corpus.lm.bin', dict='DICT/corpus.dic'):
    if len(str(phrase).split()) == 2:
        print(keywords[str(phrase).split()[0]] + keywords[str(phrase).split()[1]])
        try:
            board.push_uci(keywords[str(phrase).split()[0]] + keywords[str(phrase).split()[1]])
        except ValueError:
            print("Invalid move")
        print(board)
    else:
        print("Say 2 moves at a time")
    if board.outcome() is not None: break
if board.outcome().winner is None:
    print("Draw")
elif board.outcome().winner:
    print("White wins")
else:
    print("Black wins")
