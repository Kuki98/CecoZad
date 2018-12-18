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

if os.environ['HTTP_REFERER'] == ('http://localhost/cgi-bin/test_cgi.py?edit_line=%s' % edit_comment_line):
    url_to_go_back = 'http://localhost/cgi-bin/test_cgi.py'
    filename = 'CommentsLog.txt'
elif os.environ['HTTP_REFERER'] == ('http://localhost/cgi-bin/pic2.py?edit_line=%s' % edit_comment_line):
    url_to_go_back = 'http://localhost/cgi-bin/pic2.py'
    filename = 'CommentsLogPic2.txt'

def edit_comment(filename):
	words = []
	first_file = open(path + filename, 'r')
	for line in first_file:
		words.append(line)        
	first_file.close()
	if len(words) > 0:
	    words[int(edit_comment_line)] = (new_comment + '!@#' + '\n') 
	second_file = open(path + filename, 'w')
	for word in words:
		second_file.write(word)
	second_file.close()

print('<html>')
print('<head>')
print('<meta http-equiv="refresh" content="0;url=%s" /> ' % url_to_go_back)  
print('</head>')
print('<body>')
edit_comment(filename)
print('</body>')
print('</html>')
      