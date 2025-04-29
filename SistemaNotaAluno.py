from PIL import Image, ImageTk
import customtkinter as ctk

#--------------------------- Função Calcular média ----------------------------------
def media():
    n = nome.get() #get é o comando que puxa o que tem na caixa - vem como texto(input)
    n1 = float(unidade01.get().replace(',','.'))#replace (subistituir ',' por '.')
    n2 = float(unidade01.get().replace(',','.'))#replace (subistituir ',' por '.')
    n3 = float(unidade01.get().replace(',','.'))#replace (subistituir ',' por '.')

    media = (n1+n2+n3)/3

    if (media >= 7):
        situacao = 'foi Aprovado(a)\n Parabéns!🥳'
    elif (media >= 5 and media < 7):
        situacao = "está na Recuperação \n😟"
    else:
        situacao = 'foi Reprovado(a) \n🥺'
    
    resultado.configure(
        text = f'Olá {n}, \nMédia: {media:.1f} \nVocê {situacao} '
    )
#-----------------------------------------------------------------------------------

#--------------------------- Função Limpar Campos  ---------------------------------
def limpar(): #apaga as variavéis
    nome.delete(0,'end')
    unidade01.delete(0,'end')
    unidade02.delete(0,'end')
    unidade03.delete(0,'end')
    resultado.configure(text='')
#-----------------------------------------------------------------------------------

ctk.set_appearance_mode('system') #muda a cor da janela "system = cor do sistema do usuário" # Pode ser "light" ou "dark"
#=============================== Janela Principal =================================
janela = ctk.CTk() #criação da janela
janela.geometry('600x650') #determina o tamanho larguraxaltura
janela.resizable(False,False) #trava o tamanho da janela
janela.title('Notas') #altera o nome da janela
janela.iconbitmap('foto00.ico') #altera o icone da janela (site: icon icons)
#==================================================================================

# ============================ Incluir imagem de fundo ===================================
# Carregar a imagem
imagem = Image.open('planofundo.jpeg')      # Nome da imagem que está na pasta
imagem = imagem.resize((500, 600))    # Redimensiona pra caber certinho
imagem_tk = ImageTk.PhotoImage(imagem)

# Colocar a imagem num rótulo (label) que cobre toda a janela
fundo = ctk.CTkLabel(janela, image=imagem_tk, text="")  # text="" é pra não aparecer texto
fundo.place(x=0, y=0, relwidth=1, relheight=1)  # relwidth=1 e relheight=1 faz preencher tudo
#==================================================================================



#==========================Titulo da Janela: Sistema de Notas =====================
#criar primeiro titulo da janela(não precisa de variavel)
ctk.CTkLabel(janela,
             text='📊 Sistema de Notas Escolares', #Nome do texto
             text_color='#00ACC2', #Cor da letra (escolher cor através do color picker)
             #fg_color='#00ACC2', #cor de fundo da caixa 
             font=("Roboto", 24, "bold") #tipo da letra, tamanho, deixar a letra mais intensa(negrito)
             ).pack(pady=20) #inicializa o componente  #pady = 10 (dá um espaçamento entre o titulo e a tela)

# criação de subtitulo
ctk.CTkLabel(janela,
             text='Bem-vindo! Calcule sua média escolar abaixo.',
             font=("Roboto", 14),
             text_color='#00ACC2'
             ).pack(pady=(0, 20))
#===================================================================================

#==========================Titulo da Janela: Nome do aluno =====================
ctk.CTkLabel(janela,
    text="Nome do Aluno:", #nome do aluno
    text_color='#00ACC2', #cor da letra
    font=("Roboto", 16, "bold") # tipo de letra e tamanho
).pack(pady=(10, 5)) #inicializa o componente  #pady = 10 (dá um espaçamento entre o titulo e a tela)
#===================================================================================


#objetos importantes precisam estar numa variavel
#=================================CADASTRO NOME =====================================
#é preciso criar uma variavel
nome = ctk.CTkEntry(janela,    #CTkEntry(cria caixas)
                     width=400, # largura
                     height=45, #altura
                     border_color='#C8DCDC', #borda
                     fg_color='#F5F5DC', #cor de fundo da caixa  
                     placeholder_text='Digite o seu nome',   #criar texto em marca d'agua
                     text_color='black') #Cor da letra quando usuario digitar (escolher cor através do color picker)
nome.pack(pady=15) #inicializa o componente com variavel #pady = 10 (dá um espaçamento entre o titulo e a tela)
#=======================================================================================

