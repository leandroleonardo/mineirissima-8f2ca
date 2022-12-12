import telebot

CHAVE_API = '5549305809:AAG5nT6tyCory1N2S534ct8tiAsY8m4lCOY'

bot = telebot.TeleBot(CHAVE_API)

# ****************************** Especiarías *****************************


@bot.message_handler(commands=['opcao2', '2', 'dois', 'especiaria'])
def opcao2(mensagem):
    texto = """☕

Algumas opções disponíveis:

/porcoes
/paes
/doces 

Voltar para o /menu"""

    bot.reply_to(mensagem, texto)


# ********** porcoes

@bot.message_handler(commands=['porcoes'])
def opcao2(mensagem):
    texto = """😀 - Porções

Torresmo R$12,00 - 100gm
Pães de queijo R$10,00 - 100gm

Deseja voltar para o /menu ou escolher outra /especiaria?  
"""

    bot.reply_to(mensagem, texto)

# ************** paes


@bot.message_handler(commands=['paes'])
def opcao2(mensagem):
    texto = """🍞 - Pães

Pão Recheado Pizza. Valor: R$31,00 (unidade)
Pão Recheado Três Queijos. Valor: R$32,00 (unidade)
Pão Recheado Calabresa. Valor: R$30,00 (unidade)

Deseja voltar para o /menu ou escolher outra /especiaria?  
"""

    bot.reply_to(mensagem, texto)

# ************** doces


@bot.message_handler(commands=['doces'])
def opcao2(mensagem):
    texto = """🍭 - Doces

Doce de Leite com Coco. Valor: R$25,00 (100gm)
Doce de Leite com Ameixas. Valor: R$25,00 (100gm)
Doce de Abóbora. Valor: R$20,00 (100gm)

Deseja voltar para o /menu ou escolher outra /especiaria?  
"""

    bot.reply_to(mensagem, texto)

# ******************************* Local ***********************


@bot.message_handler(commands=['opcao4'])
def opcao2(mensagem):
    texto = """ 🗺️ - Local!
    
Não estamos em um endereço fisico por enquanto, pois estamos em fase de mudança!.

Deseja voltar para o /menu ?
"""

    bot.reply_to(mensagem, texto)

# ****************************** Orçamento *******************************


@bot.message_handler(commands=['opcao1', '1', 'um'])
def opcao1(mensagem):
    texto = """ Buffes/Festas - 🍽

Informações disponíveis sobre buffes/festas:

/valor
/comidas
/regiao 

Voltar para o /menu """

    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=['valor'])
def opcao1(mensagem):
    texto = """ 🤗 - Valores!
    
Ainda não temos um valor fixo para orçamento! Mas, você pode enviar um e-mail com as informações do evento atráves do formulário que existe em nosso site!

Outras opções: Verifique as /comidas ou /regiao disponível.

Voltar para o /menu """

    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=['comidas'])
def opcao1(mensagem):
    texto = """ 😋 - Comidas!
    
As comidas podem variar conforme o gosto do cliente, mas o gostinho mineiro sempre estará presente!

Outras opções: Verifique os /valores ou /regiao de atendimento. 

Voltar para o /menu """

    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=['regiao'])
def opcao1(mensagem):
    texto = """ 🗺️ - Região!

Atendemos na Região Metropolitana de Piracicaba! E aí, vamos fazer um orçamento?

Outras opções: verifique as /comidas ou /valor de orçamento. 

Voltar para o /menu """

    bot.reply_to(mensagem, texto)

# ****************************** Menu *******************************

# ****************************** Contato ***************************


@bot.message_handler(commands=['contato', 'opcao5'])
def opcao1(mensagem):
    texto = """ ✉ - Contato!

Gostaria de um contato direto? Mande-nos um email diretamente do formulário que existe em nosso site!

Voltar para o /menu """

    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=['menu', 'start'])
def reponder(mensagem):
    texto = """
    
Olá, seja bem-vindo!! Como posso ajudar?

Algumas opções disponíveis: 

/opcao1 Festas/buffes 🍽
/opcao2 Especiarias ☕
/opcao4 Local 🗺
/opcao5 Contato ✉

Para outra dúvida, digite "/" mais a palavra relacionada ao tema, como por exemplo: /doces.

"""

    bot.reply_to(mensagem, texto)


bot.polling()
