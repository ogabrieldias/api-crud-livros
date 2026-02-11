# Boilerplate-Api
Boilerplate de API CRUD

# API
É um lugar para disponibilizar recursos e/ou funcionalidades

# Objetivo
Criar uma API que disponibiliza a consulta, criação, edição e exclusão de livros
 
# URL base
localhost

# Endpoints
localhost/livros (GET) - Consulta <br>
localhost/livros (POST) - Criar novos livros<br>
localhost/livros/id (GET) - Consulta de livro específico por ID<br>
localhost/livros/id (PUT) - Modificação de livro por ID<br>
localhost/livros/id (DELETE) - Deletar por ID

# Recursos
Livros

# Script MySQL

CREATE DATABASE livros; <br>
USE livros; <br>

CREATE TABLE livro ( <br>
&nbsp;    id INT AUTO_INCREMENT PRIMARY KEY, <br>
&nbsp;    titulo VARCHAR(200) NOT NULL, <br>
&nbsp;    autor VARCHAR(100) NOT NULL <br>
); <br>

INSERT INTO livro (titulo, autor) VALUES <br>
('O Senhor dos Anéis - A Sociedade do Anel', 'J.R.R. Tolkien'), <br>
('Harry Potter e a Pedra Filosofal', 'J.K. Rowling'), <br>
('James Clear', 'Hábitos Atômicos'); <br>

SELECT * FROM livro