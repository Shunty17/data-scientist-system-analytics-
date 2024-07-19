import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as BS
from binance.client import Client
api_key="MMOasCe36TUPKW7JGsWx3UTssqc1KX9YCi6EPl7GcR4OSaGRfG9RxvhqjfdYZ4ps"
api_secret="QW3MShU7xRxXpPW6xGjdpPOCC5fBxfwjdPq9Z0ArJ6c5LtnHnjlZDjSN3gHLvFAj"
client = Client(api_key, api_secret)
token = "1622773631:AAHi87SZ77XQqcQSjPXNc9A9ej8rcihzTiY"
bot = telebot.TeleBot(token)
api_key="MMOasCe36TUPKW7JGsWx3UTssqc1KX9YCi6EPl7GcR4OSaGRfG9RxvhqjfdYZ4ps"
text=False

#Dollar
req=requests.get("https://www.calc.ru/kurs-UAH-USD.html")
soup = BS(req.text,"html.parser")
tbody=soup.find_all("table",cellpadding="0",cellspacing="0")[1]
dollar=tbody.find_all("td",height="25",align="center")[1]
USD=float(dollar.get_text().strip())
print("1 UAH = ", USD,"USD")

#BTC
depth = client.get_order_book(symbol='BTCUSDT')
bids=depth["bids"]
asks=depth["asks"]
b=bids[-1]
s=asks[1]
print("Придбати 1 ВТС та його кількість на Binance ", s,"- https://www.binance.com/en/trade/BTC_USDT?layout=pro")
print("Продати 1 ВТС та готовність купити його на Binance",b,"- https://www.binance.com/en/trade/BTC_USDT?layout=pro")
s1=s[0]
s2=s[-1]
b1=b[0]
b2=b[-1]

main_url="https://liteexchanger.net/exchange-BTC-to-PAYPAL/"
req = requests.get(main_url)
soup = BS(req.text,"html.parser")
first=soup.find("input", class_="js_sum_val js_decimal js_sum2")['value']
print("1(BTC)",first,"$","(PayPal)","-","https://liteexchanger.net/exchange-BTC-to-PAYPAL/")

req = requests.get("https://liteexchanger.net/exchange-BTC-to-VISA_MC_USD/")
soup = BS(req.text,"html.parser")
tw=soup.find("input", class_="js_sum_val js_decimal js_sum2")['value']
print("1(BTC)",tw,"(VISA)","$","-","https://liteexchanger.net/exchange-BTC-to-VISA_MC_USD/")

req = requests.get("https://24atm.net/ru/exchange-btc-to-cardusd/")
soup = BS(req.text,"html.parser")
tr=soup.find("input", class_="js_sum_val js_decimal js_sum2")['value']
print("1(BTC)",tr,"$","(VISA)","-","https://24atm.net/ru/exchange-btc-to-cardusd/")

req = requests.get("https://24atm.net/ru/exchange-btc-to-ppeur/")
soup = BS(req.text,"html.parser")
fr=soup.find("input", class_="js_sum_val js_decimal js_sum2")['value']
print("1(BTC)",fr,"$","(PayPal)","-","https://24atm.net/ru/exchange-btc-to-ppeur/")

#ETH

depth1 = client.get_order_book(symbol='ETHUSDT')
bids1=depth1["bids"]
asks1=depth1["asks"]
a=bids1[-1]
z=asks1[1]
print("Придбати 1 ETH та його кількість на Binance", z,"- https://www.binance.com/en/trade/ETH_USDT?layout=pro")
print("Продати 1 ETH та готовність купити його на Binance",a,"- https://www.binance.com/en/trade/ETH_USDT?layout=pro")
z1=z[0]
z2=z[-1]
a1=a[0]
a2=a[-1]

req = requests.get("https://mychanger.biz/process/Ethereum-KyivUSD.php?fromAmount=1")
soup = BS(req.text,"html.parser")
et1=soup.find("input",id="toAmount", class_="full")['value']
print("1(ETH)",et1,"$","(money)","-","https://mychanger.biz/process/Ethereum-KyivUSD.php?fromAmount=1")


