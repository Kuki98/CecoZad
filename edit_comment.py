#!/usr/bin/python3
import os
import os.path
path = "/var/www/html/"
import cgi, cgitb
cgitb.enable()
print("Content-Type: text/html")    
print()                 

form = cgi.FieldStorage()
new_comment = form.getvalue("new_comment")
edit_comment_line = form.getvalue("edit_comment_line")

def edit_comment():
	words = []
	first_file = open(path + 'CommentsLog.txt', 'r')
	for line in first_file:
		words.append(line)        
	first_file.close()
	if len(words) > 0:
	    words[int(edit_comment_line)] = (new_comment + '!@#' + '\n') 
	second_file = open(path + 'CommentsLog.txt', 'w')
	for word in words:
		second_file.write(word)
	second_file.close()


print('<html>')
print('<head>')
print('<meta http-equiv="refresh" content="0;url=http://localhost/cgi-bin/test_cgi.py" /> ')
print('</head>')
print('<body>')
edit_comment()
print('</body>')
print('</html>')




       