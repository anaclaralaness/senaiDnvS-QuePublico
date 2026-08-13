//async = cria a função buscardobanco e ela pode ser chamada a qualquer momento
async function buscarDoBanco() {
    /*
    >>em java não precisa declarar o tipo de viravel<<
    -> CONST = uma "variável" que não pode mudar os valores dps ((ela vai receber os valores do localhost
    - AWAIT = bloqueia o código e aguarda a resposta q o java vai mandar pro fetch pra continuar
    - FETCH (trazer/buscar) = vai ate o link q tu colocou e pega a informação de la e traz
    */
    const resposta = await fetch("http://localhost:8080/produtos");

/*RESPOSTA = mensagem que o fetch trouxe de volta que ainda ta em outro tipo de texto
AWAIT = faz o navegador esperar um pouco pra traduzir 
JSON() = traduz pra uma linguagem que o java entenda
*/
    const produtos = await resposta.json();

/* cria uma constante lista
DOCUMENT = a página web que vai mudar algo
getElementById = vai vasculhar a página indo atrás do id de lista produtos
agr qualquer coisa que der pra constante lista vai aparecer na tela do usuário
*/
    const lista = document.getElementById("lista-produtos");
    
/* apaga os dados do banco e da constante que criei. Apaga textos e coisinhas q tem no html da lista
" " = ta falando pra receber nada
*/
    lista.innerHTML = "";

/* pega os produtos q o código puxou do localhost
FOREACH = para cada produto faça isso..
NOMEPRODUTO = pega o nome dos produtos q estavam no localhost
lista.innerHTML = a lista q o codigo acabou de limpar e deixar vazio
+= => manter oq ja ta na lista e adicionar + 1 coisa. Se fosse só = ele ia tirar um e colocar outro
<li> = diz q é uma lista e faz o java fazer topicos pra cada coisa q ele ta recebendo
${} = pega o nome dos produtos e vai colocando em cada topicozinho

Se o banco mandou dois produtos: "Caderno" e "Caneta".
Na primeira volta, o código pega a palavra "Caderno", cria a tag <li>Caderno</li> e gruda na tela.
Na segunda volta, ele pega a palavra "Caneta", cria a tag <li>Caneta</li> e gruda logo abaixo do Caderno. No final, o usuário vê a lista na página
*/
   
    produtos.forEach(nomeProduto => {
        lista.innerHTML += `<li>${nomeProduto}</li>`;
    });
}

//cria a função salvarnoBanco que pode ser chamada a qualquer momento

async function salvarNoBanco() {

/* uma constante chamada input (podia ser qualquer nome mas input é mais lógico pq é onde a gnt digita as coisas
document é a página onde o usuário está
o java pega o id do campo onde digitam nomes e guarda dentro da constante input

cria uma constante chamada texto digitado
input = constante que acabei de criar
como input ta cheio de informação como decoração, cor e tals a gnt coloca:
value = apenas oq o usuário digitou
se ele digitou "lanes é linda" na caixinha do input, textoDigitado agr é "lanes é linda"
*/


    const input = document.getElementById("campo-nome");
    const textoDigitado = input.value;

/* Em JavaScript, sempre que você vê chaves { } (sem ser um bloco de função ou if), significa que estamos criando um Objeto.
cria uma constante chamada objetoProduto
funciona no formato "chave: valor"
colocamos "nome" no objetoproduto pq o java fica esperando ele chegar assim. Se colocar outra coisa além de "nome", o java n vai entender pq ele ta esperando NOME!!
essa parte pega o que o usuário escreveu no input e guarda em objeto pra mandar pro java
*/

    const objetoProduto = { nome: textoDigitado };


    await fetch("http://localhost:8080/produtos", { //da pro fetch o local de onde ele tem que ir e abre as chaves pra dar as instruções pra ele
        method: "POST", //avisa pro fetch que ele não ta indo buscar algo, mas sim enviar pro banco de dados (postar)
        headers: { "Content-Type": "application/json" }, //>>isso são etiquetas e "avisam" pro servidor java que o tipo do conteúdo (Content-Type) é uma aplicação organizada em formato JSON pra ele saber q tem q traduzir
        body: JSON.stringify(objetoProduto) //é o corpo da mensagem. Ela pega o objetoProduto que fizemos (o que o usuário escreveu) e muda ele para uma string pq a internet não consegue transportar objetos, só texto puro ((em formato JSON
    });

    input.value = ""; //pega o que a gnt guardou lá dentro (que acabou virando objetoProduto) e "exclui" ela, limpando a constante input. Aí o usuário pode digitar outras coisas
    buscarDoBanco(); //chama a primeira função de novo e lá vamos nós de novo (recomeça)
}
