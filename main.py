
def bot(ip,port):
    import telebot
    from grab import Grab
    g = Grab()
    print("Подключаюсь по:",ip,':', port)
    telebot.apihelper.proxy = {'https':'socks5://'+ ip +':'+port}
    bot = telebot.TeleBot('869397424:AAFktmawEJeoEUGejehBuBET4xfumC63ID4')

    @bot.message_handler(commands=['start'])

    def start_message(message):
            bot.send_message(message.chat.id, 'Привет, ты написал мне11111111111 /start')

    @bot.message_handler(commands=['gazval'])
    def start_message(message):
        g.go('http://192.168.100.6:10002/login/WebVision/ses_Fithness/')
        g.set_input('user', 'root')
        g.set_input('pass', 'GfhjkmKf;f123')
        g.submit()
        g.go(f'http://192.168.100.6:10002/WebVision/ses_Fithness1/pg_so/pg_7/pg_mn/pg_1?com=attrsBr&tm')
        gazval = []
        for elem in g.doc.select('//w[*]/el[@id="arg0val"]'): gazval.append(elem.text())
        # bot.send_message(message.chat.id, type(gazval))
        # bot.send_message(message.chat.id, 'Котельная: '+gazval[25])
        # bot.send_message(message.chat.id, 'Энергоцентр: '+gazval[13])
        bot.send_message(message.chat.id, text= '\n'.join(gazval))

    bot.polling()