#==========================Titulo da Janela: Notas =====================================
ctk.CTkLabel(janela,
             text='Digite suas notas:',
             text_color='#00ACC2', #Cor da letra (escolher cor através do color picker)
             #fg_color='#00ACC2', #cor de fundo da caixa 
             font=("Roboto", 16, "bold"), #tipo da letra, tamanho, #bold = deixar a letra mais intensa(negrito)
).pack(pady=(10, 5)) #inicializa o componente com variavel 
               #place (coloca os botões um ao lado do outro)
#===================================================================================


#================================= CADASTRO DAS NOTAS ===============================
#NOTA01
unidade01 = ctk.CTkEntry(janela,    #CTkEntry(cria caixas)
                     width=120, # largura
                     height=45, #altura
                     border_color='#C8DCDC', #borda
                     fg_color='#F5F5DC', #cor de fundo da caixa             
                     placeholder_text='1º unidade',   #criar texto em marca d'agua
                     text_color='black') #Cor da letra quando usuario digitar (escolher cor através do color picker)
unidade01.place(x=95,y=280) #inicializa o componente com variavel 
               #place (coloca os botões um ao lado do outro)

#---------------------------------------------------------------------------------------------
#NOTA02
unidade02 = ctk.CTkEntry(janela,    #CTkEntry(cria caixas)
                     width=120, # largura
                     height=45, #altura
                     border_color='#C8DCDC', #borda
                     fg_color='#F5F5DC', #cor de fundo da caixa             
                     placeholder_text='2º unidade',   #criar texto em marca d'agua
                     text_color='black') #Cor da letra quando usuario digitar (escolher cor através do color picker)
unidade02.place(x=230,y=280) #inicializa o componente com variavel 
               #place (coloca os botões um ao lado do outro)
#------------------------------------------------------------------------------------------------
#NOTA03
unidade03 = ctk.CTkEntry(janela,    #CTkEntry(cria caixas)
                     width=120, # largura
                     height=45, #altura
                     border_color='#C8DCDC', #borda
                     fg_color='#F5F5DC', #cor de fundo da caixa             
                     placeholder_text='3º unidade',   #criar texto em marca d'agua
                     text_color='black') #Cor da letra quando usuario digitar (escolher cor através do color picker)
unidade03.place(x=375,y=280) #inicializa o componente com variavel 
               #place (coloca os botões um ao lado do outro)
#==============================================================================================

#================================= BOTÃO CALCULAR ============================================
botao_calcular = ctk.CTkButton(janela, #CTkButton - cria o botão 
                      text='🧮Calcular Média', #texto do botão
                      width=120,
                      height=40,
                      fg_color='#00ACC2', #a cor do botão 
                      hover_color='#FFFFFF', #a cor do botão quando o mouse passa por cima  
                      cursor='hand2', #transforma o botão em uma mão(pra dizer que aquela area é clicavél)  
                      text_color='black', #cor do texto
                      font= ('Calibri',20, 'bold'),#fonte do texto
                      command=media)    
botao_calcular.place(x=120,y=360) #inicializa o componente com variavel 
               #place (coloca os botões um ao lado do outro)
#==============================================================================================


#================================= BOTÃO LIMPAR ============================================
botao_limpar = ctk.CTkButton(janela, #CTkButton - cria o botão 
                      text="🧹 Limpar Campos", #texto do botão
                      width=120, #largura
                      height=40, #altura
                      fg_color='red', #a cor do botão 
                      hover_color='#FFFFFF', #a cor do botão quando o mouse passa por cima  
                      cursor='hand2', #transforma o botão em uma mão(pra dizer que aquela area é clicavél)  
                      text_color='black', #cor do texto
                      font= ('Calibri',20, 'bold'),#fonte do texto
                      command=limpar)    
botao_limpar.place(x=300,y=360) #inicializa o componente com variavel 
               #place (coloca os botões um ao lado do outro)
#==============================================================================================

#=================================Resultado ============================================
#criar primeiro titulo da janela(não precisa de variavel)
resultado= ctk.CTkLabel(janela,
             text='',
             text_color='black', #escolher cor através do color picker
             #fg_color='#F5F5DC', #cor de fundo da caixa  
             font=('Calibri',20, )) # tipo da letra tamanho, bold= deixar a letra mais intensa(negrito)
resultado.place(x=190,y=460) #inicializa o componente com variavel 
               #place (coloca os botões um ao lado do outro)
#==============================================================================================



janela.mainloop() #rodar o sistema