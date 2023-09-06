# This is Main File

# import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# Config System
from config import BOT_TOKEN, CHANNEL_ID, CHANNEL_URLS

# Extra files
# Cloud Files
from cloud import coll_center_image, discount_image
from cloud import (image1, image2, image3, image4, image5, image6, image7, image8,
                    image9, image10, image11, image12, image13, image14, image15, image16,
                    image17, image18, image19, image20, image21, image22, image23, image24,)


# This is Bot's Basic Settings !
API_TOKEN = Bot(token = BOT_TOKEN, parse_mode="HTML")
bot = Dispatcher(API_TOKEN)
botName = str("Multilevel Zone Bot")

try:
    # logging.basicConfig(level=logging.INFO)


    # This is Main Buttons
    couBut = InlineKeyboardButton(text="🗓 Kurslar", callback_data="cources")
    AscBut = InlineKeyboardButton(text="🈹 Chegirma | Aksiyalar", callback_data="acsi")
    calBut = InlineKeyboardButton(text="📞 Bog`lanish", callback_data="cal")
    resBut = InlineKeyboardButton(text="📔 Natijalar", callback_data="res")
    mulBut = InlineKeyboardButton(text="🆗 Multilevel kurs", callback_data="mull")
    keyboard_inline = InlineKeyboardMarkup().add(couBut, AscBut, calBut)

    keyboards = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3).add(couBut,
                                    AscBut, calBut, resBut, mulBut)



    # This is "Follov" channel buttons function
    def followChannel():
        channel = InlineKeyboardButton(
            text="➡️ Obuna Bo'lish",
            url=CHANNEL_URLS
        )
        check_follow = InlineKeyboardButton(
            text="✅ Tekshirish",
            callback_data="subdone"
        )
        chAllBtn = InlineKeyboardMarkup(row_width=1).add(channel, check_follow)

        return chAllBtn


    @bot.message_handler(commands=['start', 'hello', 'hi', 'restart'])
    async def welcome(message: types.Message):
        checkSubChan = await API_TOKEN.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

        userName = str(message.chat.first_name)
        welTo = f"<b><em>{ userName }</em>, <em>{ botName }</em> - ga xush kelibsiz</b>"

        if checkSubChan['status'] != 'left':
            await message.answer(
                welTo,
                reply_markup=keyboards
            )
        else:
            await message.answer(
                text = f"<b>😳 <em>{ userName }</em>, Botdan foydalanish uchun Kanalimizga obuna bo'ling</b>",
                reply_markup=followChannel()
            )
            
    @bot.callback_query_handler(lambda checkSub: checkSub.data=="subdone")
    async def checkSubMes(callback: types.CallbackQuery):
        checkSubChan = await API_TOKEN.get_chat_member(chat_id=CHANNEL_ID, user_id=callback.from_user.id)
        userName = str(callback.message.chat.first_name)


        if callback.data == "subdone":
            if checkSubChan['status'] != 'left':
                await callback.message.answer(
                    text = f"<b>🥳 <em>{ userName }</em>, Tabriklaymiz endi botimizdan to'liq foydalanishingiz mumkin.</b>",
                    reply_markup=keyboards
                )
            else:
                await callback.message.answer(
                    text = f"<b>❌ <em>{ userName }</em>, hali kanalimizga obuna bo'lmadingiz.</b>",
                    reply_markup=followChannel()
                )



    # All /setcommands. Extra functions.
    @bot.message_handler(commands=['call'])
    async def call_mess(message: types.Message):
        # Connect
        connect = str(f"<b>📲 { botName }</b> - bilan bog'lanish. \n\n📝 <b>Ro'yxatdan o'tish uchun:</b> @otabek_saidakhmadovich \n\n📞 <b>Boshqa ma'lumotlar:</b> +998999357705 \n\n\n <em>🌐 Ijtimoiy Tarmoqlarimiz:</em>    <a href='https://t.me/+mYn6p1pNpfs3NzAy'>📺 Telegram</a>    <a href='https://instagram.com/multilevel_zone?igshid=MjEwN2IyYWYwYw=='>🔗 Instagram</a>")
        
        await message.answer_photo(
                coll_center_image,
                connect
            )
        
    @bot.message_handler(commands=['help'])
    async def help_mess(message: types.Message):
        # Connect
        help_letter = str(f"✅ Qandaydir <b>Muonmo yoki Tushunarsiz</b> holatlarga duch kelgan bo'lsangiz <em>{ botName }</em> - ning hodimlariga telefon qilishingiz yoki ijtimoiy tarmoqlarmimz orqali yozishingiz mumkun. Siz bilan tez bog'lanishga harakat qilamiz. \n\n👥 <b>Murajat uchun:</b> @otabek_saidakhmadovich. \n\n📞 <b>Boshqa ma'lumotlar:</b> +998999357705 \n\n\n<em>🌐 Ijtimoiy Tarmoqlarimiz:</em>    <a href='https://t.me/+mYn6p1pNpfs3NzAy'>📺 Telegram</a>    <a href='https://instagram.com/multilevel_zone?igshid=MjEwN2IyYWYwYw=='>🔗 Instagram</a>")
        
        await message.answer_photo(
                coll_center_image,
                help_letter
            )
        

    @bot.message_handler(commands=['about'])
    async def about_mess(message: types.Message):
        # Connect
        about_letter = str(f"<em><b>🌐 #MULTILEVEL va #IELTS tayyorlanayotganlar DIQQATIGA</b></em> \n\n<em><b>🗓 Kursimiz OKTABR oyida CEFR topshiruvchi O'QITUVCHI va ABITURIYENT lar uchun INTENSIVE KURS</b></em> \n\n<em><b>📊Qo'shilish uchun B1 va B1+ bo'lishingiz kerak</b></em> \n\n<em><b>🗒Kurs davomiyligi 2 oy</b></em> \n\n<em><b>📈Darslar D/CH/J kunlari boladi (haftada 3 marta) + Har dars mock exam bo'ladi</b></em> \n\n<em><b>📉DARSLAR 21:00 da videchat  bo’lib o’tadi</b></em> \n\n<em><b>📝WRITINGLAR to’liq tekshirilib, Ball qoyilib FEEDBACK beriladi</b></em> \n\n<em><b>🎙SPEAKING MOCK olinadi + FEEDBACK beriladi</b></em> \n\n<em><b><a href='https://t.me/coursedata'>➡️ KURS HAQIDA TO'LIQ MA'LUMOT</a></b></em> \n\n\n<em>( 31 ta dars + 31 ta full mock test )</em> \n\n<em><b>📝Ro'yxatdan o'tish uchun :@otabek_saidakhmadovich</b></em> \n\n<em><b>📞More information: +998999357705</b></em> \n\n <em><b><a href='https://t.me/kursimiz_natijalari'>✅ Bu KURS orqali siz C1 va B2 ga erishasiz</a></b></em> \n\n<em><b>🎙SHOSHILING KURSDA JOYLAR SONI CHEKLANGAN. ULGURMAY QOLISHINGIZ MUMKIN</b></em> \n\n\n <em>🌐 Ijtimoiy Tarmoqlarimiz:</em>    <a href='https://t.me/+mYn6p1pNpfs3NzAy'> 📺 Telegram</a>    <a href='https://instagram.com/multilevel_zone?igshid=MjEwN2IyYWYwYw=='>🔗 Instagram</a>")
        
        await message.answer_photo(
                "https://lh3.googleusercontent.com/u/0/drive-viewer/AITFw-yPZZ-q9Zt3LX5UNEdStJi-N2UbFmCglF36SfCozXpvg6xg8ESf1KaqmI-PkSe4yhuSP6NRpklBhue9CDn6FiVGYEJ7=w1380-h966",
                about_letter
            )

    # Main Buttons FUnctions.
    @bot.message_handler(text="🈹 Chegirma | Aksiyalar")
    async def discount_fun(messae: types.Message):
        dis_message = str(f"<em><b>{ botName } - ning Maxsus chegirmasi 💯</b></em> \n\n✅ Bitta taklif qilinganga <b>10%</b> chegirma. \n\n🤩 Beshta taklif qilinganga qursimizning <b>To'liq Chegirma</b>si beriladi. \n\n👥 <em><b>To'liq ma'lumot uchun: @otabek_saidakhmadovich</b></em> \n\n<em><b>📲 Boshqa ma'lumotlar: +998999357705</b></em> \n\n\n<em>🌐 Ijtimoiy Tarmoqlarimiz:</em>    <a href='https://t.me/+mYn6p1pNpfs3NzAy'> 📺 Telegram</a>    <a href='https://instagram.com/multilevel_zone?igshid=MjEwN2IyYWYwYw=='>🔗 Instagram</a>")
        await messae.answer_photo(
            discount_image,
            dis_message
        )


    @bot.message_handler(text="🆗 Multilevel kurs")
    async def mull_get(message: types.Message):
        about_letter = str(f"<em><b>🌐 #MULTILEVEL va #IELTS tayyorlanayotganlar DIQQATIGA</b></em> \n\n<em><b>🗓 Kursimiz OKTABR oyida CEFR topshiruvchi O'QITUVCHI va ABITURIYENT lar uchun INTENSIVE KURS</b></em> \n\n<em><b>📊Qo'shilish uchun B1 va B1+ bo'lishingiz kerak</b></em> \n\n<em><b>🗒Kurs davomiyligi 2 oy</b></em> \n\n<em><b>📈Darslar D/CH/J kunlari boladi (haftada 3 marta) + Har dars mock exam bo'ladi</b></em> \n\n<em><b>📉DARSLAR 21:00 da videchat  bo’lib o’tadi</b></em> \n\n<em><b>📝WRITINGLAR to’liq tekshirilib, Ball qoyilib FEEDBACK beriladi</b></em> \n\n<em><b>🎙SPEAKING MOCK olinadi + FEEDBACK beriladi</b></em> \n\n<em><b><a href='https://t.me/coursedata'>➡️ KURS HAQIDA TO'LIQ MA'LUMOT</a></b></em> \n\n\n<em>( 31 ta dars + 31 ta full mock test )</em> \n\n<em><b>📝Ro'yxatdan o'tish uchun :@otabek_saidakhmadovich</b></em> \n\n<em><b>📞More information: +998999357705</b></em> \n\n <em><b><a href='https://t.me/kursimiz_natijalari'>✅ Bu KURS orqali siz C1 va B2 ga erishasiz</a></b></em> \n\n<em><b>🎙SHOSHILING KURSDA JOYLAR SONI CHEKLANGAN. ULGURMAY QOLISHINGIZ MUMKIN</b></em> \n\n\n <em>🌐 Ijtimoiy Tarmoqlarimiz:</em>    <a href='https://t.me/+mYn6p1pNpfs3NzAy'> 📺 Telegram</a>    <a href='https://instagram.com/multilevel_zone?igshid=MjEwN2IyYWYwYw=='>🔗 Instagram</a>")
        
        await message.answer_photo(
                "https://lh3.googleusercontent.com/u/0/drive-viewer/AITFw-yPZZ-q9Zt3LX5UNEdStJi-N2UbFmCglF36SfCozXpvg6xg8ESf1KaqmI-PkSe4yhuSP6NRpklBhue9CDn6FiVGYEJ7=w1380-h966",
                about_letter
            )

    @bot.message_handler(text="📞 Bog`lanish")
    async def call_mess(message: types.Message):
        connect = str(f"<b>📲 { botName }</b> - bilan bog'lanish. \n\n📝 <em><b>Ro'yxatdan o'tish uchun: @otabek_saidakhmadovich</b></em> \n\n📞 <em><b>Boshqa ma'lumotlar: +998999357705</b></em> \n\n\n <em>🌐 Ijtimoiy Tarmoqlarimiz:</em>    <a href='https://t.me/+mYn6p1pNpfs3NzAy'>📺 Telegram</a>    <a href='https://instagram.com/multilevel_zone?igshid=MjEwN2IyYWYwYw=='>🔗 Instagram</a>")
        
        await message.answer_photo(
                coll_center_image,
                connect
            )
        
    @bot.message_handler(text="📔 Natijalar")
    async def recult_mess(message: types.Message):
        await message.answer(
            text=f"<em><b>✅ Kusimizning Natijalari</b></em>"
        )

        await asyncio.sleep(2)
        await message.answer_photo(image1)
        await message.answer_photo(image2)
        await message.answer_photo(image3)
        await message.answer_photo(image4)
        await message.answer_photo(image5)
        await message.answer_photo(image6)
        await message.answer_photo(image7)
        await message.answer_photo(image8)

        await message.answer_photo(image9)
        await message.answer_photo(image10)
        await message.answer_photo(image11)
        await message.answer_photo(image12)
        await message.answer_photo(image13)
        await message.answer_photo(image14)
        await message.answer_photo(image15)
        await message.answer_photo(image16)
        await message.answer_photo(image17)
        await message.answer_photo(image18)
        await message.answer_photo(image19)
        await message.answer_photo(image20)
        await message.answer_photo(image21)
        await message.answer_photo(image22)
        await message.answer_photo(image23)
        await message.answer_photo(image24)


    @bot.message_handler()
    async def kb_answer(message: types.Message):
        # Cources List
        cources_message = str(f"<em><b>🔎 { botName } - Kurslarimiz bilan tanishishingiz mumkin bo'ladi. Ma`lumot olish uchun tanlang.</b></em>")
        course_buttons = [
            [
                types.InlineKeyboardButton(text="✅ Multilevel kurs", callback_data="multilevel"),
            ],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=course_buttons)

        # Connect

        if message.text == '🗓 Kurslar':
            await message.reply(
                cources_message,
                reply_markup=keyboard
            )
        else:
            await message.reply(f"{ message.chat.first_name }, Mavjud bo'lmaan buyruq kiritdingiz \"{ message.text }\" \nBosha so`z yozing...")


    @bot.callback_query_handler(lambda callback_query: callback_query.data == 'multilevel')
    async def mul_get(mul_data: types.CallbackQuery) -> str:
        about_letter = str(f"<em><b>🌐 #MULTILEVEL va #IELTS tayyorlanayotganlar DIQQATIGA</b></em> \n\n<em><b>🗓 Kursimiz OKTABR oyida CEFR topshiruvchi O'QITUVCHI va ABITURIYENT lar uchun INTENSIVE KURS</b></em> \n\n<em><b>📊Qo'shilish uchun B1 va B1+ bo'lishingiz kerak</b></em> \n\n<em><b>🗒Kurs davomiyligi 2 oy</b></em> \n\n<em><b>📈Darslar D/CH/J kunlari boladi (haftada 3 marta) + Har dars mock exam bo'ladi</b></em> \n\n<em><b>📉DARSLAR 21:00 da videchat  bo’lib o’tadi</b></em> \n\n<em><b>📝WRITINGLAR to’liq tekshirilib, Ball qoyilib FEEDBACK beriladi</b></em> \n\n<em><b>🎙SPEAKING MOCK olinadi + FEEDBACK beriladi</b></em> \n\n<em><b><a href='https://t.me/coursedata'>➡️ KURS HAQIDA TO'LIQ MA'LUMOT</a></b></em> \n\n\n<em>( 31 ta dars + 31 ta full mock test )</em> \n\n<em><b>📝Ro'yxatdan o'tish uchun :@otabek_saidakhmadovich</b></em> \n\n<em><b>📞More information: +998999357705</b></em> \n\n <em><b><a href='https://t.me/kursimiz_natijalari'>✅ Bu KURS orqali siz C1 va B2 ga erishasiz</a></b></em> \n\n<em><b>🎙SHOSHILING KURSDA JOYLAR SONI CHEKLANGAN. ULGURMAY QOLISHINGIZ MUMKIN</b></em> \n\n\n <em>🌐 Ijtimoiy Tarmoqlarimiz:</em>    <a href='https://t.me/+mYn6p1pNpfs3NzAy'> 📺 Telegram</a>    <a href='https://instagram.com/multilevel_zone?igshid=MjEwN2IyYWYwYw=='>🔗 Instagram</a>")
        
        await mul_data.message.answer_photo(
                "https://lh3.googleusercontent.com/u/0/drive-viewer/AITFw-yPZZ-q9Zt3LX5UNEdStJi-N2UbFmCglF36SfCozXpvg6xg8ESf1KaqmI-PkSe4yhuSP6NRpklBhue9CDn6FiVGYEJ7=w1380-h966",
                about_letter
            )



    # ALl errors
    # All posible errors will pass through here

    @bot.errors_handler(exception = ['BotBlocked', 'TimeoutError', 'TypeError'])
    async def bot_block(update: types.Update, excention: Exception):
        print(f"I think The Bot was blocked by the User { update } { excention }")
        return True

except:
    executor.start_polling(dispatcher=bot, skip_updates=True)




if __name__ == '__main__':
    executor.start_polling(dispatcher=bot, skip_updates=True)