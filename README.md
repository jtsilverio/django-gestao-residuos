# Gestão de Resíduos
- Tema do frontend: https://demo.themesberg.com/volt/pages/dashboard/dashboard.html
  - https://themesberg.com/docs/volt-bootstrap-5-dashboard/components/widgets/


# Set up para desenvolvimento:
- instalar as dependencias de desenvolvimento usando: `pip install -r requirements-dev.txt`
- para rodar o servidor de denvolvimento: `python manage.py runserver`

# Estrutura
```
.
├── _dev        Alguns arquivos de criação e preenchimento de tabelas
├── classe      App para cadastro e listagem de Classes de Resíduos
├── core        Configurações do projeto
├── docs        Arquivos de documentação
├── entrada     App para cadastro e listagem da Entrada de Resíduos
├── fornecedor  App para cadastro e listagem de Fornecedores de Serviço
├── home        App para a página de Home
├── localidade  App para cadastro e listagem de Localidades/Franquias
├── saida       App para cadastro e listagem da Saída de Resíduos
└── templates   Templates HTML de cada um dos Apps
``` 