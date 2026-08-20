#a partir daqui vai começar a ser feita a tela do site de acordo com o que foi feito no database.py, então o database.py deve ser feito primeiro


import streamlit as st #importa biblioteca streamlit (é quem cria a tela do site) | as st >> um apelido pra não precisar digitar streamlit sempre: streamlit.title() >>>> st.title()

import database as db #pega o arquivo database.py (que eu criei) e traz todas as funções dele | as db >> cria um apelido pra database

db.criar_tabela() #chama a função criar_tabela que ta no database.py | ele se conecta em escola.db e ve se a tabela alunos ja ta criada, se não tiver ele cria com os comandos de dentro da função

st.title("esse é um título") #cria o título principal do site (função do streamlit)
st.header ("esse é um cabeçalho") #cria o cabeçalho do site
st.subheader ("esse é um cabeçalho menor") #cria um cabeçalhinho pro site

with st.form ("nome_do_formulario"): #cria um formulário | with >> tudo o que tiver indentado embaixo dessa linha ta dentro do formulario 
  #form >> avisa que é um formulário e que só pode enviar o que ta escrito quando clicar no botão
  nome = st.text_input("nome") #cria uma caixa de texto que guarda o que escrevem ali na variável "nome" | ("nome") > vai ficar escrito em cima da caixa
  idade = st.number_input("idade", value=50) #cria uma caixa com botões de + e - (number_input) que guarda o que "escrevem" ali na variável "idade" 
  #"idade" é o que vai estar escrito em cima | "value=50" > valor inicial que a caixa ja vai começar mostrando
  nota = st.number_input("Nota", value=0.0, step=0.5, min_value=0.0, max_value=10.0) #cria uma caixa do mesmo tipo que idade
  #value=0.0 > ja começa mostrando o valor 0.0 | step = Cada vez que a pessoa clica no botão de + ou -, a nota aumenta ou diminui de 0.5 em 0.5
  #min_value=0.0 e max_value=10.0 >> Impedem o usuário de digitar uma nota menor que zero ou maior que 10.
  
  #------------------------------------
  #cargo = st.text_input("cargo") >>> cria uma caixa de texto com cargo escrito em cima
  #dt_nasc = st.date_input("Data de Nascimento", value="today") >>>> cria uma caixa de data e se clicar mostra uma calendário na tela | "value" : já começa mostrando a data de hoje
  #-----------------------------------------------------------
  btn_form = st.form_submit_button("enviar") #botão de enviar o formulário e tudo que foi escrito | "enviar" é o que vai aparecer no botão | btn_form > variavel (true or false)

if btn_form: #"O botão 'enviar' foi clicado?" Se a resposta for Sim (True), o Python entra no bloco e executa as linhas abaixo. Se for Não (False), ele ignora tudo e não mexe no banco
  conn = db.conectar() #chama a função conectar que eu criei no outro arquivo | ele vai no arquivo escola.db, abre a porta e guarda o acesso em conn
  cursor = conn.cursor() #chama o cursor e coloca ele na conexão pra trabalhar (executar as coisas)

  cursor.execute("INSERT INTO alunos (nome, idade, notas) VALUES (?, ?, ?)", (nome, idade, nota)) #cursor pega oq o usuario escreveu e coloca em escola.db
  #INSERT INTO alunos: Diz ao banco "Adicione uma linha nova na tabela de alunos".
  #(nome, idade, notas): Especifica em quais colunas da tabela cada informação deve ser guardada.
  #VALUES (?, ?, ?): Os pontos de interrogação funcionam como "vagas reservadas"
  #, (nome, idade, nota): É a lista com as variáveis contendo o que a pessoa digitou no formulário. O Python pega esses valores e encaixa perfeitamente no lugar de cada ?.

  conn.commit() #salva o que foi feito
  conn.close() #encerra a conexão

  st.success("Aluno cadastrado com sucesso!") #caixinha q mostra uma mensagem de sucesso pro usuario ficar feliz :)
