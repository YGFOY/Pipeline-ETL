import pandas as pd
import openai

df = pd.read_csv('Pasta1.csv', sep=',')
user_ids = df['UserID'].tolist()
subjects = df['Subject_Test'].tolist()
names = df['Name'].tolist()


openai_api_key = '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'
openai.api_key = openai_api_key


def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
              "role": "system",
              "content": "Você é um universitário do curso de estatística que precisa estudar para uma prova."
            },
            {
                "role": "user",
                "content": f"De para {user['Name']} apenas o nome(titulo) dos 3 principais assuntos para estudar sobre a matéria {user['Subject_Test']}, sem adicionar nennhum outro comentário (separe cada nome por ponto e virgula)"
            }
        ]
    )
    return completion.choices[0].message.content.strip('\"')


messages = []
for idx, id in enumerate(user_ids):
    user = df.iloc[idx]
    news = generate_ai_news(user)
    print(news)
    messages.append(news)

df['Mensagens'] = messages
df.to_csv('Pasta1.csv', index=False)
