#!/usr/bin/python

import pieceAttributes

class Piece:
	def __init__(self,color,pieceType,position,status):
		# print position
		self.color = color
		self.pieceType = pieceType
		self.position = position
		self.status = status
		# print self.position

	def displayPiece(self):
		print "color : ", self.color,  ", pieceType: ", self.pieceType,", position : ", self.position,  ", status: ", self.status

	def killPiece(self):
		setattr(self,'status',pieceAttributes.Status.Dead)
		return


