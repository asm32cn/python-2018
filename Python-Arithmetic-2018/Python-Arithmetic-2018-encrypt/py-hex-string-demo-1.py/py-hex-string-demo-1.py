#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-hex-string-demo-1.py

class HexString():
	strHexDigit = "0123456789ABCDEF"
	def HexStringEncode(self, s):
		i, nCount = 0, len(s)
		cache = ['\0'] * (nCount * 2)
		for ch in s:
			nCode = ord(ch)
			cache[i] = self.strHexDigit[(nCode & 0xf0) >> 4]; i += 1;
			cache[i] = self.strHexDigit[nCode & 15]; i += 1;
		return ''.join(cache)

	def HexStringDecode(self, s):
		dict = {}
		for i in xrange(len(self.strHexDigit)):
			dict[self.strHexDigit[i]] = i
		nCount = len(s) / 2
		cache = ['\0'] * nCount
		for i in xrange(nCount):
			n = i + i
			cache[i] = chr( (dict[s[n]] << 4) + dict[s[n + 1]] )
		return ''.join(cache)

def Main():
	hs = HexString()
	strSource = 'c-base64-demo-1.c\n程序中书写着所见所闻所感，编译着心中的万水千山。'
	strEncrypt = hs.HexStringEncode(strSource)
	strDecrypt = hs.HexStringDecode(strEncrypt)
	print 'strSource:\n\t%s\nstrEncrypt:\n\t%s\nstrDecrypt:\n\t%s' % (strSource, strEncrypt, strDecrypt)

if __name__ == '__main__':
	Main()
