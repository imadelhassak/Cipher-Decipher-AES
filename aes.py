#AES	
#KEY	=16
#IV		=16
#MODE 	=CBC

from Crypto.Cipher import AES
from Crypto import Random
import base64

def Encrypt(message):
	block_size =16
	padding= "*"
	p=lambda  s :s +(block_size-len(s) % block_size )*padding
	KEY = Random.new().read(16)
	IV = Random.new().read(16)
	E =AES.new(KEY,AES.MODE_CBC,IV)
	Encrypted_message = base64.b64encode(IV + E.encrypt(p(message.encode('utf-8'))))
	data =[KEY, Encrypted_message]
	return data


def Decrypt(KEY, Encrypted_message):
	Encrypted_message_=base64.b64decode(Encrypted_message)[16:]
	IV_=base64.b64decode(Encrypted_message)[:16] 
	D =AES.new(KEY,AES.MODE_CBC,IV_)
	Plain_text =D.decrypt(Encrypted_message_)
	Plain_text = Plain_text.decode('utf-8')
	print(Plain_text.rstrip('*'))


data = Encrypt("MY NAME IS IMAD")

print(data[0])

Decrypt(data[0],data[1])
