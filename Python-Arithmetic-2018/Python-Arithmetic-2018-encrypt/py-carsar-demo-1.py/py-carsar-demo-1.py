#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-carsar-demo-1.py

class Carser():
	def CarserEncode(self, s):
		nCount = len(s)
		cache = ['\0'] * nCount
		for i in xrange(nCount):
			ch = ord(s[i])
			if ch >= 97 and ch <= 122:
				ch = 97 + (ch - 97 + 3) % 26
			elif ch >= 65 and ch <= 90:
				ch = 65 + (ch - 65 + 3) % 26
			cache[i] = chr(ch)
		return ''.join(cache)

	def CarserDecode(self, s):
		nCount = len(s)
		cache = ['\0'] * nCount
		for i in xrange(nCount):
			ch = ord(s[i])
			if ch >= 97 and ch <= 122:
				ch = 97 + (ch - 97 - 3) % 26
			elif ch >= 65 and ch <= 90:
				ch = 65 + (ch - 65 - 3) % 26
			cache[i] = chr(ch)
		return ''.join(cache)

def Main():
	strSource = "py-carsar-demo-1.py (Python实现caesar凯撒加密算法)";
	carser = Carser()
	strEncrypt = carser.CarserEncode(strSource)
	strDecrypt = carser.CarserDecode(strEncrypt)

	print 'strSource:\n\t' + strSource
	print 'strEncrypt:\n\t' + strEncrypt
	print 'strDecrypt:\n\t' + strDecrypt

if __name__ == '__main__':
	Main()

'''
strSource:
	py-carsar-demo-1.py (Python实现caesar凯撒加密算法)
strEncrypt:
	sb-fduvdu-ghpr-1.sb (Sbwkrq实现fdhvdu凯撒加密算法)
strDecrypt:
	py-carsar-demo-1.py (Python实现caesar凯撒加密算法)
'''