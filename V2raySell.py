import telebot
from telebot import types
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot("")

button_sell = KeyboardButton('🛒 خرید سرویس')
button_Servises = KeyboardButton('🛍 سرویس های من')
button_charge = KeyboardButton('💸 شارژ حساب')
button_Taarefe = KeyboardButton('🛒 تعرفه خدمات')
button_prifile = KeyboardButton('👤 پروفایل')
button_help = KeyboardButton('🔗 راهنمای اتصال')
button_support = KeyboardButton('📮 پشتیبانی آنلاین')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(button_sell,button_Servises)
greet_kb.add(button_charge,button_Taarefe,button_prifile)
greet_kb.add(button_help,button_support)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, '▪️ کاربر گرامی عضویت شما را به ربات تبریک میگویم ، لطفا یکی از گزینه های زیر را انتخاب نمایید :',
                     reply_markup=greet_kb)

@bot.message_handler(commands=['poo', 'test'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'سلام عرفانم ')

inline_btn_1 = InlineKeyboardButton('10 گیگ 2 کاربره', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('25 گیگ 3 کاربره', callback_data='button2')
inline_btn_3 = InlineKeyboardButton('50 گیگ 4 کاربره', callback_data='button3')
inline_btn_4 = InlineKeyboardButton('70 گیگ 5 کاربره', callback_data='button4')
inline_btn_5 = InlineKeyboardButton('100 گیگ 7 کاربره', callback_data='button5')
inline_btn_25 = InlineKeyboardButton('200 گیگ 10 کاربره', callback_data='button25')
inline_btn_6 = InlineKeyboardButton('🛍پلن دلخواه', callback_data='button6')
inline_btn_7 = InlineKeyboardButton('انصراف', callback_data='button7')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1,inline_btn_2)
inline_kb1.add(inline_btn_3,inline_btn_4)
inline_kb1.add(inline_btn_5,inline_btn_25)
inline_kb1.add(inline_btn_6)
inline_kb1.add(inline_btn_7)
def create_message(location, duration, user_count, storage, price, balance):
    message = (f"مشخصات سرویس مورد نظر ( فاکتور نهایی ) 👇🏻\n\n"
               f"🔘 لوکیشن : {location}\n"
               f"⏳ مدت زمان : {duration} روزه\n"
               f"👤 تعداد کاربر : {user_count} کاربره\n"
               f"♾ حجم سرویس : {storage} گیگ\n\n"
               f"💳 اعتبار کیف پول شما : {balance} تومان\n"
               f"💵 قیمت سرویس : {price} تومان\n\n"
               "📍 برای ساخت سرویس اختصاصی شما و نهایی کردن خرید, روی گزینه تایید و دریافت کلیک کنید.")
    return message

inline_btn_16 = InlineKeyboardButton('🇫🇮فنلاند', callback_data='button16')
inline_btn_17 = InlineKeyboardButton('🇬🇧انگلیس', callback_data='button17')
inline_btn_18 = InlineKeyboardButton("🇹🇷ترکیه", callback_data='button18')
inline_btn_19 = InlineKeyboardButton('🇳🇱هلند', callback_data='button19')
inline_btn_20 = InlineKeyboardButton('🇩🇪آلمان', callback_data='button20')
inline_btn_21 = InlineKeyboardButton("🇫🇷فرانسه", callback_data='button21')
inline_btn_22 = InlineKeyboardButton("📊استعلام وضعیت", callback_data='button22')
inline_btn_23 = InlineKeyboardButton("بازگشت🔙", callback_data='button23')
inline_btn_24 = InlineKeyboardButton('انصراف', callback_data='button24')
inline_kb5 = InlineKeyboardMarkup().add(inline_btn_16,inline_btn_17)
inline_kb5.add(inline_btn_18,inline_btn_19)
inline_kb5.add(inline_btn_20,inline_btn_21)
inline_kb5.add(inline_btn_22)
inline_kb5.add(inline_btn_23,inline_btn_24)

@bot.callback_query_handler(func=lambda c: c.data == 'button16')
def test_callbackb16(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇫🇮فنلاند', 30, 2,10,"50,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button17')
def test_callbackb17(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇬🇧انگلیس',30, 2,10,"50,000",0),
                    reply_markup=greet_kb)    
@bot.callback_query_handler(func=lambda c: c.data == 'button18')
def test_callbackb18(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇹🇷ترکیه',30, 2,10,"50,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button19')
def test_callbackb19(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇳🇱هلند',30, 2,10,"50,000",0),
                    reply_markup=greet_kb)    
@bot.callback_query_handler(func=lambda c: c.data == 'button20')
def test_callbackb20(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇩🇪آلمان',30, 2,10,"50,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button21')
def test_callbackb21(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇫🇷فرانسه',30, 2,10,"50,000",0),
                    reply_markup=greet_kb)
            
inline_btn_26 = InlineKeyboardButton('🇫🇮فنلاند', callback_data='button26')
inline_btn_27 = InlineKeyboardButton('🇬🇧انگلیس', callback_data='button27')
inline_btn_28 = InlineKeyboardButton("🇹🇷ترکیه", callback_data='button28')
inline_btn_29 = InlineKeyboardButton('🇳🇱هلند', callback_data='button29')
inline_btn_30 = InlineKeyboardButton('🇩🇪آلمان', callback_data='button30')
inline_btn_31 = InlineKeyboardButton("🇫🇷فرانسه", callback_data='button31')
inline_kb6 = InlineKeyboardMarkup().add(inline_btn_26,inline_btn_27)
inline_kb6.add(inline_btn_28,inline_btn_29)
inline_kb6.add(inline_btn_30,inline_btn_31)
inline_kb6.add(inline_btn_22)
inline_kb6.add(inline_btn_23,inline_btn_24)

@bot.callback_query_handler(func=lambda c: c.data == 'button26')
def test_callbackb16(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇫🇮فنلاند', 30, 3,25,"85,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button27')
def test_callbackb17(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇬🇧انگلیس',30, 3,25,"85,000",0),
                    reply_markup=greet_kb)    
@bot.callback_query_handler(func=lambda c: c.data == 'button28')
def test_callbackb18(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇹🇷ترکیه',30, 3,25,"85,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button29')
def test_callbackb19(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇳🇱هلند',30, 3,25,"85,000",0),
                    reply_markup=greet_kb)    
@bot.callback_query_handler(func=lambda c: c.data == 'button30')
def test_callbackb20(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇩🇪آلمان',30, 3,25,"85,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button31')
def test_callbackb21(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇫🇷فرانسه',30, 3,25,"85,000",0),
                    reply_markup=greet_kb)  
    
inline_btn_32 = InlineKeyboardButton('🇫🇮فنلاند', callback_data='button32')
inline_btn_33 = InlineKeyboardButton('🇬🇧انگلیس', callback_data='button33')
inline_btn_34 = InlineKeyboardButton("🇹🇷ترکیه", callback_data='button34')
inline_btn_35 = InlineKeyboardButton('🇳🇱هلند', callback_data='button35')
inline_btn_36 = InlineKeyboardButton('🇩🇪آلمان', callback_data='button36')
inline_btn_37 = InlineKeyboardButton("🇫🇷فرانسه", callback_data='button37')
inline_kb7 = InlineKeyboardMarkup().add(inline_btn_32,inline_btn_33)
inline_kb7.add(inline_btn_34,inline_btn_35)
inline_kb7.add(inline_btn_36,inline_btn_37)
inline_kb7.add(inline_btn_22)
inline_kb7.add(inline_btn_23,inline_btn_24)

@bot.callback_query_handler(func=lambda c: c.data == 'button32')
def test_callbackb16(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇫🇮فنلاند', 30, 4,50,"140,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button33')
def test_callbackb17(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇬🇧انگلیس',30, 4,50,"140,000",0),
                    reply_markup=greet_kb)    
@bot.callback_query_handler(func=lambda c: c.data == 'button34')
def test_callbackb18(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇹🇷ترکیه',30, 4,50,"140,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button35')
def test_callbackb19(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇳🇱هلند',30, 4,50,"140,000",0),
                    reply_markup=greet_kb)    
@bot.callback_query_handler(func=lambda c: c.data == 'button36')
def test_callbackb20(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇩🇪آلمان',30, 4,50,"140,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button37')
def test_callbackb21(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇫🇷فرانسه',30, 4,50,"140,000",0),
                    reply_markup=greet_kb)  
    
inline_btn_38 = InlineKeyboardButton('🇫🇮فنلاند', callback_data='button38')
inline_btn_39 = InlineKeyboardButton('🇬🇧انگلیس', callback_data='button39')
inline_btn_40 = InlineKeyboardButton("🇹🇷ترکیه", callback_data='button40')
inline_btn_41 = InlineKeyboardButton('🇳🇱هلند', callback_data='button41')
inline_btn_42 = InlineKeyboardButton('🇩🇪آلمان', callback_data='button42')
inline_btn_43 = InlineKeyboardButton("🇫🇷فرانسه", callback_data='button43')
inline_kb8 = InlineKeyboardMarkup().add(inline_btn_38,inline_btn_39)
inline_kb8.add(inline_btn_40,inline_btn_41)
inline_kb8.add(inline_btn_42,inline_btn_43)
inline_kb8.add(inline_btn_22)
inline_kb8.add(inline_btn_23,inline_btn_24)

@bot.callback_query_handler(func=lambda c: c.data == 'button38')
def test_callbackb16(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇫🇮فنلاند', 30, 5,70,"185,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button39')
def test_callbackb17(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇬🇧انگلیس',30, 5,70,"185,000",0),
                    reply_markup=greet_kb)    
@bot.callback_query_handler(func=lambda c: c.data == 'button40')
def test_callbackb18(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇹🇷ترکیه',30, 5,70,"185,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button41')
def test_callbackb19(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇳🇱هلند',30, 5,70,"185,000",0),
                    reply_markup=greet_kb)    
@bot.callback_query_handler(func=lambda c: c.data == 'button42')
def test_callbackb20(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇩🇪آلمان',30, 5,70,"185,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button43')
def test_callbackb21(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇫🇷فرانسه',30, 5,70,"185,000",0),
                    reply_markup=greet_kb)  

inline_btn_44 = InlineKeyboardButton('🇫🇮فنلاند', callback_data='button44')
inline_btn_45 = InlineKeyboardButton('🇬🇧انگلیس', callback_data='button45')
inline_btn_46 = InlineKeyboardButton("🇹🇷ترکیه", callback_data='button46')
inline_btn_47 = InlineKeyboardButton('🇳🇱هلند', callback_data='button47')
inline_btn_48 = InlineKeyboardButton('🇩🇪آلمان', callback_data='button48')
inline_btn_49 = InlineKeyboardButton("🇫🇷فرانسه", callback_data='button49')
inline_kb9 = InlineKeyboardMarkup().add(inline_btn_44,inline_btn_45)
inline_kb9.add(inline_btn_46,inline_btn_47)
inline_kb9.add(inline_btn_48,inline_btn_49)
inline_kb9.add(inline_btn_22)
inline_kb9.add(inline_btn_23,inline_btn_24)

@bot.callback_query_handler(func=lambda c: c.data == 'button44')
def test_callbackb16(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇫🇮فنلاند', 30, 7,100,"255,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button45')
def test_callbackb17(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇬🇧انگلیس',30, 7,100,"255,000",0),
                    reply_markup=greet_kb)    
@bot.callback_query_handler(func=lambda c: c.data == 'button46')
def test_callbackb18(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇹🇷ترکیه',30, 7,100,"255,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button47')
def test_callbackb19(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇳🇱هلند',30, 7,100,"255,000",0),
                    reply_markup=greet_kb)    
@bot.callback_query_handler(func=lambda c: c.data == 'button48')
def test_callbackb20(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇩🇪آلمان',30, 7,100,"255,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button49')
def test_callbackb21(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇫🇷فرانسه',30, 7,100,"255,000",0),
                    reply_markup=greet_kb)  

inline_btn_50 = InlineKeyboardButton('🇫🇮فنلاند', callback_data='button50')
inline_btn_51 = InlineKeyboardButton('🇬🇧انگلیس', callback_data='button51')
inline_btn_52 = InlineKeyboardButton("🇹🇷ترکیه", callback_data='button52')
inline_btn_53 = InlineKeyboardButton('🇳🇱هلند', callback_data='button53')
inline_btn_54 = InlineKeyboardButton('🇩🇪آلمان', callback_data='button54')
inline_btn_55 = InlineKeyboardButton("🇫🇷فرانسه", callback_data='button55')
inline_kb10 = InlineKeyboardMarkup().add(inline_btn_50,inline_btn_51)
inline_kb10.add(inline_btn_52,inline_btn_53)
inline_kb10.add(inline_btn_54,inline_btn_55)
inline_kb10.add(inline_btn_22)
inline_kb10.add(inline_btn_23,inline_btn_24)

@bot.callback_query_handler(func=lambda c: c.data == 'button50')
def test_callbackb16(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇫🇮فنلاند', 30, 10,200,"300,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button51')
def test_callbackb17(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇬🇧انگلیس',30, 10,200,"300,000",0),
                    reply_markup=greet_kb)    
@bot.callback_query_handler(func=lambda c: c.data == 'button52')
def test_callbackb18(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇹🇷ترکیه',30, 10,200,"300,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button53')
def test_callbackb19(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇳🇱هلند',30, 10,200,"300,000",0),
                    reply_markup=greet_kb)    
@bot.callback_query_handler(func=lambda c: c.data == 'button54')
def test_callbackb20(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇩🇪آلمان',30, 10,200,"300,000",0),
                    reply_markup=greet_kb)
@bot.callback_query_handler(func=lambda c: c.data == 'button55')
def test_callbackb21(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(call.message.chat.id, create_message('🇫🇷فرانسه',30, 10,200,"300,000",0),
                    reply_markup=greet_kb)  

@bot.callback_query_handler(func=lambda c: c.data == 'button1')
def delete_callback(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text='مرحله دوم؛ لطفا لوکیشن موردنظر خودتون رو انتخاب بفرمایید :',reply_markup=inline_kb5)


@bot.callback_query_handler(func=lambda c: c.data == 'button2')
def delete_callback(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text='مرحله دوم؛ لطفا لوکیشن موردنظر خودتون رو انتخاب بفرمایید :',reply_markup=inline_kb6)

@bot.callback_query_handler(func=lambda c: c.data == 'button3')
def delete_callback(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text='مرحله دوم؛ لطفا لوکیشن موردنظر خودتون رو انتخاب بفرمایید :',reply_markup=inline_kb7)

@bot.callback_query_handler(func=lambda c: c.data == 'button4')
def delete_callback(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text='مرحله دوم؛ لطفا لوکیشن موردنظر خودتون رو انتخاب بفرمایید :',reply_markup=inline_kb8)

@bot.callback_query_handler(func=lambda c: c.data == 'button5')
def delete_callback(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.mesFFFsage.message_id)
    bot.send_message(chat_id=call.message.chat.id, text='مرحله دوم؛ لطفا لوکیشن موردنظر خودتون رو انتخاب بفرمایید :',reply_markup=inline_kb9)
@bot.callback_query_handler(func=lambda c: c.data == 'button25')
def delete_callback(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text='مرحله دوم؛ لطفا لوکیشن موردنظر خودتون رو انتخاب بفرمایید :',reply_markup=inline_kb10)




inline_btn_8 = InlineKeyboardButton('پرداخت با درگاه شاپرک (IRR) 💵', callback_data='button8')
inline_btn_9 = InlineKeyboardButton('کارت به کارت 💳', callback_data='button9')
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_8)
inline_kb2.add(inline_btn_9)

inline_btn_10 = InlineKeyboardButton('پرداخت های ریالی 💵', callback_data='button10')
inline_btn_11 = InlineKeyboardButton('پرداخت های ارزی 💎', callback_data='button11')
inline_kb3 = InlineKeyboardMarkup().add(inline_btn_10)
inline_kb3.add(inline_btn_11)
inline_btn_12 = InlineKeyboardButton('📱اندروید', callback_data='button12')
inline_btn_13 = InlineKeyboardButton('🍏آیفون', callback_data='button13')
inline_btn_14 = InlineKeyboardButton('💻مک', callback_data='button14')
inline_btn_15 = InlineKeyboardButton('🖥ویندوز', callback_data='button15')
inline_kb4 = InlineKeyboardMarkup().add(inline_btn_12)
inline_kb4.add(inline_btn_13)
inline_kb4.add(inline_btn_14)
inline_kb4.add(inline_btn_15)

@bot.callback_query_handler(func=lambda c: c.data == 'button4')
def test_callback(call):
        bot.send_message(call.message.chat.id, 'میره ب درگاه پرداخت',
                     reply_markup=greet_kb)
        
@bot.message_handler(content_types=['text'])
def send_text(message):
    if '🛒 خرید سرویس' in message.text:
        bot.send_message(message.chat.id, """🚀 فقط توی 3 مرحله کانفیگ اختصاصی خودت رو دریافت کن !
        
        مرحله اول؛ لطفا پلن موردنظر خودتون رو انتخاب بفرمایید :
        ( تمامی پلان ها 30 روزه میباشند و امکان ارتقا پس از خرید وجود دارد )"""
                                         ,reply_markup=inline_kb1)
       


    elif '🛍 سرویس های من' in message.text:
        bot.send_message(message.chat.id, """‼️ شما هیچ سرویسی ندارید
ابتدا از بخش ' خرید سرویس ' سرویسی تهیه بفرمایید.""")

    elif '💸 شارژ حساب' in message.text:
        bot.send_message(message.chat.id, '⚖️ افزایش موجودی کاملا خودکار است.\n---------------------------------------------------------------------\n〰️ لطفا روش افزایش موجودی را انتخاب بفرمایید',reply_markup=inline_kb2)
    
    elif '🛒 تعرفه خدمات' in message.text:
        bot.send_message(message.chat.id, """
💸 تعرفه کانفیگ اختصاصی و پرسرعت

▪️تعرفه پلن های ثابت
10 گیگ 2 کاربره 50,000 تومان
25 گیگ 3 کاربره 85,000 تومان
50 گیگ 4 کاربره 140,000 تومان
70 گیگ 5 کاربره 185,000 تومان
100 گیگ 7 کاربره 255,000 تومان
200 گیگ 10 کاربره 300,000 تومان
( تمامی پلن های ثابت ، بصورت ماهیانه محاسبه میشود )

▪️تعرفه پلن دلخواه
👈🏻 هر 1 گیگ برابر با 2,000 تومان میباشد.
👈🏻 هر 30 روز اعتبار برابر با 20,000 تومان میباشد.
👈🏻 هر 1 اتصال برابر با 5,000 تومان میباشد.

⭐️ امکان ارتقای سرویس در هر زمان وجود دارد.
""")
    elif '👤 پروفایل'in message.text:
        text = """
👤 شناسه کاربری: ```000000000```
💰 موجودی: 0 تومان

👈🏻 پرداخت های موفق: 0 عدد
👈🏻 *کل سرویس ها : 0 عدد*
🟡 فاکتور های پرداخت نشده : 0 عدد

📞 شماره تلفن : ثبت نشده ❌
🕒 تاریخ عضویت : 1401/11/13
"""

        bot.send_message(message.chat.id, text, parse_mode='Markdown',reply_markup=inline_kb3)
    
    elif '🔗 راهنمای اتصال'in message.text:
        bot.send_message(message.chat.id, "راهنمای اتصال برای کدام سیستم عامل رو میخواهید بدانید ؟",reply_markup=inline_kb4)
   
    elif '📮 پشتیبانی آنلاین' in message.text:
        keyboard = [[InlineKeyboardButton("مشاهده قوانین", url="https://t.me/erfann31")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(chat_id=message.chat.id, text="""
        👈🏻 جهت ارتباط به صورت مستقیم (مشکلات سرویس):
    🆔 @erfann31

    🛑 قبل از ارسال پیام به پشتیبانی،  قوانین سرویس دهی را بخوانید.

    🗯 سؤال، پیشنهاد، مشکل و یا انتقاد خودرا در قالب یک پیام متنی واحد به طور کامل ارسال کنید :""", reply_markup=reply_markup)
    
    else:
        text = "```This text will be in monospace font.```"
        bot.send_message(message.chat.id, text, parse_mode='Markdown')

bot.polling(none_stop=True)
