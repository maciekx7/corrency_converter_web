from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def exchange_import_from_page(currency, currency_1):
    p = {"s": currency + currency_1}
    odpowiedz = requests.get("http://stooq.pl/q/?", params=p)
    soup = BeautifulSoup(odpowiedz.text, 'html.parser')
    exchange_mark = soup.find("span", id=f"aq_{currency}{currency_1}_c5")
    exchange = float(exchange_mark.text)
    return exchange

def page(requests):
	return render(requests,'mysite/page.html')


def output(request):
	cur1=request.POST["cur1"]
	cur2 = request.POST["cur2"]
	money = request.POST["money"]
	rate = exchange_import_from_page(str(cur1), str(cur2))
	out = float(rate)*float(money)
	print(rate)
	content = {
            "cur1": cur1,
            "cur2": cur2,
            "rate": rate,
            "money": money,
            "out": out
        }
	return render(request, 'mysite/response.html',content)
	