req = requests.get("https://payforia.net/exchange_ETH_to_PRIVAT/")
soup = BS(req.text,"html.parser")
et3=soup.find("input",class_="js_decimal js_sum2")['value']
et3d=float(et3)*USD
et3d=str(et3d)
print("1(ETH)",et3,"UAH","=",et3d,"USD","(privat24)","-","https://payforia.net/exchange_ETH_to_PRIVAT/")

req = requests.get("https://hotexchange.ru/exchange_ETH_to_P24UAH/")
soup = BS(req.text,"html.parser")
et4=soup.find("input",class_="js_sum_val js_decimal js_sum2")['value']
et4d=float(et4)*USD
et4d=str(et4d)
print("1(ETH)",et4,"UAH","=",et4d,"USD","(privat24)","-","https://hotexchange.ru/exchange_ETH_to_P24UAH/")

#XRP
depth2 = client.get_order_book(symbol='XRPUSDT')
bids2=depth2["bids"]
asks2=depth2["asks"]
c=bids2[-1]
v=asks2[1]
c1=c[0]
c2=c[-1]
v1=v[0]
v2=v[-1]
print("Придбати 1 XRP та його кількість на Binance", v1 ,"-",v2,"- https://www.binance.com/en/trade/XRP_USDT?layout=pro")
print("Продати 1 XRP та готовність купити його на Binance",c1,"-", c2,"- https://www.binance.com/en/trade/XRP_USDT?layout=pro")

req = requests.get("https://mychanger.biz/process/Ripple-KyivUSD.php?fromAmount=1")
soup = BS(req.text,"html.parser")
xr1=soup.find("input",maxlength="16",id="toAmount",class_="full")['value']
print("1(XRP)",xr1,"$","(money)","-","https://mychanger.biz/process/Ripple-KyivUSD.php?fromAmount=1")



req = requests.get("https://newline.online/exchange_XRP_2_P24UAH/")
soup = BS(req.text,"html.parser")
xr3=soup.find("input",class_="js_decimal js_sum2")['value']
xr3d=float(xr3)*USD
xr3d=str(xr3d)
print("1(XRP)",xr3,"(UAH) =",xr3d,"(USD) (Privat24)- https://newline.online/exchange_XRP_2_P24UAH/")
print("min.: 180 XRP, max.: 1000 XRP")

#BAT

depth3 = client.get_order_book(symbol='BATUSDT')
bids3=depth3["bids"]
asks3=depth3["asks"]
e=bids3[-1]
q=asks3[1]
e1=e[0]
e2=e[-1]
q1=q[0]
q2=q[-1]
print("Придбати 1 BAT та його кількість на Binance ", e1 ," - ",e2," - https://www.binance.com/en/trade/BAT_USDT?layout=pro&type=spot")
print("Продати 1 BAT та готовність купити його на Binance ",q1," - ", q2," - https://www.binance.com/en/trade/BAT_USDT?layout=pro&type=spot")

req = requests.get("https://mychanger.biz/process/BAT-KyivUSD.php?fromAmount=1")
soup = BS(req.text,"html.parser")
bat1=soup.find("input",maxlength="16",id="toAmount",class_="full")['value']
print("1(BAT)",bat1,"$","(money)","-"," https://mychanger.biz/process/BAT-KyivUSD.php?fromAmount=1")

#BNB
depth4 = client.get_order_book(symbol='BNBUSDT')
bids4=depth4["bids"]
asks4=depth4["asks"]
r=bids4[-1]
t=asks4[1]
r1=r[0]
r2=r[-1]
t1=t[0]
t2=t[-1]
print("Придбати 1 BNB та його кількість на Binance ", t1 ," - ",t2," - https://www.binance.com/en/trade/BNB_USDT?layout=pro&type=spot")
print("Продати 1 BNB та готовність купити його на Binance ",r1," - ", r2," - https://www.binance.com/en/trade/BNB_USDT?layout=pro&type=spot")


