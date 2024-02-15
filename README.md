# wallet_bazin_new
A wallet to verify your strategy

Passos para rodar o projeto.

1 - Crie um ambiente virtual e instale as dependências:

python3 -m venv venv
pip3 install -r requirements.txt


2 - Crie o banco de dados local:

python3 create_db.py

*Como é um projeto pessoal e de estudo, estou fazendo com o sqlite, porém, caso necessário, existe a configuração para usar em outros bancos como Postegres já no código, é só descomentar essa parte no src.database.connection.py


3 - Rodar a API:

python3 main.py


4 - Visualizar endpoints:

Digite o seu host:port/docs


