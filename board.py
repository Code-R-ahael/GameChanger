#!/usr/bin/python

import pieceAttributes
import piece
import string

w, h = 8, 8
BoardPositions = [[0 for x in range(w)] for y in range(h)]
Board = [[0 for x in range(w)] for y in range(h)]
BlackPieces = [0 for x in range(w+h)]
WhitePieces = [0 for x in range(w+h)]

i = 0; letters = 'abcdefgh';
while(i < 8):
	for j in range(len(letters)):
		BoardPositions[i][j] = letters[j]+str(i+1);
	i=i+1;

def init():
	initBlack()
	initWhite()
	print (Board)

def initBlack():
	for pieceType in pieceAttributes.Type:
		piece.Piece.initPiece(pieceAttributes.Color.Black,pieceType)
	Board[6] = [1 for x in range(w)]
	Board[7] = [1 for x in range(w)]

def initWhite():
	for pieceType in pieceAttributes.Type:
		piece.Piece.initPiece(pieceAttributes.Color.White,pieceType)
	Board[0] = [1 for x in range(w)]
	Board[1] = [1 for x in range(w)]
	