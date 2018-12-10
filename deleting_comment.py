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
delete_comment = form.getvalue("delete_comment") 
delete_comment = int(delete_comment)
def deleting_comment():  
    words = []
    line_counter = 0
    first_file = open(path + 'CommentsLog.txt', 'r')
    for line in first_file:
        words.append(line)        
    first_file.close()
    if len(words) > 0:
        del words[delete_comment]
    second_file = open(path + 'CommentsLog.txt', 'w')
    for word in words:
        second_file.write(word)
    second_file.close()

print('<html>')

print('<head>')
print('<meta http-equiv="refresh" content="0;url=http://localhost/cgi-bin/test_cgi.py" /> ')
print('</head>')
print('<body>')
deleting_comment()
print('<P> ABV </P>')
print('</body>')
print('</html>')
