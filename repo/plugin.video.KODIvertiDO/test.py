import base64
url2 = 'aHR0cHM6Ly9kbC5ncmFudG9ycmVudC5wbS90b3JyZW50cy9wZWxpY3VsYXMvRGV2aWxzLVBlYWstKDIwMjMpLWhkLm1wNDE3LnRvcnJlbnQ='
url = base64.b64decode(url2).decode('utf-8')
print(url)