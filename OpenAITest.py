from openai import OpenAI
from time import *

client = OpenAI(api_key="sk-python-bot-kT0YKYdzJDRzdi69t7BWT3BlbkFJLP5JUa2l6Lv4Ioh6wAJR")

print("Вы используете ChatGPT 3.5-turbo. Сделайте свой запрос.")

def checkOnRequest():
    Eula = input("Напишите 'Согласен', если вы обязуетесь использовать бота в законных целях для вашего места проживания.\n")
    if Eula.lower() == "согласен":
            request = input("Введите запрос (стоп для отмены): ")
            chat_completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": request}]
            )
            print(chat_completion.choices[0].message)
            time.sleep(5)

    else:
        print("Программа завершена, т.к. вы не согласились с условиями использования(Exit code 0).")

checkOnRequest()