req = requests.get("https://mychanger.biz/process/BNB-KyivUSD.php?fromAmount=1")
soup = BS(req.text,"html.parser")
bnb2=soup.find("input",maxlength="16",id="toAmount",class_="full")['value']
print("1(BNB)",bnb2,"$","(money)","-"," https://mychanger.biz/process/BNB-KyivUSD.php?fromAmount=1")

#BCH
depth5 = client.get_order_book(symbol='BCHUSDT')
bids5=depth5["bids"]
asks5=depth5["asks"]
u=bids5[-1]
i=asks5[1]
u1=u[0]
u2=u[-1]
i1=i[0]
i2=i[-1]
print("Придбати 1 BCH та його кількість на Binance ", i1 ," ($)- ",i2," - https://www.binance.com/en/trade/BCH_USDT?layout=pro&type=spot")
print("Продати 1 BCH та готовність купити його на Binance ",u1," ($)- ", u2," - https://www.binance.com/en/trade/BCH_USDT?layout=pro&type=spot")



req = requests.get("https://mychanger.biz/process/BitcoinCash-KyivUSD.php?fromAmount=1")
soup = BS(req.text,"html.parser")
bch2=soup.find("input",maxlength="16",id="toAmount",class_="full")['value']
print("1(BCH)",bch2,"$","(money)","-"," https://mychanger.biz/process/BitcoinCash-KyivUSD.php?fromAmount=1")

#ZEC
depth6 = client.get_order_book(symbol='ZECUSDT')
bids6=depth6["bids"]
asks6=depth6["asks"]
p=bids6[-1]
o=asks6[1]
o1=o[0]
o2=o[-1]
p1=p[0]
p2=p[-1]
print("Придбати 1 ZEC та його кількість на Binance ", o1 ," ($)- ",o2," - https://www.binance.com/en/trade/ZEC_USDT?layout=pro&type=spot")
print("Продати 1 ZEC та готовність купити його на Binance ",p1," ($)- ", p2," - https://www.binance.com/en/trade/ZEC_USDT?layout=pro&type=spot")



req = requests.get("https://mychanger.biz/process/ZCash-KyivUSD.php?fromAmount=1")
soup = BS(req.text,"html.parser")
zec2=soup.find("input",maxlength="16",id="toAmount",class_="full")['value']
print("1(ZEC)",zec2,"$","(money)","-"," https://mychanger.biz/process/ZCash-KyivUSD.php?fromAmount=1")

req = requests.get("https://newline.online/exchange_ZEC_2_P24UAH/")
soup = BS(req.text,"html.parser")
zec3=soup.find("input",class_="js_decimal js_sum2")['value']
zec3d=float(zec3)*USD
zec3d=str(zec3d)
print("1(ZEC)",zec3,"(UAH) =",zec3d,"(USD) (Privat24)- https://newline.online/exchange_ZEC_2_P24UAH/")
print("min.: 1.3 ZEC, max.: 7.2 ZEC")


