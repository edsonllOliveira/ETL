import pandas as pd
import requests
import time
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

XAI_API_KEY = os.getenv("XAI_API_KEY")

if not XAI_API_KEY:
    raise ValueError(
        "Chave da API não encontrada!\n"
        "Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:\n"
        "XAI_API_KEY= [Coloque a chave aqui]"
    )

BASE_URL = "https://api.x.ai/v1/chat/completions"
MODEL = "grok-3-mini"

print("Iniciando Pipeline ETL com Grok (xAI)")
print("Lendo o arquivo SDW2023.csv...")

df = pd.read_csv("SDW2023.csv")

if "news" not in df.columns:
    df["news"] = ""

df["news"] = df["news"].fillna("").astype(str)


def gerar_news_via_grok(nome: str, max_tentativas: int = 3) -> str:
    """Gera uma frase motivacional usando a API do Grok"""

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Gerando mensagem para: {nome}")

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "Especialista motivacional em finanças pessoais.",
            },
            {
                "role": "user",
                "content": f"Crie uma frase curta e motivadora sobre finanças para {nome}. Máximo 100 caracteres.",
            },
        ],
        "temperature": 0.7,
        "max_tokens": 120,
    }

    headers = {
        "Authorization": f"Bearer {XAI_API_KEY}",
        "Content-Type": "application/json",
    }

    for tentativa in range(1, max_tentativas + 1):
        try:
            response = requests.post(
                BASE_URL, json=payload, headers=headers, timeout=25
            )

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"].strip()

            elif response.status_code == 403:
                print("Acesso negado (403). Usando mensagem padrão.")
                return "Invista no seu futuro com consistência!"

            elif response.status_code == 429:
                print("Rate limit atingido. Aguardando 2 segundos...")
                time.sleep(2)
                continue

            else:
                print(f"Erro {response.status_code}: {response.text[:150]}")

        except Exception as e:
            print(f"Tentativa {tentativa} falhou: {e}")

        if tentativa < max_tentativas:
            time.sleep(1.5)

    return "Que a força financeira esteja com você!"


print(f"\nProcessando {len(df)} registros...\n")

for index, row in df.iterrows():
    texto = gerar_news_via_grok(row["name"])
    df.at[index, "news"] = texto
    time.sleep(0.7)


df.to_csv("SDW2023_finalizado.csv", index=False)

print("\n" + "=" * 50)
print("PROCESSO CONCLUÍDO COM SUCESSO!")
print("=" * 50)
print(f"Total de registros processados: {len(df)}")
print("Arquivo gerado: SDW2023_finalizado.csv")
print("=" * 50)
