#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-BKDRHash-demo-1.py

class PythonBKDRHashDemo1():
	def BKDRHash(self, s):
		nSeed = 131 # 31 131 1313 13131 131313 etc
		nHash = 0
		for ch in s:
			nHash = nHash * nSeed + ord(ch)
		return nHash & 0x7fffffff

def Main():
	A_strKeys = ("C", "C++", "Java", "C#", "Python", "Go", "Scala", "vb.net", "JavaScript", "PHP", "Perl", "Ruby")
	brd = PythonBKDRHashDemo1()

	for i in xrange(len(A_strKeys)):
		s = A_strKeys[i]
		nHash = brd.BKDRHash(s)
		print '%-10d %-15s %11u %3d' % (i, s, nHash, nHash % 31)

if __name__ == '__main__':
	Main()

'''
0          C                        67   5
1          C++                 1155463   0
2          Java              168038906  27
3          C#                     8812   8
4          Python           1962499928   9
5          Go                     9412  19
6          Scala            1045413186   0
7          vb.net            763463135   2
8          JavaScript        557701633   8
9          PHP                 1382392   9
10         Perl              181595583   1
11         Ruby              186364258   8
'''