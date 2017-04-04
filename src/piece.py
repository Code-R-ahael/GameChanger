#!/usr/bin/python

import pieceAttributes
import board

class Piece:
	def __init__(self,color,pieceType,position,status):
		# print position
		self.color = color
		self.pieceType = pieceType
		self.position = position
		self.status = status
		# print self.position 
		return

	def displayPiece(self):
		print ("color : ", self.color,  ", pieceType: ", self.pieceType,", position : ", self.position,  ", status: ", self.status)

	def killPiece(self):
		setattr(self,'status',pieceAttributes.Status.Dead)
		return

	def initPiece(color,pieceType):
		print(pieceType);
		print(color);
		if(pieceType==pieceAttributes.Type.Castle):
			Piece.initCastle(color)
		elif(pieceType==pieceAttributes.Type.Knight):
			Piece.initKnight(color)
		elif(pieceType==pieceAttributes.Type.Bishop):
			Piece.initBishop(color)
		elif(pieceType==pieceAttributes.Type.Queen):
			Piece.initQueen(color)
		elif(pieceType==pieceAttributes.Type.King):
			Piece.initKing(color)
		else:
			print("check")
			Piece.initPon(color)
		return

	def initPon(color):
		print("in initPon");
		if(color==pieceAttributes.Color.Black):
			i=0;
			while(i < 8):
				print(i)
				board.BlackPieces[i] = Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Pon,board.BoardPositions[6][i],pieceAttributes.Status.Alive);
				i = i+1;
		else:
			i=0;
			while(i < 8):
				board.WhitePieces[i] = Piece(pieceAttributes.Color.White,pieceAttributes.Type.Pon,board.BoardPositions[1][i],pieceAttributes.Status.Alive);
				i = i+1;
		return

	def initCastle(color):
		print("in initCastle");
		if(color==pieceAttributes.Color.Black):
			board.BlackPieces[8] = Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Castle,board.BoardPositions[7][0],pieceAttributes.Status.Alive);
			board.BlackPieces[15] = Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Castle,board.BoardPositions[7][7],pieceAttributes.Status.Alive);
		else:
			board.WhitePieces[8] = Piece(pieceAttributes.Color.White,pieceAttributes.Type.Castle,board.BoardPositions[0][0],pieceAttributes.Status.Alive);
			board.WhitePieces[15] = Piece(pieceAttributes.Color.White,pieceAttributes.Type.Castle,board.BoardPositions[0][7],pieceAttributes.Status.Alive);
		return

	def initKnight(color):
		print("in initKnight");
		if(color==pieceAttributes.Color.Black):
			board.BlackPieces[9] = Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Knight,board.BoardPositions[7][1],pieceAttributes.Status.Alive);
			board.BlackPieces[14] = Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Knight,board.BoardPositions[7][6],pieceAttributes.Status.Alive);
		else:
			board.WhitePieces[9] = Piece(pieceAttributes.Color.White,pieceAttributes.Type.Knight,board.BoardPositions[0][1],pieceAttributes.Status.Alive);
			board.WhitePieces[14] = Piece(pieceAttributes.Color.White,pieceAttributes.Type.Knight,board.BoardPositions[0][6],pieceAttributes.Status.Alive);
		return

	def initBishop(color):
		print("in initBishop");
		if(color==pieceAttributes.Color.Black):
			board.BlackPieces[10] = Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Bishop,board.BoardPositions[7][2],pieceAttributes.Status.Alive);
			board.BlackPieces[13] = Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Bishop,board.BoardPositions[7][5],pieceAttributes.Status.Alive);
		else:
			board.WhitePieces[10] = Piece(pieceAttributes.Color.White,pieceAttributes.Type.Bishop,board.BoardPositions[0][2],pieceAttributes.Status.Alive);
			board.WhitePieces[13] = Piece(pieceAttributes.Color.White,pieceAttributes.Type.Bishop,board.BoardPositions[0][5],pieceAttributes.Status.Alive);
		return

	def initQueen(color):
		print("in initQueen");
		if(color==pieceAttributes.Color.Black):
			board.BlackPieces[11] = Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Queen,board.BoardPositions[7][3],pieceAttributes.Status.Alive);
		else:
			board.WhitePieces[11] = Piece(pieceAttributes.Color.White,pieceAttributes.Type.Queen,board.BoardPositions[0][3],pieceAttributes.Status.Alive);
		return

	def initKing(color):
		print("in initKing");
		if(color==pieceAttributes.Color.Black):
			board.BlackPieces[12] = Piece(pieceAttributes.Color.Black,pieceAttributes.Type.Queen,board.BoardPositions[7][4],pieceAttributes.Status.Alive);
		else:
			board.WhitePieces[12] = Piece(pieceAttributes.Color.White,pieceAttributes.Type.Queen,board.BoardPositions[0][4],pieceAttributes.Status.Alive);
		return


