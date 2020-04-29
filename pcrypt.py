### picture crypt for chatlines ###
import binascii
# use:
# import pycrypt
# modul = pycrypt.Materials(picturename)
# modul.encrypt(plainline) // modul.decrypt(chipertext)
class Materials:
	def __init__(self, pictureName):
		# special materials needed to read the message clearly
		try:
			with open(pictureName, 'rb') as sternenbytes:
				keystring = binascii.a2b_base64(sternenbytes.read())
		except:
			print 'You need to insert a Picture when setting up the Materials'
		finally:
			listobj = list(keystring)
			chiper = ''
			reduced = 0
			# generate a key from pictureFile
			for item in listobj:
				if 13 < ord(item) < 256: chiper += item
				else: reduced += 1
			print 'keylenght=', len(chiper), '..OK'
			self.KEY = chiper
		
	def decrypt(self, chipertext):
		# decrypt a chipertext via Picturebytes
		message = ''
		for k, item in enumerate(chipertext):
			message += chr(self._ciph(ord(item) - ord(self.KEY[k]))) # substraction can be under 0!
		return message

	def encrypt(self, plaintext):
		# encrypt a plain textline
		feed = list(plaintext)
		r = ''
		for k, item in enumerate(feed):
			r += chr(self._ciph(ord(item) + ord(self.KEY[k]))) # addition can be over 256!
		return r
		

	def _ciph(self, ordl):
		# cycle too high or low bytevalues
		if ordl > 255: return ordl - 256
		elif ordl < 0: return ordl + 256
		else: return ordl


