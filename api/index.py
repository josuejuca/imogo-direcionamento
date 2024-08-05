from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    os_info = parse_user_agent(user_agent)
    return f"<p>Seu sistema operacional é: {os_info}</p>"

@app.route('/proprietario')
def proprietario():
    return handle_redirection_Proprietario()

@app.route('/corretor')
def corretor():
    return handle_redirection_Corretor()

def handle_redirection_Proprietario():
    user_agent = request.headers.get('User-Agent')
    os_info = parse_user_agent(user_agent)

    if os_info == 'Android':
        return redirect('https://play.google.com/store/apps/details?id=br.com.politiz.qi.owner&hl=pt_BR')
    elif os_info == 'iOS':
        return redirect('https://apps.apple.com/br/app/imogo-vendedor/id6447977587')
    else:
        return redirect('https://imogo.com.br')
        
def handle_redirection_Corretor():
    user_agent = request.headers.get('User-Agent')
    os_info = parse_user_agent(user_agent)

    if os_info == 'Android':
        return redirect('https://play.google.com/store/apps/details?id=br.com.politiz.qi&hl=pt_BR')
    elif os_info == 'iOS':
        return redirect('https://apps.apple.com/br/app/imogo/id1661571220')
    else:
        return redirect('https://imogo.com.br')

def parse_user_agent(user_agent):
    if 'Windows' in user_agent:
        return 'Windows'
    elif 'Android' in user_agent:
        return 'Android'
    elif 'iPhone' in user_agent or 'iPad' in user_agent:
        return 'iOS'
    else:
        return 'Desconhecido'

if __name__ == '__main__':
    app.run()
