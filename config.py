# Arquivo de configuração específica da aplicação

# Ativando o live reload
DEBUG = True

## Configuração para interação com banco de dados
USERNAME = 'Marlon Melo'
PASSWORD = 'supersonicbeatle23${{41'

# Utilização do servidor local
SERVER = 'localhost'

# Nome do banco de dados criado para a aplicação
DB = 'api_flask'

# String de conexão com o banco
SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'

# Alteração automática do modelo ou migration
SQLALCHEMY_TRACK_MODIFICATIONS = True

