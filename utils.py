import json
from database import Database, Note

'''
HTTP/1.1
Host: 192.168.15.14:8080
Connection: keep-alive
Save-Data: on
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7
'''

def extract_route(s):
    inicio = s.index('/') + 1
    fim = s.index('HTTP') - 1
    return s[inicio:fim]

def read_file(path):
    lista = str(path)
    if lista[-1] == 'txt' or lista[-1] == 'css' or lista[-1] == 'js' or lista[-1] == 'html':
        return(open(path))
    else:
        return(open(path, 'rb').read())

def load_data():
    # return(json.loads(open('data/'+filename, 'rt').read()))
    db = Database('notes')
    return db.get_all()

def load_template(filename):
    return(open('templates/'+filename).read())

def add_note(new_note):
    db = Database('notes')
    db.add(Note(title=new_note['titulo'], content=new_note['detalhes']))

def delete_note(id):
    db = Database('notes')
    db.delete(id)

def update_note(id, title, content):
    db = Database('notes')
    db.update(Note(id=id, title=title,content=content))

def build_response(body='', code=200, reason='OK', headers=''):
    if headers=='':
        return ('HTTP/1.1 '+str(code)+' '+reason+'\n\n'+body).encode()
    return ('HTTP/1.1 '+str(code)+' '+reason+'\n'+headers+'\n\n'+body).encode()