#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-base64-demo-1.py

import base64

class Base64Utils():
	strKey = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

	def Base64Encode(self, s):
		chr1 = chr2 = chr3 = 0;
		enc1 = enc2 = enc3 = enc4 = 0;
		i, j, nCount = 0, 0, len(s)
		byteCache = ['='] * ((nCount + 2) / 3 * 4)
		while i < nCount:
			chr1 = ord(s[i]); i += 1;
			enc1 = chr1 >> 2
			if i < nCount:
				chr2 = ord(s[i]); i += 1;
				enc2 = ((chr1 & 3) << 4) | ((chr2 & 0xf0) >> 4);
				if i < nCount:
					chr3 = ord(s[i]); i += 1;
					enc3 = ((chr2 & 15) << 2) | ((chr3 & 0xc0) >> 6)
					enc4 = chr3 & 63;
				else:
					enc3 = (chr2 & 15) << 2
					enc4 = 64
			else:
				enc2 = (chr & 3) << 4;
				enc3 = enc4 = 64;

			byteCache[j] = self.strKey[enc1]; j += 1;
			byteCache[j] = self.strKey[enc2]; j += 1;
			byteCache[j] = self.strKey[enc3]; j += 1;
			byteCache[j] = self.strKey[enc4]; j += 1;

		return ''.join(byteCache)

def Main():
	b64 = Base64Utils()
	strData = "py-base64-demo-1.py\n程序中书写着所见所闻所感，编译着心中的万水千山。"
	strSysEncrypt = b64.Base64Encode(strData)
	strUserEncrypt = base64.b64encode(strData)
	print 'strData:\n\t' + strData
	print 'strSysEncrypt:\n\t' + strSysEncrypt
	print 'strUserEncrypt:\n\t' + strUserEncrypt

if __name__ == '__main__':
	Main()


'''
strData:
	py-base64-demo-1.py
程序中书写着所见所闻所感，编译着心中的万水千山。
strSysEncrypt:
	cHktYmFzZTY0LWRlbW8tMS5weQrnqIvluo/kuK3kuablhpnnnYDmiYDop4HmiYDpl7vmiYDmhJ/vvIznvJbor5HnnYDlv4PkuK3nmoTkuIfmsLTljYPlsbHjgII=
strUserEncrypt:
	cHktYmFzZTY0LWRlbW8tMS5weQrnqIvluo/kuK3kuablhpnnnYDmiYDop4HmiYDpl7vmiYDmhJ/vvIznvJbor5HnnYDlv4PkuK3nmoTkuIfmsLTljYPlsbHjgII=
'''