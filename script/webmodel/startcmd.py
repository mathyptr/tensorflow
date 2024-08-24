#!/usr/bin/env python3

print(
    """\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<body>
<h1>Start .............</h1>
</body>
</html>"""
)


f = open("/content/cmd/cmdfile.txt", "w")
f.write("START")
f.close()
