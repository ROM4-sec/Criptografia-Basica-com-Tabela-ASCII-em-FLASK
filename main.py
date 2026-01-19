import random

def criptografar(mensagem, coeficiente):
    ruido_limite = 19
    bases = ['hex', 'oct', 'html']
    base_idx = 0
    blocos_finais = []
    
    #divide a mensagem em pedaços do tamanho do coeficiente
    for i in range(0, len(mensagem), coeficiente):
        grupo = mensagem[i : i + coeficiente]
        
        #1. processa os caracteres reais
        for char in grupo:
            decimal = ord(char)
            base_atual = bases[base_idx % 3]
            
            if( base_atual == 'hex'):
                bloco = hex(decimal)[2:].upper().zfill(5)
            elif( base_atual == 'oct'):
                bloco = oct(decimal)[2:].zfill(5)
            else: #html
                bloco = f"&#{str(decimal).zfill(3)}"
            
            blocos_finais.append(bloco)
            base_idx += 1 
            
        #2. adiciona o ruído (sempre após cada grupo)
        for _ in range(coeficiente):
            valor_ruido = random.randint(0, ruido_limite)
            blocos_finais.append(str(valor_ruido).zfill(5))
            
    return "".join(blocos_finais)

def descriptografar(codigo_completo, coeficiente):
    bases = ['hex', 'oct', 'html']
    base_idx = 0
    mensagem_recuperada = []
    
    #quebra a string gigante em blocos individuais de 5 caracteres
    todos_blocos = [codigo_completo[i:i+5] for i in range(0, len(codigo_completo), 5)]
    
    ponteiro = 0
    while( ponteiro < len(todos_blocos)):
        #1. identifica quantos blocos de mensagem existem neste grupo
        #(pode ser o valor do coeficiente ou o que sobrar antes do ruído final)
        
        #o número de blocos de mensagem real antes do ruído é o coeficiente, 
        #a menos que estejamos no último grupo e ele seja menor que o coeficiente.
        #o ruído final sempre nos ajuda a isolar.
        
        #como sabemos que SEMPRE tem 'coeficiente' blocos de ruído após a mensagem:
        #lemos até 'coeficiente' blocos, mas paramos se encontrarmos o bloco de ruído 
        #ou se o total de blocos restantes for apenas o ruído final.
        
        #vamos usar a lógica de saltos:
        blocos_mensagem = todos_blocos[ponteiro : ponteiro + coeficiente]
        
        #antes de processar, precisamos checar se esses blocos não são ruído
        #a cada ciclo de 'coeficiente', os primeiros são dados, os próximos são lixo.
        
        for bloco in blocos_mensagem:
            #se o bloco for um dos ruídos finais (adicionados no descarte), paramos
            #mas a forma mais segura é contar: se já lemos o que devia ser lido.
            
            #tenta converter baseado na ordem
            base_atual = bases[base_idx % 3]
            
            try:
                if( base_atual == 'hex'):
                    char = chr(int(bloco, 16))
                elif( base_atual == 'oct'):
                    char = chr(int(bloco, 8))
                else: #html
                    #remove o &# e converte o resto
                    limpo = bloco.replace("&#", "")
                    char = chr(int(limpo))
                
                #regra de Segurança: se o que extraímos é um caractere de controle (0-31), 
                #e não pedimos por ele, provavelmente entramos na zona de ruído.
                if( ord(char) > 31):
                    mensagem_recuperada.append(char)
                    base_idx += 1
            except:
                #se der erro de conversão, é ruído
                pass

        #pula os blocos de mensagem que acabamos de ler + os blocos de ruído
        ponteiro += (coeficiente * 2)

    return "".join(mensagem_recuperada)


"""
original = "olha esse vídeo depois, papo reto https://www.instagram.com/reel/C0XONepxwZf/"
coef = 3

print(f"--- INICIANDO TESTE (Coeficiente: {coef}) ---")
cifrado = criptografar(original, coef)
print(f"Criptografado: {cifrado}")

decifrado = descriptografar(cifrado, coef)
print(f"Descriptografado: {decifrado}")

if( original == decifrado):
    print("\n✅ SUCESSO! A lógica funcionou perfeitamente.")
else:
    print("\n❌ ERRO! A mensagem voltou diferente.")
"""
coef = 5
cifrado = "0006F00154&#1040000400018000020006100040&#1010001600011000030007300163&#1010000000017000160002000166&#2370001000008000130006400145&#1110000600005000150002000144&#1010000900014000170007000157&#1050000500001000000007300040&#1120001700011000190006100160&#1110000900019000160002000162&#1010001600005000040007400157&#0320000500016000160006800164&#1160001400017000110007000163&#0580000300000000110002F00057&#1190001200008000070007700167&#0460000800012000190006900156&#1150001100007000150007400141&#1030000500010000160007200141&#1090001600017000110002E00143&#1110001700009000080006D00057&#1140001300014000150006500145&#1080000100012000030002F00103&#0480001100000000050005800117&#0780001200003000020006500160&#1200000600016000110007700132&#1020001100005000150002F000180000000011"
decifrando = descriptografar(cifrado, coef)
print(decifrando)