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
	'E:\\git-folder\\git-user1',
	'E:\\git-folder\\git-user2'
)

A_strButtonsName = (
	'user1@github.com',
	'user2@github.com',
	A_strFolders[0],
	A_strFolders[1]
)

conf__strFiles = (
	conf__strFolder + '.gitconfig',
	conf__strFolder + '.git-credentials'
)

conf__strDatas = (
	(
		'[user]\n\tname = user1\n\temail = email1@host.com\n[credential]\n\thelper = store\n',
		'https://user1:******@github.com\nhttps://user2:******@github.com\n'
	),
	(
		'[user]\n\tname = user2\n\temail = email2@host.com\n[credential]\n\thelper = store\n',
		'https://user2:******@github.com\nhttps://user1:******@github.com\n'
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