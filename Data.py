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
        [InlineKeyboardButton("Iniciar sessão de geração", callback_data="generate")],
        [InlineKeyboardButton(text="Voltar para trás", callback_data="home")]
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
        [InlineKeyboardButton("Meu criador", url"https://t.me/lntocavel")],
    
        # Help Message
    HELP = """
✨ **Comandos disponíveis** ✨

/about - Sobre o bot
/help - Esta mensagem
/start - Inicie o bot
/generate - Iniciar sessão de string
/cancel - Cancelar o processo
/restart - Cancelar o processo
"""

    # About Message
    ABOUT = """
**Sobre este bot** 

 by @AlbedoProjects

Source Code : [Click Here](https://github.com/Intocavel/AlbedoStringGen)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @lntocavel
    """
