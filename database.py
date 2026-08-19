import sqlite3 #importa a biblioteca pra poder trabalhar com o banco de dados do SQLite

def conectar (): #cria a função conectar, então agora toda vez que chamar ela, o programa vai fazer o que ta dentro
  conn = sqlite3.connect("escola.db") #conn = variavel connect | ele guarda a ligação com o banco de dados | quando chamar conn, o python vai ate o arquivo escola.db e conecta "abre a porta" (se nao tiver escola.db, ele cria)
  #--DB = DataBase/Banco de Dados | 
  return conn #retorna o valor de conn, entao traz de volta a conexão com escola db
def criar_tabela() : #cria a função criar_tabela
  conn = conectar() #chama a função conectar que acabou de criar, então faz tudo q tem dentro dela (se conectar com escola db)
  cursor = conn.cursor() #cria a variável cursor | ele vai pegar os seus comandos SQL (como criar tabelas, salvar alunos ou apagar dados) e executar lá dentro do arquivo.
  #Se a conn é a linha telefônica aberta com o banco, o cursor é o mensageiro que vai falar nessa linha. >> analogia do gemini
  cursor.execute("""  
  CREATE TABLE IF NOT EXISTS alunos (  
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT(150) NOT NULL,
  idade INTEGER NOT NULL,
  nota REAL
  )
  """)
#exatamente oq foi dito em cima, o cursor entrou no bano de dados e vai executar algo 
#Crie a tabela 'alunos', mas SÓ SE ELA NÃO EXISTIR | Na primeira vez que o sistema rodar, ele cria a tabela. Nas vezes seguintes, ele percebe que ela já existe e não dá erro.
#-- ID INTEGER PRIMARY KEY AUTOINCREMENT >> Cria a primeira coluna, chamada ID (como se fosse o número do crachá do aluno) | 
#INTEGER: Aceita apenas números inteiros (1, 2, 3...).
#PRIMARY KEY: É a "chave principal". Garante que nenhum aluno tenha o mesmo número que outro.
#AUTOINCREMENT: O banco de dados gera esse número sozinho! O primeiro aluno ganha o ID 1, o segundo ganha o ID 2, e assim por diante.
#-- nome TEXT(150) NOT NULL >> Cria a coluna nome | 
#TEXT(150): Guarda texto (com limite de até 150 letras).
#NOT NULL: Significa "Não pode ficar em branco!". Se tentarem salvar sem nome, o banco recusa.
#-- idade INTEGER NOT NULL>> Cria a coluna idade, que guarda um número inteiro (INTEGER) (ex: 15) e também é de preenchimento obrigatório (NOT NULL).
#-- nota REAL >>Cria a coluna nota
#REAL: É o nome que o banco dá para números com vírgula/ponto (ex: 8.5 ou 10.0). 
#Como não tem o NOT NULL, essa coluna é opcional (o aluno pode ser cadastrado antes de fazer a prova).
  
  conn.commit() #Confirma e salva as alterações e salva em escola.db | Sem essa linha, as mudanças sumiriam assim que o programa fechasse.
  conn.close() #Desconecta o Python do banco e encerra.

#As três aspas (""") servem apenas para o Python aceitar um texto longo pulando várias linhas.
