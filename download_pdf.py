import urllib.request
html = urllib.request.urlopen('<PDF_URL>')
fobj = open('/tmp/<file_name>.pdf', 'ab')
while True:
    data = html.read(4096)
    if not data:
        break
    fobj.write(data)
fobj.close()
