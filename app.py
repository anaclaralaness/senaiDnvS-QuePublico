import streamlit as st

import database as db

db.criar_tabela()

st.title("esse é um título")
st.header ("esse é um cabeçalho")
st.subheader ("esse é um cabeçalho menor")

with st.form ("nome_do_formulario"):
  nome = st.text_input("nome")
  idade = st.number_input("idade", value=50)
  nota = st.number_input("Nota", value=0.0, step=0.5, min_value=0.0, max_value=10.0)
  #cargo = st.text_input("cargo")
  #dt_nasc = st.date_input("Data de Nascimento", value="today")
  btn_form = st.form_submit_button("enviar")

if btn_form:
  conn = db.conectar()
  cursor = conn.cursor()

  cursor.execute("INSERT INTO alunos (nome, idade, notas) VALUES (?, ?, ?)", (nome, idade, nota))

  conn.commit()
  conn.close()
#else:
  #st.write(f"o seu nome é {nome}")
