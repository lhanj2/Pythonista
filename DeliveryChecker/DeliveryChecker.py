import ui
import re
import clipboard
import urllib.request
import webbrowser
from urllib.parse import quote
import sys


def listToString(str_list):
	result =""
	for s in str_list:
		result += s + " "
		return result.strip()

def tableview_shipping_did_select(sender):
  value = sender.selected_row
  global name 
  name = sender.items[value]
  defaultUrl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query='  + quote(str(name)) +listToString(newList)
  webbrowser.open(defaultUrl)
  v.close()

v = ui.load_view()
v.name = 'Delivery Checker'
#clipboard.get_image()
clipboardData = clipboard.get()
numbersList = re.findall(r'\d+', clipboardData)

newList = [x for x in numbersList if len(x)>10]

if listToString(newList) is None:
  v.close()
  sys.exit()
else:
  v.present('sheet')
