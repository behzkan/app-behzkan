from asyncio import sleep
from random import choice, randint
from aiogram import types, Dispatcher
from utils.util import play_stroke_anim, play_anim, _get_heart_stickers

async def cmd_sponge(msg: types.Message):
    msg = await msg.answer('msg')
    text = (
        "╲┏━┳━━━━━━━━┓╲╲",
        "╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲",
        "╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲",
        "╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲",
        "╲┃◯┃╭╮╰╯┏━━━┳╯╲",
        "╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲",
        "╲┃╰┃◯╰┗┛┗┛╯╭┃╲╲",
    )
    await play_stroke_anim(msg, text)


async def cmd_hare(msg: types.Message):
    msg = await msg.answer('1')
    left_eyes = '┈┃▋▏▋▏┃┈'
    right_eyes = '┈┃╱▋╱▋┃┈'
    img = [
        '╭━━╮╭━━╮',
        '╰━╮┃┃╭━╯',
        '┈╭┛┗┛┗╮┈',
        '┈┃╱▋╱▋┃┈',
        '╭┛▔▃▔┈┗╮',
        '╰┓╰┻━╯┏╯',
        '╭┛┈┏┓┈┗╮',
        '╰━━╯╰━━╯',
    ]
    eyes = choice((True, False))
    img[3] = right_eyes if eyes else left_eyes
    await play_stroke_anim(msg, img)
    await sleep(1)

    for _ in range(randint(5, 10)):
        eyes = not eyes
        img[3] = right_eyes if eyes else left_eyes
        await msg.edit_text('\n'.join(img))
        await sleep(0.3)



async def cmd_bomb(msg: types.Message):
    msg = await msg.answer('s')
    row = '▪️▪️▪️▪️\n'
    bombs = '💣 💣 💣 💣\n'
    fire = '💥 💥 💥 💥\n'
    smile = '😵 😵 😵 😵\n'
    words = (
        f"{row}{row}{row}{row}{row}",
        f"{bombs}{row}{row}{row}{row}",
        f"{row}{bombs}{row}{row}{row}",
        f"{row}{row}{bombs}{row}{row}",
        f"{row}{row}{row}{bombs}{row}",
        f"{row}{row}{row}{row}{bombs}",
        f"{row}{row}{row}{row}{fire}",
        f"{row}{row}{row}{fire}{fire}",
        f"{row}{row}{row}{row}{smile}"
    )
    await play_anim(msg, words)


async def __stupid(msg: types.Message):
    msg = await msg.answer('1')
    first_str = 'YOUR BRAIN ➡️ 🧠\n\n🧠'
    second_str = 'YOUR BRAIN ➡️ 🧠\n\n'
    words = (
        f'{first_str}         (^_^)🗑',
        f'{first_str}       (^_^)  🗑',
        f'{first_str}     (^_^)    🗑',
        f'{first_str}   (^_^)      🗑',
        f'{first_str} (^_^)        🗑',
        f'{first_str} <(^_^ <)     🗑',
        f'{second_str}(> ^_^)>🧠   🗑',
        f'{second_str} (> ^_^)>🧠  🗑',
        f'{second_str}  (> ^_^)>🧠 🗑',
        f'{second_str}   (> ^_^)>🧠🗑',
        f'{second_str}       (^_^) 🗑',
        f'{second_str}        (3_3)🗑'
    )
    await play_anim(msg, words)


async def __compli(msg: types.Message):
    msg = await msg.answer('1')
    words = (
        'удивительная', 'внимательная', 'красивая', 'лучшая', 'успешная', 'заботливая', 'милая', 'прекрасная',
        'умная', 'шикарная', 'обалденная', 'очаровашка', 'любимая', 'весёлая', 'нежная', 'яркая', 'прелестная',
        'приятная', 'сладкая', 'дивная', 'ангельская', 'добрая', 'бесподобная', 'волшебная', 'крутышка', 'смелая',
        'ласковая', 'романтичная', 'великолепная', 'внимательная', 'страстная', 'игривая', 'единственная',
        'стройная', 'безумная', 'симпатичная', 'изящная', 'талантливая', 'элегантная', 'чуткая', 'уникальная',
    )
    await msg.edit_text('<b>Крошечные напоминания того, что ты...</b>', parse_mode=types.ParseMode.HTML)
    await sleep(1)

    for word in words:
        await msg.edit_text(f'Cамая {choice(words)}✨')
        await sleep(0.5)
    await msg.edit_text(f'Cамая {choice(words)}✨')

async def __heart(msg: types.Message):
    msg = await msg.answer('1')
    img = _get_heart_stickers()
    for anim in img:
        await msg.edit_text('\n'.join(anim))
        await sleep(1)

def register_msg_handler(dp: Dispatcher):
    dp.register_message_handler(cmd_sponge, commands='sponge')
    dp.register_message_handler(cmd_bomb, commands='bomb')
    dp.register_message_handler(__stupid, commands='stupid')
    dp.register_message_handler(__compli, commands='compli')
