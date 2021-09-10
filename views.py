from utils import delete_note, load_data, load_template, add_note, build_response, update_note
from urllib import parse

def index(request):
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, id=dados.id, details=dados.content)
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            params[parse.unquote_plus(chave)] = parse.unquote_plus(valor)
        if 'titulo' in params.keys():
            if params["titulo"] != '' or params["detalhes"] != '':
                add_note(params)
        elif 'new-title' in params.keys():
            update_note(params["id"], params["new-title"], params["new-content"])
        else:
            delete_note(params["id"])
        return build_response(body=load_template('index.html').format(notes=notes), code=303, reason='See Other', headers='Location: /')

    return build_response(body=load_template('index.html').format(notes=notes))