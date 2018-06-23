#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# PaSwitchGitHubAccount2018TK.py

from Tkinter import *
import os

# 'C:\\Users\\Administrator\\'
# 'HOMEDRIVE'	'USERPROFILE'	'HOMEPATH'
conf__strFolder = os.getenv('HOMEDRIVE') + os.getenv('HOMEPATH') + '\\'

A_strFolders = (
	'E:\\git-folder\\git-asm32cn',
	'E:\\git-folder\\git-asm32net'
)

A_strButtonsName = (
	'asm32cn@github.com',
	'asm32net@github.com',
	A_strFolders[0],
	A_strFolders[1]
)

conf__strFiles = (
	conf__strFolder + '.gitconfig',
	conf__strFolder + '.git-credentials'
)

conf__strDatas = (
	(
		'[user]\n\tname = asm32cn\n\temail = asm32@qq.com\n[credential]\n\thelper = store\n',
		'https://asm32cn:paaddde010@github.com\nhttps://asm32net:paaddde010@github.com\n'
	),
	(
		'[user]\n\tname = asm32net\n\temail = 379754432@qq.com\n[credential]\n\thelper = store\n',
		'https://asm32net:paaddde010@github.com\nhttps://asm32cn:paaddde010@github.com\n'
	)
)

class PaSwitchGitHubAccount2018TK(Tk):
	def __init__(self):
		Tk.__init__(self)

		self.title('PaSwitchGitHubAccount2018TK.pyw')
		self.geometry('300x200')

		self.columnconfigure(0, weight=1)

		def SaveFiles(n):
			for i in xrange(2):
				with open(conf__strFiles[i], 'wb') as fo:
					fo.write(conf__strDatas[n][i])

		def btnClick(n):
			if n == 0:
				SaveFiles(0)
			elif n == 1:
				SaveFiles(1)
			elif n == 2:
				os.system('start ' + A_strFolders[0])
			elif n == 3:
				os.system('start ' + A_strFolders[1])

		for i in xrange(len(A_strButtonsName)):
			self.rowconfigure(i, weight=1)
			oButton = Button( text=A_strButtonsName[i], command=lambda n=i:btnClick(n) )
			oButton.grid(row=i, column=0, padx=10, pady=5, sticky='nwse')

if __name__ == '__main__':
	PaSwitchGitHubAccount2018TK()
	mainloop()