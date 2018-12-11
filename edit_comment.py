#!/usr/bin/python3
import os
import os.path
path = "/var/www/html/"
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html")    # HTML is following""
print()                          
form = cgi.FieldStorage()
new_comment = form.getvalue("new_comment", '') 
#edit_comment = form.getvalue("edit_comment")
#edit_comment = int(edit_comment)

def edit_comment():
	words = []
	first_file = open(path + 'CommentsLog.txt', 'r')
	for line in first_file:
		words.append(line)        
	first_file.close()
	print(words)
	if len(words) > 0:
	#	edit_comment = form.getvalue("edit_comment")
	    words[0] = (new_comment + '!@#' + '\n') 
	second_file = open(path + 'CommentsLog.txt', 'w')
	for word in words:
		second_file.write(word)
	second_file.close()
print('<html>')
print('<head>')
print('</head>')
print('<body>')
print('<form action="/cgi-bin/edit_comment.py" method="post">')
print(' <input type= "text" name="new_comment" >')
print(' <button type="submit">Enter</button><br>')
print('</form>')
edit_comment()
print('</body>')
print('</html>')



       