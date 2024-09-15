import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, types

API_TOKEN = 'SomeToken'

sents = [
    "Я не знаю, подумай сам.",
    "Я не могу тебе помочь, думай сам.",
    "Решение лежит на тебе, подумай хорошенько.",
    "Это твоя задача, подумай сам.",
    "Только ты можешь найти ответ, подумай внимательно.",
    "Думай глубже, я не знаю.",
    "Это вопрос для размышлений, подумай сам.",
    "Пусть это станет твоим уроком, подумай самостоятельно.",
    "Это важное решение, требует внимательного обдумывания.",
    "Время принимать решения, думай сам.",
    "Только ты знаешь ответ, подумай внимательно.",
    "Я не могу решить за тебя, подумай сам.",
    "Решение в твоих руках, думай сам.",
    "Необходимо самостоятельно понять, что делать.",
    "Подумай хорошо, решение будет твое.",
    "Исход зависит от твоих размышлений, подумай сам.",
    "Тебе стоит самостоятельно принять решение.",
    "Только ты знаешь правильный путь, думай сам.",
    "Рассматривай варианты и принимай решение самостоятельно.",
    "Подумай о последствиях, прежде чем принимать решение.",
    "Решение зависит от твоего внутреннего чувства, думай сам.",
    "Обдумай все аспекты проблемы, прежде чем принимать решение.",
    "Думай креативно, решение будет индивидуальным.",
    "Ищи ответ в себе, подумай самостоятельно.",
    "Не буду давать подсказок, нужно думать самостоятельно.",
    "Задача требует твоего внимания и усилий, думай сам.",
    "Только ты знаешь, что лучше всего для тебя, подумай внимательно.",
    "Прояви творческий подход к проблеме, думай сам.",
    "Думай извне коробки, решение может быть нестандартным.",
    "Решение будет индивидуальным, думай самостоятельно.",
    "Только ты можешь принять окончательное решение, подумай внимательно.",
    "Время принять решение, думай самостоятельно.",
    "Размышляй о возможных вариантах действий, прежде чем принимать решение.",
    "Вопрос доверия и интуиции, думай сам.",
    "Только ты знаешь все аспекты ситуации, подумай внимательно.",
    "Не спешите, решение требует вдумчивости, думайте самостоятельно.",
    "Решение находится в тебе, подумай сам.",
    "Что бы ты ни выбрал, думай рационально и основательно.",
    "Дай себе время на размышления, ответ появится сам.",
    "Прояви свою самостоятельность, решение будет твоим.",
    "Решение зависит только от тебя, подумай внимательно.",
    "Думай креативно, ответ будет индивидуальным.",
    "Решение в твоих руках, думай самостоятельно.",
    "Только ты можешь решить этот вопрос, подумай внимательно.",
    "Не спеши на решение, обдумывай внимательно, думай сам.",
    "Тебе стоит самостоятельно исследовать вопрос, думай сам.",
    "Рассмотрите все возможные варианты, прежде чем принимать решение.",
    "Принятие решения требует внимательного анализа, думай внимательно.",
    "Только ты знаешь свои желания и цели, подумай самостоятельно.",
    "Решение зависит только от тебя, думай внимательно.",
    "Не торопись, решение требует взвешенного подхода и анализа, думай сам.",
    "Решение будет твоим, думай сам.",
    "Прояви свой характер и прими твердое решение, подумай самостоятельно.",
    "Решение будет индивидуальным, подумай внимательно.",
    "Время делать выбор, думай сам.",
    "Только ты знаешь все детали ситуации, подумай внимательно.",
    "Исход зависит от твоего решения, думай сам.",
    "Необходимо самостоятельно исследовать вопрос, думай сам.",
    "Решение находится внутри тебя, подумай внимательно.",
    "Решение зависит от твоего понимания ситуации, думай сам.",
    "Дай себе время на размышления, ответ придет сам.",
    "Тебе стоит принять собственное решение, думай самостоятельно.",
    "Решение будет индивидуальным, думай внимательно.",
    "Время действовать, подумай сам.",
    "Только ты можешь найти правильный путь, думай сам.",
    "Не спешите с решением, требуется вдумчивость, думайте самостоятельно.",
    "Самостоятельное принятие решения развивает креативность, подумай сам.",
    "Решение является ключом к твоему успеху, думай сам.",
    "Решение находится в твоей голове, думай внимательно.",
    "Только ты можешь найти ответ, обдумай внимательно.",
    "Сосредоточься на проблеме, ответ придет тебе сам.",
    "Рассмотрите все стороны вопроса, прежде чем принимать решение.",
    "Дай себе время на размышления, результат появится самостоятельно.",
    "Прояви инициативу и уверенность в принятии решения, подумай сам.",
    "Решение зависит от твоей ответственности и интуиции, думай самостоятельно.",
    "Не теряй время, думай вразумительно и обдуманно, думай сам.",
    "Решение будет твоим, только ты знаешь путь, думай внимательно.",
    "Прояви свой характер и прими решение, подумай сам.",
    "Решение - это твое дело, думай сам, подумай хорошо.",
    "Только ты можешь ответить на этот вопрос, подумай внимательно.",
    "Необходимо самостоятельно рассмотреть проблему, думай сам.",
    "Ищи решение в себе, подумай самостоятельно.",
    "Решение в твоих руках, думай креативно и самостоятельно.",
    "Только ты можешь найти ответ, думай сам.",
    "Рассмотрите все стороны вопроса, перед тем как принимать решение.",
    "Решение находится в тебе, подумай внимательно.",
    "Решение зависит от твоего понимания, думай сам.",
    "Не спешите с решением, дайте себе время на размышление, подумай самостоятельно.",
    "Решение будет индивидуальным, думай внимательно.",
    "Время принять решение, подумай сам.",
    "Только ты можешь найти правильный путь, думай сам.",
    "Неспеша принимай решение, требуется вдумчивое обдумывание, думайте самостоятельно.",
    "Прояви свой креативный подход в принятии решения, думай сам.",
    "Решение - ключ к твоему успеху, подумай сам.",
    "Решение зависит от твоего размышления, думай внимательно.",
    "Только ты знаешь ответ, думай внимательно.",
    "Проанализируй проблему, ответ предстанет перед тобой сам.",
    "Рассмотрите возможные варианты, прежде чем принимать решение.",
    "Дай себе время на раздумье, ответ придет сам.",
    "Прими самостоятельное решение, подумай самостоятельно.",
    "Решение будет индивидуальным, думай внимательно.",
    "Иди вперед и действуй, думай сам."
]

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)

dp=Dispatcher()

@dp.message()
async def default(message : types.Message):
    print(message.text)
    await bot.send_message(message.from_user.id, random.choice(sents))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
