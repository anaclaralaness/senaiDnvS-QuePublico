#a partir daqui vai começar a ser feita a tela do site de acordo com o que foi feito no database.py, então o database.py deve ser feito primeiro


import streamlit as st #importa biblioteca streamlit (é quem cria a tela do site) | as st >> um apelido pra não precisar digitar streamlit sempre: streamlit.title() >>>> st.title()

import database as db #pega o arquivo database.py (que eu criei) e traz todas as funções dele | as db >> cria um apelido pra database

db.criar_tabela() #chama a função criar_tabela que ta no database.py | ele se conecta em escola.db e ve se a tabela alunos ja ta criada, se não tiver ele cria com os comandos de dentro da função

st.title("Cadastro de Alunos") #cria o título principal do site (função do streamlit)
st.header ("Escola Firjan Sesi") #cria o cabeçalho do site
st.subheader ("Desde 2018") #cria um cabeçalhinho pro site

with st.form ("nome_do_formulario"): #cria um formulário | with >> tudo o que tiver indentado embaixo dessa linha ta dentro do formulario 
  #form >> avisa que é um formulário e que só pode enviar o que ta escrito quando clicar no botão
  nome = st.text_input("Nome") #cria uma caixa de texto que guarda o que escrevem ali na variável "nome" | ("nome") > vai ficar escrito em cima da caixa
  idade = st.number_input("Idade", value=22) #cria uma caixa com botões de + e - (number_input) que guarda o que "escrevem" ali na variável "idade" 
  #"idade" é o que vai estar escrito em cima | "value=50" > valor inicial que a caixa ja vai começar mostrando
  nota = st.number_input("Nota", value=0.0, step=0.5, min_value=0.0, max_value=10.0) #cria uma caixa do mesmo tipo que idade
  #value=0.0 > ja começa mostrando o valor 0.0 | step = Cada vez que a pessoa clica no botão de + ou -, a nota aumenta ou diminui de 0.5 em 0.5
  #min_value=0.0 e max_value=10.0 >> Impedem o usuário de digitar uma nota menor que zero ou maior que 10.
  
  #------------------------------------
  #cargo = st.text_input("cargo") >>> cria uma caixa de texto com cargo escrito em cima
  #dt_nasc = st.date_input("Data de Nascimento", value="today") >>>> cria uma caixa de data e se clicar mostra uma calendário na tela | "value" : já começa mostrando a data de hoje
  #-----------------------------------------------------------
  btn_cadastro_aluno = st.form_submit_button("Cadastrar") #botão de enviar o formulário e tudo que foi escrito | "enviar" é o que vai aparecer no botão | btn_form > variavel (true or false)

if btn_cadastro_aluno: #"O botão 'enviar' foi clicado?" Se a resposta for Sim (True), o Python entra no bloco e executa as linhas abaixo. Se for Não (False), ele ignora tudo e não mexe no banco
    msg = db.cadastro_aluno(nome, idade, nota)
    st.warning(msg, icon="🔥")

with st.form ("form_delete_aluno"):
    id_aluno = st.number_input("ID do aluno", value=0, step=1, min_value=0)

    btn_delete_aluno = st.form_submit_button("Deletar", 
    help= "Ao clicar aqui você mata uma pessoa") 

if btn_delete_aluno:
   msg = db.delete_aluno(id_aluno)
   st.success(msg)
