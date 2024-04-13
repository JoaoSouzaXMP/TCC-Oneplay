# TCC Oneplay 2.0 ![Status](https://img.shields.io/badge/STATUS-Em_Aberto-red) 
![Python](https://img.shields.io/badge/Python-3776AB?style=()&logo=python&logoColor=ffffff) ![Flask](https://img.shields.io/badge/Flask-000000?style=()&logo=flask&logoColor=ffffff) ![SQLServer](https://img.shields.io/badge/SQL_Server-CC2927?style==()&logo=microsoftsqlserver&logoColor=ffffff) ![HTML](https://img.shields.io/badge/HTML-E34F26?style=()&logo=html5&logoColor=ffffff) ![CSS](https://img.shields.io/badge/CSS-1572B6?style=()&logo=css3&logoColor=ffffff) ![GIT](https://img.shields.io/badge/GIT-F05032?style=()&logo=git&logoColor=ffffff) ![VSCode](https://img.shields.io/badge/VS_Code-007ACC?style=()&logo=visualstudiocode&logoColor=ffffff)

## 📚 Introdução

O "Oneplay" é um projeto de Trabalho de Conclusão de Curso (TCC) apresentado ao Curso Técnico em Informática para Internet Integrado ao Ensino Médio da Etec Comendador João Rays. Esta versão é uma reconstrução de um projeto originalmente desenvolvido em ASP.NET e MySql, agora construído com Python, Flask, SQL Server e Git.

## 🎮 Sobre o Projeto

O site "Oneplay" oferece um feed de novidades onde os jogadores podem acessar notícias, curiosidades, atualizações e guias. Além disso, auxilia novos jogadores a criarem uma party dentro do próprio jogo. O objetivo é criar um ambiente de jogo mais colaborativo e interativo, promovendo a troca de experiências entre os jogadores.

Em resumo, "Oneplay" é uma plataforma de jogos online que busca melhorar a experiência do jogador por meio da interação e colaboração. Ele é o resultado de um aprendizado contínuo e da aplicação prática de habilidades de desenvolvimento web backend adquiridas.

## ⚙️ Características do Projeto

- **Persistência de Dados**: Utiliza SQL Server para armazenamento e gerenciamento de dados.
- **Autenticação de Usuários**: Permite a criação e autenticação de usuários.
- **Validação de Formulários**: Implementa a validação de dados de formulários.
- **Criptografia de Senhas**: Assegura a segurança dos usuários através da criptografia de senhas.
- **Proteção CSRF**: Protege contra ataques Cross-Site Request Forgery.
- **Armazenamento de Imagens**: Armazena imagens usando dados binários.
- **Orientação a Objetos**: Manipula informações de forma orientada a objetos.
- **CRUD Completo**: Implementa operações completas de CRUD para jogos.
- **Backup de Banco de Dados**: Possui funcionalidade de backup do banco de dados.
- **Registro de Alteração de Dados**: Possui funcionalidade de registrar a última alteração nas linhas da tabela.

# 📊 Diagrama das tabelas

# 🖥️ Visualização

## 🔧 Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:

- [Git 2.44.0](https://git-scm.com/download/win)
- [Python 3.12.2](https://www.python.org/downloads/release/python-3122/)
- [SQL Server Express 2022](https://www.microsoft.com/pt-br/sql-server/sql-server-2022)

Você também precisará de um editor de código de sua preferência.

> [!IMPORTANT]
> Estes são pré-requisitos essenciais para o projeto. Certifique-se de que todos eles estão instalados corretamente antes de prosseguir.

Após a instalação dos pré-requisitos, você pode seguir com as instruções abaixo.

1. Clone o código fonte:
```git
git clone https://github.com/JoaoSouzaXMP/Projeto-Lista-Jogos.git
```

2. Crie um ambiente virtual para o projeto :
```
python -m venv venv
```

3. Ative o ambiente virtual:
```
.\venv\Scripts\Activate.ps1
```

4. Instale todos os Frameworks:
```
python -m pip install flask Flask-WTF flask-bcrypt pyodbc pyopenssl werkzeug pandas openpyxl ipykernel
```

## Iniciando o Programa
### Ajustes no codigo
Se você instalou a mesma versão do SQL Server e não alterou os parâmetros padrão da instalação, então não precisará ajustar os arquivos. No entanto, se fez alterações, insira as duas variáveis da ConnectionString, o DRIVER e o SERVER, nos arquivos `create_database.ipynb` e `config.py`.


Com todos os ajustes feitos, utilize o seguinte comando para rodar a aplicação:
```
python main.py
```
> [!IMPORTANT]
> O Projeto agora está em execução e pode ser acessado apontando um navegador da web para [`http://localhost:25565/`](http://localhost:25565/)

> [!NOTE]
> Para acessar o projeto de fora da sua rede, utilize seu [`IP Externo`](https://www.invertexto.com/teste-de-portas) ou um [`DNS Dinâmico`](https://www.noip.com/pt-BR) para não ter o trabalho de trocar o IP caso mude. O usuário e senha padrão são `admin` e `1234`, respectivamente.

# Configuração de Backup

Para configurar o backup do banco de dados, precisamos executar o seguinte comando no [`Management Studio (SSMS)`](https://aka.ms/ssmsfullsetup). Altere o caminho conforme a sua escolha.
```sql
CREATE procedure BACKUP_dbOneplay
AS
DECLARE @Caminho varchar(MAX)
DECLARE @Descricao varchar(MAX)
set @Caminho = 'D:\Backups\' + 'dbOneplay' + replace(replace(replace(convert(varchar(20), getdate(), 120), '-',''),':',''),' ','_') + '.bak'
set @Descricao = 'Backup do dia ' + convert(varchar(20), getdate(),120)
backup database dbListaJogos to disk = @caminho with checksum, description = @Descricao
```
# Realizar Backup 
## Pelo CMD.
```bash
sqlcmd -S .\SQLEXPRESS -ddbOneplay -Q "exec BACKUP_dbOneplay"
```
## Pelo Management Studio.
```sql
exec BACKUP_dbOneplay
```

# Automatizando o Backup
Se desejar automatizar o backup, utilize o Agendador de Tarefas do Windows junto a um arquivo .bat conforme os parâmetros abaixo. Edite os caminhos das pastas conforme a sua escolha. É necessário ter o [`7-Zip`](https://www.7-zip.org/download.html) instalado para a compactação.
```bash
@echo Iniciando Processo de Backup do Banco de Dados, aguarde...
@echo Transferindo Backup, aguarde...
@d:
@cd\Backups
@move *.7Z "D:\Backups\Backup_Anterior"

@echo Iniciando Backup, aguarde...
@sqlcmd -S .\SQLEXPRESS -ddbOneplay -Q "exec BACKUP_dbOneplay"

@echo Compactando Backup, aguarde...
For %%f in (*.bak) do ("C:\Program Files\7-Zip\7z.exe" a "%%~nf.7Z" "%%f" -sdel)

@echo Backup Efetuado com Sucesso!

@echo Apagando Backup antigo com mais de 30 dias, aguarde...
forfiles -p "D:\Backups\Backup_Anterior" -s -d -30 -m *.7Z -c "cmd /c del /f /q @path"

@exit
```
