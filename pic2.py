#!/usr/bin/python3
import os
import os.path
path = "/var/www/html/"
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html")   
print()         
form = cgi.FieldStorage()
special_simbols = '!@#'

def get_url():
    url = os.environ['HTTP_HOST']
    uri = os.environ['REQUEST_URI']
    return url + uri

default_url = "localhost/cgi-bin/pic2.py"

comment = form.getvalue("comment", '')
def Comment_file():
    global comment 
    CommentsLog = open(path + "CommentsLogPic2.txt", 'a+')
    if comment == '':
        CommentsLog.close()
    else:
        CommentsLog.write(comment + special_simbols)
        CommentsLog.write('\n')

if os.environ['REQUEST_METHOD'] == 'POST':
    Comment_file()

def read_from_file():
    global special_simbols
    line_counter = 0
    CommentsLog = open(path + "CommentsLogPic2.txt", 'r')
    for line in CommentsLog:
        line_counter += 1
        if get_url() != default_url:
            edit_line = form["edit_line"].value
            if int(edit_line) == line_counter-1:
                edit_form(line_counter)
            else:
                print('<form action = "/cgi-bin/deleting_comment.py" method= "get">')
                print(' <P> %s '  % (line.replace(special_simbols, '')))
                print('<button type="submit" name="delete_comment" value="%d">X</button><button formmethod="get" formaction="/cgi-bin/pic2.py?edit_line=%d" type="submit" name="edit_line" value=%d>Edit</button><br></P>' % 
                ((line_counter-1),(line_counter-1),(line_counter-1)))
                print('</form>')
                
        else:
            print('<form action = "/cgi-bin/deleting_comment.py" method= "get">')
            print(' <P> %s '  % (line.replace(special_simbols, '')))
            print('<button type="submit" name="delete_comment" value="%d">X</button><button formmethod="get" formaction="/cgi-bin/pic2.py?edit_line=%d" type="submit" name="edit_line" value=%d>Edit</button><br></P>' % 
            ((line_counter-1),(line_counter-1),(line_counter-1)))
            print('</form>')
            
    CommentsLog.close() 
def edit_form(button_value):
    print('<form action="/cgi-bin/edit_comment.py" method="GET">')
    print(' <input type= "text" name="new_comment" >')
    print(' <button type= "submit" name="edit_comment_line" value=%d>Enter</button><br> ' % (button_value-1))
    print('</form>')

print('<html>')
print('<head>')
print('<link rel = "stylesheet" href = "/style.css" style = "text/css">')
print('</head>')
print('<body>')
print('<h1> Ceco Zadacha </h1>')
print('<p> Picture 2</p>')
print('<a href="http://localhost"><p>Go home</p></a>')
print('<div id = "ImageContainer">')
print(' <img src= "/pic2.jpeg" />')
print('</div>')
print('<div id = "CommentContainer">')
print(' <div id = "CommentShow" >')
read_from_file()
print(' </div>')
print(' <div id = "CommentEnter">')
print('     <form action= "/cgi-bin/pic2.py" method= "post">')
print('         <P>Comments:</P>')
if os.environ['REQUEST_METHOD'] == 'POST':
    if comment == '':
        print('<P style="color:red;"> Cant be empty! </P>')
print('         <input type = "text" name= "comment" id="comment"/><br><br>')
print('         <input type="submit" value = "Submit">')
print('     </form>')
print(' </div>')
print('</div>')
print('</body>')
print('</html>')
