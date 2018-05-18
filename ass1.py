#!/usr/bin/Python2
import time
import webbrowser
option= '''
Press1- google search 
Press2- google images  
Press3- Enter anything 
Press4- Enter anything 
Press5- Enter anything 
Press6- Enter anything 
Press7- Enter anything
'''
print option
ch=raw_input()
if ch=='1':
	search_data=raw_input("Enter anything")
	final_data=search_data.strip()
	done_data=final_data.split()
	print done_data
	for i in done_data:
		webbrowser.open_new_tab('https://www.google.com/search?q='+i)

elif(ch=='2'):
	search_data=raw_input("Enter anything")
	final_data=search_data.strip()
	done_data=final_data.split()
	for i in done_data:
		webbrowser.open_new_tab('https://images.google.com/'+i)
