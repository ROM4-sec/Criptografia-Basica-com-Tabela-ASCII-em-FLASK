from flask import Flask, render_template, request
import random

app = Flask(__name__)

def criptografar(mensagem, coeficiente):
    ruido_limite = 19
    bases = ['hex', 'oct', 'html']
    base_idx = 0
    blocos_finais = []
    for i in range(0, len(mensagem), coeficiente):
        grupo = mensagem[i : i + coeficiente]
        for char in grupo:
            decimal = ord(char)
            base_atual = bases[base_idx % 3]
            if base_atual == 'hex':
                bloco = hex(decimal)[2:].upper().zfill(5)
            elif base_atual == 'oct':
                bloco = oct(decimal)[2:].zfill(5)
            else:
                bloco = f"&#{str(decimal).zfill(3)}"
            blocos_finais.append(bloco)
            base_idx += 1 
        for _ in range(coeficiente):
            valor_ruido = random.randint(0, ruido_limite)
            blocos_finais.append(str(valor_ruido).zfill(5))
    return "".join(blocos_finais)

def descriptografar(codigo_completo, coeficiente):
    if not codigo_completo: return ""
    bases = ['hex', 'oct', 'html']
    base_idx = 0
    mensagem_recuperada = []
    todos_blocos = [codigo_completo[i:i+5] for i in range(0, len(codigo_completo), 5)]
    ponteiro = 0
    while ponteiro < len(todos_blocos):
        blocos_mensagem = todos_blocos[ponteiro : ponteiro + coeficiente]
        for bloco in blocos_mensagem:
            base_atual = bases[base_idx % 3]
            try:
                if base_atual == 'hex':
                    char = chr(int(bloco, 16))
                elif base_atual == 'oct':
                    char = chr(int(bloco, 8))
                else:
                    limpo = bloco.replace("&#", "")
                    char = chr(int(limpo))
                if ord(char) > 31:
                    mensagem_recuperada.append(char)
                    base_idx += 1
            except:
                pass
        ponteiro += (coeficiente * 2)
    return "".join(mensagem_recuperada)

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = None #começa como None para não mostrar a div no HTML
    texto = ""
    coef = 3

    if request.method == 'POST':
        #captura os dados do formulário
        texto = request.form.get('texto', '')
        coef_raw = request.form.get('coeficiente', '3')
        coef = int(coef_raw)
        acao = request.form.get('acao') #captura qual botão foi clicado

        if acao == 'cripto':
            resultado = criptografar(texto, coef)
        elif acao == 'descripto':
            resultado = descriptografar(texto, coef)
            
    #retorna as variáveis para o HTML
    return render_template('index.html', resultado=resultado, texto=texto, coef=coef)

if __name__ == '__main__':
    app.run(debug=True)