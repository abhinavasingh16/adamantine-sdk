import requests
import json
import datetime

class Endpoint:
	def __init__(self,token,hst='http://127.0.0.1',prt=5000,endpnt='/'):
		self.host = host
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

class AdamentineTextEvent:
	def __init__(self,token,user,message,seq,is_response=True,timestamp=datetime.now):
		self.endpoint = Endpoint(token,endpnt='/TextEvent')
		self.user_id = user
		self.event_timestamp = timestamp
		self.message_content = message
		self.seq_nr = seq
		self.response_flag = is_response

	def to_dict(self):
		'''
		Get dictionary representation of
		text event.
		'''
		adamentine_text_event = {
			'user_id':self.user_id,
			'event_timestamp':self.event_timestamp,
			'message_content':self.message_content,
			'seq_nr':self.seq_nr,
			'response_flag':self.response_flag
		}
		return adamentine_text_event

	def __repr__(self):
		return json.dumps(self.to_dict())

	def send(self):
		'''
		Use requests to send log event 
		to public API.
		'''
		log_info = self.to_dict()
		self.endpoint.send(log_info)

class AdamentineImpressionEvent:
	def __init__(self,token,user,timestamp,impression_information,is_carrousel=False,seq_nr=None,funnel_step=None,campaign_name=None):
		self.endpoint = Endpoint(token,endpnt='/ImpressionEvent')
		self.user_id = user
		self.event_timestamp = timestamp
		self.impression_information = impression_information
		self.is_carrousel = is_carrousel
		self.seq_nr = seq_nr
		self.funnel_step = funnel_step
		self.campaign_name = campaign_name

	def to_dict(self):
		'''
		Get dictionary representation of object.
		'''
		adamentine_impression_event = {
			'user_id':self.user_id,
			'event_timestamp':self.event_timestamp,
			'impression_information':self.impression_information,
			'is_carrousel':self.is_carrousel,
			'seq_nr':self.carrousel_position,
			'funnel_step':self.funnel_step,
			'campaign_name':self.campaign_name
		}
		return adamentine_impression_event

	def send(self):
		log_info = self.to_dict()
		self.endpoint.send(log_info)

class AdamentineClickEvent:
	def __init__(self,token,user,timestamp,target_url):
		self.endpoint = Endpoint(token,endpnt='/ImpressionEvent')
		self.user_id = user
		self.event_timestamp = timestamp
		self.url = target_url



