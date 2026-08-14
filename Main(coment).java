import com.sun.net.httpserver.HttpServer; // Ferramenta para criar o Servidor Web.
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;
import com.google.gson.Gson;
import java.io.*;
import java.net.InetSocketAddress;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ServidorApp {
    public static void main(String[] args) throws Exception {
        Connection conexao = DriverManager.getConnection("jdbc:sqlite:meubanco.db");
        Statement stmt = conexao.createStatement();
        stmt.execute("CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)");

        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
        //classe^^ objeto^^
        //cria um contexto produ tos
        server.createContext("/produtos", exchange -> {
            exchange.getResponseHeaders().add("Access-Control-Allow-Origin", "*");
            exchange.getResponseHeaders().add("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
            exchange.getResponseHeaders().add("Access-Control-Allow-Headers", "Content-Type");

            if ("OPTIONS".equals(exchange.getRequestMethod())) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            Gson gson = new Gson();

            if ("GET".equals(exchange.getRequestMethod())) {
                List<String> lista = new ArrayList<>();
                ResultSet rs = stmt.executeQuery("SELECT nome FROM produtos");
                while (rs.next()) {
                    lista.add(rs.getString("nome"));
                }
                
                String jsonResposta = gson.toJson(lista);
                byte[] bytes = jsonResposta.getBytes();
                
                exchange.sendResponseHeaders(200, bytes.length);
                OutputStream os = exchange.getResponseBody();
                os.write(bytes);
                os.close();

            } else if ("POST".equals(exchange.getRequestMethod())) {
                InputStreamReader reader = new InputStreamReader(exchange.getRequestBody());
                Produto produtoRecebido = gson.fromJson(reader, Produto.class);

                PreparedStatement ps = conexao.prepareStatement("INSERT INTO produtos (nome) VALUES (?)");
                ps.setString(1, produtoRecebido.nome);
                ps.executeUpdate();

                String resposta = "Salvo com sucesso!";
                exchange.sendResponseHeaders(201, resposta.length());
                OutputStream os = exchange.getResponseBody();
                os.write(resposta.getBytes());
                os.close();
            }
        });

        server.start();
        System.out.println("Servidor rodando na porta 8080...");
    }
}

class Produto {
    String nome;
}

class Cliente {
    String nome;
}
