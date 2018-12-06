#!/usr/bin/python3
import os
import os.path
path = "/var/www/html/"
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

form = cgi.FieldStorage()
#value = form["comment"]
special_simbols = '!@#'
comment = form.getvalue("comment", '')
#print("<P>%s</P>" % (comment + special_simbols))

def Comment_file():
    global comment 
    CommentsLog = open(path + "CommentsLog.txt", 'a+')
    CommentsLog.write(comment + special_simbols)
    CommentsLog.write('\n')

if os.environ['REQUEST_METHOD'] == 'POST':
    Comment_file()

def deleting_comment():  
    delete_comment = int(form.getvalue("delete_comment"))
    words = []
    line_counter = 0
    first_file = open(path + 'CommentsLog.txt', 'r')
    for line in first_file:
        words.append(line)        
    first_file.close()
    del words[delete_comment]
    second_file = open(path + 'CommentsLog.txt', 'w')
    for word in words:
        second_file.write(word)
    second_file.close()

def read_from_file():
    global special_simbols
    line_counter = 0
    CommentsLog = open(path + "CommentsLog.txt", 'r')
    # print("<P>Comments <br>%s</P><br>" % CommentsLog.read().replace(special_simbols, ''))
    for line in CommentsLog:
        line_counter += 1
        print('<form action = "/cgi-bin/test_cgi.py" method= "get">')
        print(' <P> %s <button type="submit" name="delete_comment" value="%d">X</button><br></P>' % ((line.replace(special_simbols, '')), (line_counter)))
        print('</form>') 
        
    CommentsLog.close()

print('<html>')
print('<head>')
print('<link rel = "stylesheet" href = "/style.css" style = "text/css">')
print('</head>')
print('<body>')
print('<h1> Ceco Zadacha </h1>')
print('<p> Ivan\'s image </p>')
print('<div id = "ImageContainer">')
print('	<img src= "/DSC_0213.JPG" />')
print('</div>')
print('<div id = "CommentContainer">')
print(' <div id = "CommentShow" >')
#print('<P> Comments: </P>')
deleting_comment()
read_from_file()
print(' </div>')
print(' <div id = "CommentEnter">')
print('	    <form action= "/cgi-bin/test_cgi.py" method= "post">')
print('		    <P>Comments:</P>')
print('		    <input type = "text" name= "comment" id="comment"/><br><br>')
print('		    <input type="submit" value = "Submit">')
print('	    </form>')
print(' </div>')
print('</div>')
print('</body>')
print('</html>')