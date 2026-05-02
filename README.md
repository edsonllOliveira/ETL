# ETL com IA Generativa - Grok (xAI)

**Desafio:** Explorando IA Generativa em um Pipeline de ETL com Python  
**Bootcamp:** TOTVS - Fundamentos de Engenharia de Dados e Machine Learning - [Digital Innovation One (DIO)](https://www.dio.me)

---

## 📋 Sobre o Projeto

Este projeto implementa um **pipeline ETL (Extract, Transform, Load)** em Python que utiliza a **API do Grok (xAI)** para gerar mensagens personalizadas sobre finanças.

O script lê o arquivo `SDW2023.csv`, gera uma frase curta e motivadora para cada nome e salva o resultado em `SDW2023_finalizado.csv`.

---

## ✨ Funcionalidades

- Leitura de dados via CSV
- Integração com Grok-3-mini (xAI)
- Geração automática de frases motivacionais personalizadas
- Tratamento de erros e retentativas
- Controle de rate limit com delay
- Exportação dos dados enriquecidos

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Pandas**
- **Requests**
- **Grok-3-mini** (xAI API)
- **python-dotenv** (gerenciamento de variáveis de ambiente)

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/edsonllOliveira/ETL.git
cd ETL
2. Instale as dependências
Bashpip install pandas requests python-dotenv
3. Configure sua chave da API
Crie um arquivo .env na raiz do projeto:
envXAI_API_KEY=sua_chave_aqui
4. Prepare o arquivo de entrada
Adicione o arquivo SDW2023.csv na raiz com a coluna name.
5. Execute o pipeline
Bashpython main.py
O arquivo SDW2023_finalizado.csv será gerado automaticamente.

📁 Estrutura do Projeto
text/
├── SDW2023.csv                  # Arquivo de entrada
├── SDW2023_finalizado.csv       # Arquivo de saída (gerado)
├── main.py                      # Script principal do ETL
├── .env                         # Chave da API (não versionar)
├── README.md
└── requirements.txt

🎯 Objetivo do Desafio
Demonstrar na prática a construção de um pipeline ETL utilizando Python integrado com Inteligência Artificial Generativa.

📄 Licença
Este projeto foi desenvolvido para fins educacionais e está sob a licença MIT.

Feito com ❤️ utilizando Grok (xAI)
Por Edson Oliveira
