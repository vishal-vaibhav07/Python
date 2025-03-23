

import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head><title>CGI Script</title></head>")
print("<body>")
print(f"<h2>Hello, {name}!</h2>")
print("</body>")
print("</html>")
