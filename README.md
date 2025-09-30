API:
    3 endpoints (rotas): 
        Meeting
        Transcripts
        chat

core:
    configuraçoes e banco de dados(conexão)

models


services
    (regras de negócio e integrações externas)
    Exemplos:
    Função que chama a API do Whisper para transcrever.
    Função que recebe um texto e gera um resumo.
    etc

utils
    funções genéricas e auxiliares, que não conhecem a regra de negócio.
    Função para formatar datas.
    Função para fazer log.
    etc


**Tarefas**
Dockstring nas func'ões main
Separar html do main
Detalhar arquiterua primitiva no readme (escrever na lousa antes)
Detalhar dockfile
Escrever arquivo make (libs de cleancode (sonar, lint, bandit, radon, etc))
