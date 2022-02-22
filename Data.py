from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Ei {}

Bem-vindo ao {}

Se você não confia neste bot,
1) pare de ler esta mensagem
2) excluir este bate-papo

Ainda lendo?
Você pode me usar para gerar pirograma e sessão de cordas de teleton. Use os botões abaixo para saber mais !

By @AlbedoProjects
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Iniciar sessão de geração de string", callback_data="generate")],
        [InlineKeyboardButton(text="Voltar para casa", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("Iniciar sessão de geração", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Iniciar sessão de geração", callback_data="generate")],
        [InlineKeyboardButton("Status do bot", url="https://t.me/AlbedoProjects")],
        [
            InlineKeyboardButton("Como usar ❔", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
        ],
        [InlineKeyboardButton("Saber sobre meu dono", url="https://t.me/LookRight")],
    ]

    # Help Message
    HELP = """
**Comandos disponíveis**

/about - Sobre o bot
/help - Para ajuda
/start - Inicie o bot
/generate - Iniciar sessão de geração
/cancel - Cancelar o processo
/restart - Cancelar o processo
"""

    # About Message
    ABOUT = """
**Sobre este bot** 

Um bot telegram para gerar sessão de string pyrogram e teleton por @lntocavel

Source Code : [Click Here](https://github.com/Intocavel/AlbedoStringGen)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @lntocavel
    """
