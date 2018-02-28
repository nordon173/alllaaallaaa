import telebot
import os
import random


token="554192076:AAG_LTd1yE2rrDle0Z_JRvHAKLVZPvoVKGs"
bot=telebot.TeleBot(token)

#bot.send_message(258340140,"testik")

#upd=bot.get_updates()

#last_upd=upd[-1]
#message_from_user=last_upd.message

#print(message_from_user)


@bot.message_handler(content_types=['text'])
def hendle_text(message):
    if message.text == 'фото':
        directory = 'C:\\Users\\User\\PycharmProjects\\imge'
        all_files_of_directory=os.listdir(directory)
        random_file=random.choice(all_files_of_directory)
        img=open(directory + '/' + random_file,'rb')
        bot.send_chat_action(message.from_user.id,'upload_photo')
        bot.send_photo(message.from_user.id,img)
        img.close()
bot.polling(none_stop=True,interval=0)