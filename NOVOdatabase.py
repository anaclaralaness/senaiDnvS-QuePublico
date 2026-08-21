import sqlite3 #importa a biblioteca pra poder trabalhar com o banco de dados do SQLite

def conectar (): #cria a função conectar, então agora toda vez que chamar ela, o programa vai fazer o que ta dentro
  conn = sqlite3.connect("escola.db") #conn = variavel connect | ele guarda a ligação com o banco de dados | quando chamar conn, o python vai ate o arquivo escola.db e conecta "abre a porta" (se nao tiver escola.db, ele cria)
  #--DB = DataBase/Banco de Dados | 
  return conn #retorna o valor de conn, entao traz de volta a conexão com escola db


#-----------------CREATE------------------
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
#------------------------------------------------------------------------------------------------

###essas partes abaixo vieram do rep. de lohan. obg lohan

#-----------------READ------------------
#decidi colocar duas funções: uma busca por id e outra por nome

def buscar_aluno_id(ID): #cria a função buscar aluno por id | precisa de um parametro (id do aluno)

    conn = conectar() #conecta em escola.db
    cursor = conn.cursor() #vai executar as funções

    cursor.execute( 
        "SELECT * FROM alunos WHERE ID = ?", #SELECT * FROM alunos: Pega todas as colunas da tabela. | WHERE ID = ?: Filtra para buscar apenas os registros onde a coluna ID bate exatamente com a pesquisa
        (ID,) #Passa a variável dentro de uma tupla para o lugar do ?.
    )

    alunos = cursor.fetchone() #guarda o aluno na variável "alunos" ou "None" se não achar ninguem

    conn.close() #fecha a conexão
    return alunos #retorna o resultado da variável alunos

#-------------------------------------------------------------

def cadastro_aluno(nome: str, idade, nota): #tem q botar ":str" pra usar o strip
    
    if nome.strip() == "" : #strip = remove espaços acidentais antes e dps do nome | se não passar nada, ele converte o "none" para ""
        #ex strip: "      ana" >>> "ana"
        return "Nome do aluno não pode ficar em branco."
        
    elif idade > 22:
        return "Idade acima de 22 anos."

    else: #conexao começa agr pra poupar o trabalho de conectar e no final não precisar pq ta errado
        conn = conectar() #chama a função conectar que eu criei | ele vai no arquivo escola.db, abre a porta e guarda o acesso em conn
        cursor = conn.cursor() #chama o cursor e coloca ele na conexão pra trabalhar (executar as coisas)

        cursor.execute("INSERT INTO alunos (nome, idade, nota) VALUES (?, ?, ?)", (nome, idade, nota)) #cursor pega oq o usuario escreveu e coloca em escola.db
             #INSERT INTO alunos: Diz ao banco "Adicione uma linha nova na tabela de alunos".
             #(nome, idade, notas): Especifica em quais colunas da tabela cada informação deve ser guardada.
             #VALUES (?, ?, ?): Os pontos de interrogação funcionam como "vagas reservadas"
             #, (nome, idade, nota): É a lista com as variáveis contendo o que a pessoa digitou no formulário. O Python pega esses valores e encaixa perfeitamente no lugar de cada ?.
        
        conn.commit() #salva o que foi feito
        conn.close() #encerra a conexão
        return ("Aluno cadastrado com sucesso!") #caixinha q mostra uma mensagem de sucesso pro usuario ficar feliz :)
 


#-----------------------------------------

def buscar_aluno_nome(nome): #cria a função buscar aluno com o parâmetro nome
    conn = conectar() #conecta em escola.db
    cursor = conn.cursor() #vai executar as funções


    cursor.execute("SELECT * FROM alunos WHERE nome = ?", (nome,)) #SELECT * FROM alunos: Pega todas as colunas da tabela. | WHERE nome = ?: Filtra para buscar apenas os registros 
  #onde a coluna nome bate exatamente com a pesquisa. | (nome,): Passa a variável dentro de uma tupla para o lugar do ?.
    alunos = cursor.fetchall()  # coloca na variável alunos uma lista com todas as "Anas" achadas 

    conn.close()  #fecha a conexão
    return alunos #retorna o resultado da variável alunos

#-----------------UPDATE------------------

def editar_aluno(id, nome, idade, nota): #cria uma função que edita os parâmetros id, nome, idade, nota
    conn = conectar() #conecta em escola.db
    cursor = conn.cursor() #vai executar as funções

    cursor.execute(" UPDATE alunos SET nome = ?, idade = ?, nota = ? WHERE ID = ?", (nome, idade, nota, id))
  #UPDATE alunos: >> Avisa ao banco que você vai modificar alunos
  #SET nome = ?, idade = ?, nota = ?: >> Especifica quais colunas receberão os novos valores digitados.
  #WHERE ID = ? >> qual aluno vai ser editado de acordo com o id dele
  # (nome, idade, nota, id) >> passa as mudanças dentro de tuplas | precisa estar na ordem dos "?"
  #Se esquecer WHERE em um comando UPDATE, o banco vai alterar os dados de todos os alunos da tabela de uma vez só!

    conn.commit() #salva as mudanças
    conn.close() #fecha a conexão


#-----------------DELETE------------------
def delete_aluno(id): #cria a função para deletar um aluno pedindo id
    if id > 0:
        conn = conectar() #conecta em escola.db
        cursor = conn.cursor() #vai executar as funções

        cursor.execute("DELETE FROM alunos WHERE ID = ?", (id,))
      #DELETE FROM alunos >> Comando SQL para remover registros da tabela.
      #WHERE ID = ? >> pede o id | se não tiver "where" vai apagar a porra toda
      #(id,) >> Passa a variável para o lugar do ?. >>A vírgula no final é o que força o Python a reconhecer isso como uma tupla de um elemento.<<

        conn.commit()  #salva as mudanças
        conn.close() #fecha a conexão
        return f"O aluno de ID {id} foi deletado"
    else:
        return "ID inserido é inválido"
