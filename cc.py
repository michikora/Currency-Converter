import requests
from wox import Wox,WoxAPI
import clipboard
from os.path import dirname, join
import pycountry

a=""

class Main(Wox):
	icon = join(dirname(__file__), 'Images', 'plugin.png')
	def query(self,query):
		results=[]
		args = query.split(' ')
		if len(args)==3 and len(args[1])==3 and len(args[2])==3:
			url = ('https://currency-api.appspot.com/api/%s/%s.json') % (args[1], args[2])
			r = requests.get(url)
			a = r.json()['rate']
			try:
				a=float(a)
				b=float(args[0])*a
				c=args[2]

				pass
			except Exception, e:
				b="Invalid amount"
				c="" 
				pass
			finally:
				pass

			results=[]
			if b>0 and b!="Invalid amount":
				c=c.upper()
				c=pycountry.currencies.get(letter=c)
				x=str(c.name)
				b="{0:.2f}".format(b)
				b=str(b)
				results.append({
   					"Title": b+" "+x+"s",
    				"SubTitle":"Copy to clipboard",
    				"IcoPath":"Images/plugin.png",
    				"JsonRPCAction":{'method': 'copy', 'parameters': [b],'dontHideAfterAction': False}
				})
				return results
				
			if args[0] == "0":
				str(b)
				results.append({
   				"Title": "Please enter an ammount other than 0",
    			"SubTitle":"We can't convert nothing...",
    			"IcoPath":"Images/plugin.png"
				})
				return results
			if b<=0:
				str(b)
				results.append({
   				"Title": "Please enter valid currency codes",
    			"SubTitle":"One of those currencies doesn't exist",
    			"IcoPath":"Images/plugin.png"
				})
				return results
			if b=="Invalid amount":
				results.append({
   				"Title": "Invalid amount",
    			"SubTitle":"Enter a number",
    			"IcoPath":"Images/plugin.png"
				})
				return results
		else:
			results=[]
			results.append({
       			"Title":"Currency Converter",
        		"SubTitle":"How may I take your order?",
        		"IcoPath":"Images/plugin.png"
        	})
    		return results		
   
	def copy(self, data):
		clipboard.put(data)
		WoxAPI.show_msg("Value has been copied to clipboard.", '', self.icon)

if __name__ == "__main__":
	Main()