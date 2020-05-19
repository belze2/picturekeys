### picturekeygenerator ###
import pickle
'''
some information

'''
class KeyObj:
	def __init__(self, PART):
		self.sessionKEY = PART

class Materials:
	def __init__(self, pictureFileName):
		# setup keys with a pictue file 
		self.KEYDATA = []
		self.keypartbuffer = ''
		self.blockcounts = 0
		self.part = None
		if pictureFileName:
			self.keyObj = open(pictureFileName, 'rb')
			while self._reading():
				self.blockcounts += 1
				self.KEYDATA.append(self.keypartbuffer)
				if self.blockcounts == 99:
					self.part = KeyObj(self.keypartbuffer)
					break
			self.keyObj.close()
			print('--KEYDATA is ready... counted blocks:', self.blockcounts)
		else:
			print('tell the name of a picturefile to initialize..')
			
		print('--lenght of the sessionKEY(block 99) is:', len(self.part.sessionKEY))
		print('--method encrypt(string) for hiding a string')
		print('--method decrypt(string) for revealing a string')
		print(self.part.sessionKEY)
		#print(self.encrypt('Hello!0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ? lets go!'))
		print('\n')
		

	def _reading(self):
		# returns 0 when the reading reaches the end
		self.keypartbuffer = ''
		self.keypartbuffer = self.keyObj.read(1028)
		if self.keypartbuffer != '': return 1
		else: return 0		

	def _ciph(self, ordl):
		# cycle too high or low bytevalues
		if ordl > 255: return ordl - 256
		elif ordl < 0: return ordl + 256
		else: return ordl
	
	def export(self):
		with open('sessionkey.dat', 'wb') as picklefile:
			pickle.dump(self.part, picklefile)
		print('--KeyObj has been pickled to sessionkey.dat..')
		
	def decrypt(self, chipertext):
		# decrypt a chipertext via Picturebytes
		message = ''
		for k, item in enumerate(chipertext):
			message += chr(self._ciph(ord(item) - self.part.sessionKEY[k])) # substraction can be under 0!
		return message

	def encrypt(self, plaintext):
		# encrypt a plain textline
		feed = list(plaintext)
		r = ''
		for k, item in enumerate(feed):
			print(item, ord(item), self.part.sessionKEY[k])
			r += chr(self._ciph(ord(item) + self.part.sessionKEY[k])) # addition can be over 256!
		return r