@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, f"Вітаю вас, {message.chat.first_name}")
    print(message)
    keyboard = types.InlineKeyboardMarkup()
    key_op = types.InlineKeyboardButton(text="Навігація", callback_data='option')
    keyboard.add(key_op)
    bot.send_message(message.chat.id,text="Це новітній телебот для відстеження криптовалюти та їх можливості купівлі продажу" ,reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "option":
        keys = types.ReplyKeyboardMarkup(True, True)
        keys.row("Bitcoin (BTC)","Ethereum (ETH)","Ripple (XRP)")
        keys.row("Basic Attention Token (BAT)","Binance Coin (BNB)")
        keys.row("Bitcoin Cash (BCH)","Zcash (ZEC)")
        keys.row("Profit")
        bot.send_message(call.message.chat.id,text="Також для швидкого звернення до панелі керування введіть команду '/button_menu' ", reply_markup=keys)
        global text
        text = True
@bot.message_handler(commands=['button_menu'])
def keyboard(message):
    keys = types.ReplyKeyboardMarkup(True, True)
    keys.row("Bitcoin (BTC)","Ethereum (ETH)","Ripple (XRP)")
    keys.row("Basic Attention Token (BAT)", "Binance Coin (BNB)")
    keys.row("Bitcoin Cash (BCH)","Zcash (ZEC)")
    keys.row("Profit")
    bot.send_message(message.chat.id,text="Починаеємо роботу", reply_markup=keys)
    global text
    text = True


@bot.message_handler(content_types=['text'])
def coins(message):
    global text
    if message.text=="Bitcoin (BTC)" and text==True :
        bot.send_message(message.chat.id,"Придбати 1 ВТС та його кiлькiсть на Binance "+ s1 +" ($), "+s2+ " - https://www.binance.com/en/trade/BTC_USDT?layout=pro",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"Продати 1 ВТС та готовність купити його на Binance "+ b1 +" ($), "+b2 +" - https://www.binance.com/en/trade/BTC_USDT?layout=pro",disable_web_page_preview = True)

        bot.send_message(message.chat.id,"1(BTC) "+ first+ " $ (PayPal) - https://liteexchanger.net/exchange-BTC-to-PAYPAL/",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"1(BTC) "+ tw+ " (VISA) $ - https://liteexchanger.net/exchange-BTC-to-VISA_MC_USD/",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"1(BTC) "+ tr+ " $ (VISA) - https://24atm.net/ru/exchange-btc-to-cardusd/",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"1(BTC) "+ fr+ " $ (PayPal) - https://24atm.net/ru/exchange-btc-to-ppeur/",disable_web_page_preview = True)

    if message.text=="Ethereum (ETH)" and text==True:
        bot.send_message(message.chat.id,"Придбати 1 ETH та його кількість на Binance "+ z1+ " ($), "+z2+" - https://www.binance.com/en/trade/ETH_USDT?layout=pro",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"Продати 1 ETH та готовність купити його на Binance "+ a1+ " ($), "+a2+" - https://www.binance.com/en/trade/ETH_USDT?layout=pro",disable_web_page_preview = True)

        bot.send_message(message.chat.id,"1(ETH) "+ et1+ " $ (money) - https://mychanger.biz/process/Ethereum-KyivUSD.php?fromAmount=1",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"1(ETH) "+ et3+ " UAH = "+ et3d+ " USD (privat24) -  https://payforia.net/exchange_ETH_to_PRIVAT/",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"1(ETH) "+ et4+ " UAH = "+ et4d+ " USD (privat24) - https://hotexchange.ru/exchange_ETH_to_P24UAH/",disable_web_page_preview = True)

    if message.text =="Ripple (XRP)"  and text == True:
        bot.send_message(message.chat.id,"Придбати 1 XRP та його кількість на Binance "+ v1+ " ($)- "+ v2+" - https://www.binance.com/en/trade/XRP_USDT?layout=pro",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"Продати 1 XRP та готовність купити його на Binance "+ c1+ " ($)- "+ c2+" - https://www.binance.com/en/trade/XRP_USDT?layout=pro",disable_web_page_preview = True)

        bot.send_message(message.chat.id,"1(XRP) "+ xr1+ " $ (money) - https://mychanger.biz/process/Ripple-KyivUSD.php?fromAmount=1",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"min.: 10.3852 XRP, max.: 27 464.6225 XRP ☝")
        bot.send_message(message.chat.id,"1(XRP) "+ xr3+ " (UAH) = "+ xr3d+ " (USD) (Privat24)- https://newline.online/exchange_XRP_2_P24UAH/",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"min.: 180 XRP, max.: 1000 XRP ☝")

    if message.text == "Basic Attention Token (BAT)" and text == True:
        bot.send_message(message.chat.id,"Придбати 1 BAT та його кількість на Binance "+ e1+ " ($)- "+ e2+" - https://www.binance.com/en/trade/BAT_USDT?layout=pro&type=spot",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"Продати 1 BAT та готовність купити його на Binance "+ p1+ " ($)- "+ p2+ " - https://www.binance.com/en/trade/BAT_USDT?layout=pro&type=spot",disable_web_page_preview = True)

        bot.send_message(message.chat.id,"1(BAT) "+ bat1+ " $ (money) -  https://mychanger.biz/process/BAT-KyivUSD.php?fromAmount=1",disable_web_page_preview = True)

    if message.text == "Binance Coin (BNB)" and text == True:
        bot.send_message(message.chat.id,"Придбати 1 BNB та його кількість на Binance "+ t1+ " ($)- "+ t2+" - https://www.binance.com/en/trade/BNB_USDT?layout=pro&type=spot",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"Продати 1 BNB та готовність купити його на Binance "+ r1+ " ($)- "+ r2+" - https://www.binance.com/en/trade/BNB_USDT?layout=pro&type=spot",disable_web_page_preview = True)


        bot.send_message(message.chat.id,"1(BNB)"+ bnb2+ "$ (money) -  https://mychanger.biz/process/BNB-KyivUSD.php?fromAmount=1",disable_web_page_preview = True)


    if message.text == "Bitcoin Cash (BCH)" and text == True:
        bot.send_message(message.chat.id,"Придбати 1 BCH та його кількість на Binance "+ i1+ " ($)- "+ i2+" - https://www.binance.com/en/trade/BCH_USDT?layout=pro&type=spot",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"Продати 1 BCH та готовність купити його на Binance "+ u1+ " ($)- "+ u2+" - https://www.binance.com/en/trade/BCH_USDT?layout=pro&type=spot",disable_web_page_preview = True)

        bot.send_message(message.chat.id,"1(BCH)"+ bch2+ "$"+ "(money)"+ "-"+" https://mychanger.biz/process/BitcoinCash-KyivUSD.php?fromAmount=1",disable_web_page_preview = True)

    if message.text == "Zcash (ZEC)" and text == True:
        bot.send_message(message.chat.id,"Придбати 1 ZEC та його кількість на Binance "+ o1+ " ($)- "+ o2+" - https://www.binance.com/en/trade/ZEC_USDT?layout=pro&type=spot",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"Продати 1 ZEC та готовність купити його на Binance "+ p1+ " ($)- "+ p2+" - https://www.binance.com/en/trade/ZEC_USDT?layout=pro&type=spot",disable_web_page_preview = True)

        bot.send_message(message.chat.id,"1(ZEC)"+ zec2+ "$"+ "(money)"+ "-"+ " https://mychanger.biz/process/ZCash-KyivUSD.php?fromAmount=1",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"1(ZEC)"+ zec3+ "(UAH) ="+ zec3d+ "(USD) (Privat24)- https://newline.online/exchange_ZEC_2_P24UAH/",disable_web_page_preview = True)
        bot.send_message(message.chat.id,"min.: 1.3 ZEC, max.: 7.2 ZEC ☝")

    if message.text == "Profit" and text == True:



        if float(first) > float(s1) and float(first) > float(tw) and float(first) > float(tr) and float(first) > float(fr):
            bot.send_message(message.chat.id,"Придбати 1 ВТС та його кiлькiсть на Binance "+ s1 +" ($), "+s2+ " - https://www.binance.com/en/trade/BTC_USDT?layout=pro",disable_web_page_preview = True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + first + " $ (PayPal) - https://liteexchanger.net/exchange-BTC-to-PAYPAL/",
                             disable_web_page_preview=True)
        elif float(tw)> float(s1) and float(tw)> float(first) and float(tw) > float(tr) and float(tw) > float(fr):
            bot.send_message(message.chat.id,
                             "Придбати 1 ВТС та його кiлькiсть на Binance " + s1 + " ($), " + s2 + " - https://www.binance.com/en/trade/BTC_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + tw + " (VISA) $ - https://liteexchanger.net/exchange-BTC-to-VISA_MC_USD/",
                             disable_web_page_preview=True)
        elif float(tr) > float(s1) and float(tr) > float(first) and float(tr) > float(tw)and float(tr) > float(fr):
            bot.send_message(message.chat.id,
                             "Придбати 1 ВТС та його кiлькiсть на Binance " + s1 + " ($), " + s2 + " - https://www.binance.com/en/trade/BTC_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + tr + " $ (VISA) - https://24atm.net/ru/exchange-btc-to-cardusd/",
                             disable_web_page_preview=True)

        elif float(fr) > float(s1) and float(fr)> float(first) and float(fr) > float(tw) and float(fr) > float(tr):
            bot.send_message(message.chat.id,
                             "Придбати 1 ВТС та його кiлькiсть на Binance " + s1 + " ($), " + s2 + " - https://www.binance.com/en/trade/BTC_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + fr + " $ (PayPal) - https://24atm.net/ru/exchange-btc-to-ppeur/",
                             disable_web_page_preview=True)
        elif float(first) == float(tw):
            bot.send_message(message.chat.id,
                             "Придбати 1 ВТС та його кiлькiсть на Binance " + s1 + " ($), " + s2 + " - https://www.binance.com/en/trade/BTC_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + first + " $ (PayPal) - https://liteexchanger.net/exchange-BTC-to-PAYPAL/",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + tw + " (VISA) $ - https://liteexchanger.net/exchange-BTC-to-VISA_MC_USD/",
                             disable_web_page_preview=True)

        elif float(first) == float(tr):
            bot.send_message(message.chat.id,
                             "Придбати 1 ВТС та його кiлькiсть на Binance " + s1 + " ($), " + s2 + " - https://www.binance.com/en/trade/BTC_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + first + " $ (PayPal) - https://liteexchanger.net/exchange-BTC-to-PAYPAL/",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + tr + " $ (VISA) - https://24atm.net/ru/exchange-btc-to-cardusd/",
                             disable_web_page_preview=True)
        elif float(first) == float(fr):
            bot.send_message(message.chat.id,
                             "Придбати 1 ВТС та його кiлькiсть на Binance " + s1 + " ($), " + s2 + " - https://www.binance.com/en/trade/BTC_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + first + " $ (PayPal) - https://liteexchanger.net/exchange-BTC-to-PAYPAL/",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + fr + " $ (PayPal) - https://24atm.net/ru/exchange-btc-to-ppeur/",
                             disable_web_page_preview=True)
        elif float(tw) == float(tr):
            bot.send_message(message.chat.id,
                             "Придбати 1 ВТС та його кiлькiсть на Binance " + s1 + " ($), " + s2 + " - https://www.binance.com/en/trade/BTC_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + tw + " (VISA) $ - https://liteexchanger.net/exchange-BTC-to-VISA_MC_USD/",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + tr + " $ (VISA) - https://24atm.net/ru/exchange-btc-to-cardusd/",
                             disable_web_page_preview=True)
        elif float(tw) == float(fr):
            bot.send_message(message.chat.id,
                             "Придбати 1 ВТС та його кiлькiсть на Binance " + s1 + " ($), " + s2 + " - https://www.binance.com/en/trade/BTC_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + tw + " (VISA) $ - https://liteexchanger.net/exchange-BTC-to-VISA_MC_USD/",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + fr + " $ (PayPal) - https://24atm.net/ru/exchange-btc-to-ppeur/",
                             disable_web_page_preview=True)
        elif float(tr) == float(fr):
            bot.send_message(message.chat.id,
                             "Придбати 1 ВТС та його кiлькiсть на Binance " + s1 + " ($), " + s2 + " - https://www.binance.com/en/trade/BTC_USDT?layout=pro",
                             disable_web_page_preview=True)

            bot.send_message(message.chat.id,
                             "1(BTC) " + fr + " $ (PayPal) - https://24atm.net/ru/exchange-btc-to-ppeur/",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BTC) " + tr + " $ (VISA) - https://24atm.net/ru/exchange-btc-to-cardusd/",
                             disable_web_page_preview=True)


        if float(et1) > float(z1)  and float(et1) > float(et3d) and float(et1) > float(et4d):
            bot.send_message(message.chat.id,
                             "Придбати 1 ETH та його кількість на Binance " + z1 + " ($), " + z2 + " - https://www.binance.com/en/trade/ETH_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(ETH) " + et1 + " $ (money) - https://mychanger.biz/process/Ethereum-KyivUSD.php?fromAmount=1",
                             disable_web_page_preview=True)

        elif float(et3d) > float(z1) and float(et3d) > float(et1)  and float(et3) > float(et4d):
            bot.send_message(message.chat.id,
                             "Придбати 1 ETH та його кількість на Binance " + z1 + " ($), " + z2 + " - https://www.binance.com/en/trade/ETH_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(ETH) " + et3 + " UAH = " + et3d + " USD (privat24) -  https://payforia.net/exchange_ETH_to_PRIVAT/",
                             disable_web_page_preview=True)

        elif float(et4d) > float(z1) and float(et4d) > float(et1)  and float(et4d) > float(et3d):
            bot.send_message(message.chat.id,
                             "Придбати 1 ETH та його кількість на Binance " + z1 + " ($), " + z2 + " - https://www.binance.com/en/trade/ETH_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(ETH) " + et4 + " UAH = " + et4d + " USD (privat24) - https://hotexchange.ru/exchange_ETH_to_P24UAH/",
                             disable_web_page_preview=True)

        elif float(et1) == float(et3d):
            bot.send_message(message.chat.id,
                             "Придбати 1 ETH та його кількість на Binance " + z1 + " ($), " + z2 + " - https://www.binance.com/en/trade/ETH_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(ETH) " + et1 + " $ (money) - https://mychanger.biz/process/Ethereum-KyivUSD.php?fromAmount=1",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(ETH) " + et3 + " UAH = " + et3d + " USD (privat24) -  https://payforia.net/exchange_ETH_to_PRIVAT/",
                             disable_web_page_preview=True)
        elif float(et1) == float(et4d):
            bot.send_message(message.chat.id,
                             "Придбати 1 ETH та його кількість на Binance " + z1 + " ($), " + z2 + " - https://www.binance.com/en/trade/ETH_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(ETH) " + et1 + " $ (money) - https://mychanger.biz/process/Ethereum-KyivUSD.php?fromAmount=1",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(ETH) " + et4 + " UAH = " + et4d + " USD (privat24) - https://hotexchange.ru/exchange_ETH_to_P24UAH/",
                             disable_web_page_preview=True)

        elif float(et3d) == float(et4d):
            bot.send_message(message.chat.id,
                             "Придбати 1 ETH та його кількість на Binance " + z1 + " ($), " + z2 + " - https://www.binance.com/en/trade/ETH_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(ETH) " + et3 + " UAH = " + et3d + " USD (privat24) -  https://payforia.net/exchange_ETH_to_PRIVAT/",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(ETH) " + et4 + " UAH = " + et4d + " USD (privat24) - https://hotexchange.ru/exchange_ETH_to_P24UAH/",
                             disable_web_page_preview=True)


        if float(xr1) > float(v1)  and float(xr1) > float(xr3d):
            bot.send_message(message.chat.id,
                             "Придбати 1 XRP та його кількість на Binance " + v1 + " ($)- " + v2 + " - https://www.binance.com/en/trade/XRP_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(XRP) " + xr1 + " $ (money) - https://mychanger.biz/process/Ripple-KyivUSD.php?fromAmount=1",
                             disable_web_page_preview=True)


        elif float(xr3d) > float(v1) and float(xr3d) > float(xr1) :
            bot.send_message(message.chat.id,
                             "Придбати 1 XRP та його кількість на Binance " + v1 + " ($)- " + v2 + " - https://www.binance.com/en/trade/XRP_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(XRP) " + xr3 + " (UAH) = " + xr3d + " (USD) (Privat24)- https://newline.online/exchange_XRP_2_P24UAH/",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id, "min.: 180 XRP, max.: 1000 XRP ☝")

        elif float(xr1) == float(xr3d):
            bot.send_message(message.chat.id,
                             "Придбати 1 XRP та його кількість на Binance " + v1 + " ($)- " + v2 + " - https://www.binance.com/en/trade/XRP_USDT?layout=pro",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(XRP) " + xr1 + " $ (money) - https://mychanger.biz/process/Ripple-KyivUSD.php?fromAmount=1",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(XRP) " + xr3 + " (UAH) = " + xr3d + " (USD) (Privat24)- https://newline.online/exchange_XRP_2_P24UAH/",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id, "min.: 180 XRP, max.: 1000 XRP ☝")


        if float(bat1)>float(e1):
            bot.send_message(message.chat.id,
                             "Придбати 1 BAT та його кількість на Binance " + e1 + " ($)- " + e2 + " - https://www.binance.com/en/trade/BAT_USDT?layout=pro&type=spot",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BAT) " + bat1 + " $ (money) -  https://mychanger.biz/process/BAT-KyivUSD.php?fromAmount=1",
                             disable_web_page_preview=True)

        if float(bnb2) > float(t1) :
            bot.send_message(message.chat.id,
                             "Придбати 1 BNB та його кількість на Binance " + t1 + " ($)- " + t2 + " - https://www.binance.com/en/trade/BNB_USDT?layout=pro&type=spot",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BNB)" + bnb2 + "$ (money) -  https://mychanger.biz/process/BNB-KyivUSD.php?fromAmount=1",
                             disable_web_page_preview=True)



        if float(bch2)>float(i1) :
            bot.send_message(message.chat.id,
                             "Придбати 1 BCH та його кількість на Binance " + i1 + " ($)- " + i2 + " - https://www.binance.com/en/trade/BCH_USDT?layout=pro&type=spot",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(BCH)" + bch2 + "$" + "(money)" + "-" + " https://mychanger.biz/process/BitcoinCash-KyivUSD.php?fromAmount=1",
                             disable_web_page_preview=True)




        if float(zec2) > float(o1)  and float(zec2) > float(zec3d):
            bot.send_message(message.chat.id,
                             "Придбати 1 ZEC та його кількість на Binance " + o1 + " ($)- " + o2 + " - https://www.binance.com/en/trade/ZEC_USDT?layout=pro&type=spot",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(ZEC)" + zec2 + "$" + "(money)" + "-" + " https://mychanger.biz/process/ZCash-KyivUSD.php?fromAmount=1",
                             disable_web_page_preview=True)
        elif float(zec3d) > float(o1)  and float(zec3d) > float(zec2):
            bot.send_message(message.chat.id,
                             "Придбати 1 BCH та його кількість на Binance " + o1 + " ($)- " + o2 + " - https://www.binance.com/en/trade/ZEC_USDT?layout=pro&type=spot",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(ZEC)" + zec3 + "(UAH) =" + zec3d + "(USD) (Privat24)- https://newline.online/exchange_ZEC_2_P24UAH/",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id, "min.: 1.3 ZEC, max.: 7.2 ZEC ☝")


        elif float(zec2) == float(zec3d):
            bot.send_message(message.chat.id,
                             "Придбати 1 BCH та його кількість на Binance "  + o1 + " ($)- " + o2 + " - https://www.binance.com/en/trade/ZEC_USDT?layout=pro&type=spot",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(ZEC)" + zec2 + "$" + "(money)" + "-" + " https://mychanger.biz/process/ZCash-KyivUSD.php?fromAmount=1",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id,
                             "1(ZEC)" + zec3 + "(UAH) =" + zec3d + "(USD) (Privat24)- https://newline.online/exchange_ZEC_2_P24UAH/",
                             disable_web_page_preview=True)
            bot.send_message(message.chat.id, "min.: 1.3 ZEC, max.: 7.2 ZEC ☝")



bot.polling()


