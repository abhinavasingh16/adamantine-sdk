import requests

class LogTransporter:
	def __init__(self,token,hst='http://127.0.0.1',prt=5000,endpnt='/'):
		self.host = hst
		self.port = prt
		self.endpoint = endpnt
		self.tkn = token

	def get_endpoint(self):
		return "{0}:{1}/{2}/{3}".format(self.host,self.port,self.endpoint,self.tkn)

	def send(self,log_info):
		url = self.get_endpoint()
		status = requests.post(url,data=log_info)
		if int(status) != 202:
			raise Exception("Error: API returned a {0} status.".format(status))

	def __repr__(self):
		return self.get_endpoint()