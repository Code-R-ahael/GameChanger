#!/usr/bin/python

import pieceAttributes
import piece
import string

w, h = 8, 8
BoardPositions = [[0 for x in range(w)] for y in range(h)]
Board = [[0 for x in range(w)] for y in range(h)]
BlackPieces = [0 for x in range(w+h)]
WhitePieces = [0 for x in range(w+h)]

i = 0;
while(i < 8):
   j = 0
   while(j < 8):
      BoardPositions[i][j] = string.lowercase[j]+str(i+1);
      j=j+1;
   i=i+1;

def init():
	initBlack()
	initWhite()
	print Board

def initBlack():
	i=0;
	while(i < 8):
		BlackPieces[i] = piece.Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Pon,BoardPositions[6][i],pieceAttributes.Status.Alive);
		Board[6][i] = 1
		i = i+1;
	j=0;
	BlackPieces[i] = piece.Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Castle,BoardPositions[7][j],pieceAttributes.Status.Alive);
	Board[7][j] = 1
	BlackPieces[i+(8-j-1)] = piece.Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Castle,BoardPositions[7][8-j-1],pieceAttributes.Status.Alive);
	Board[7][8-j-1] =1
	i = i+1;
	j = j+1;
	BlackPieces[i] = piece.Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Knight,BoardPositions[7][j],pieceAttributes.Status.Alive);
	Board[7][j] =1
	BlackPieces[i+(8-j-1)] = piece.Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Knight,BoardPositions[7][8-j-1],pieceAttributes.Status.Alive);
	Board[7][8-j-1] = 1
	i = i+1;
	j = j+1;
	BlackPieces[i] = piece.Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Bishop,BoardPositions[7][j],pieceAttributes.Status.Alive);
	Board[7][j] = 1
	BlackPieces[i+(8-j-1)] = piece.Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Bishop,BoardPositions[7][8-j-1],pieceAttributes.Status.Alive);
	Board[7][8-j-1] = 1
	i = i+1;
	j = j+1;
	BlackPieces[i] = piece.Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Queen,BoardPositions[7][j],pieceAttributes.Status.Alive);
	Board[7][j] = 1
	i = i+1;
	j = j+1;
	BlackPieces[i] = piece.Piece(pieceAttributes.Color.Black,pieceAttributes.Type.King,BoardPositions[7][j],pieceAttributes.Status.Alive);
	Board[7][j] = 1

def initWhite():
	i=0;
	while(i < 8):
		WhitePieces[i] = piece.Piece(pieceAttributes.Color.White,pieceAttributes.Type.Pon,BoardPositions[1][i],pieceAttributes.Status.Alive);
		Board[1][i] = 1
		i = i+1;
	j=0;
	WhitePieces[i] = piece.Piece(pieceAttributes.Color.White,pieceAttributes.Type.Castle,BoardPositions[0][j],pieceAttributes.Status.Alive);
	Board[0][j] = 1
	WhitePieces[i+(8-j-1)] = piece.Piece(pieceAttributes.Color.White,pieceAttributes.Type.Castle,BoardPositions[0][8-j-1],pieceAttributes.Status.Alive);
	Board[0][8-j-1] = 1
	i = i+1;
	j = j+1;
	WhitePieces[i] = piece.Piece(pieceAttributes.Color.White,pieceAttributes.Type.Knight,BoardPositions[0][j],pieceAttributes.Status.Alive);
	Board[0][j] = 1
	WhitePieces[i+(8-j-1)] = piece.Piece(pieceAttributes.Color.White,pieceAttributes.Type.Knight,BoardPositions[0][8-j-1],pieceAttributes.Status.Alive);
	Board[0][8-j-1] = 1
	i = i+1;
	j = j+1;
	WhitePieces[i] = piece.Piece(pieceAttributes.Color.White,pieceAttributes.Type.Bishop,BoardPositions[0][j],pieceAttributes.Status.Alive);
	Board[0][j] = 1
	WhitePieces[i+(8-j-1)] = piece.Piece(pieceAttributes.Color.White,pieceAttributes.Type.Bishop,BoardPositions[0][8-j-1],pieceAttributes.Status.Alive);
	Board[0][8-j-1] = 1
	i = i+1;
	j = j+1;
	WhitePieces[i] = piece.Piece(pieceAttributes.Color.White,pieceAttributes.Type.Queen,BoardPositions[0][j],pieceAttributes.Status.Alive);
	Board[0][j] = 1
	i = i+1;
	j = j+1;
	WhitePieces[i] = piece.Piece(pieceAttributes.Color.White,pieceAttributes.Type.King,BoardPositions[0][j],pieceAttributes.Status.Alive);
	Board[0][j] = 1
	