from send import LogTransporter
from datetime import datetime as dt

class Event(object):
	def __init__(self,token,event_ep,user,timestamp):
		self.endpoint = LogTransporter(token,endpnt=event_ep)
		self.user_id = user
		self.ts = timestamp

	def to_dict(self):
		return {}

	def send(self):
		log_event = self.to_dict()
		self.endpoint.send(log_info)

class TextMessageEvent(Event):
	def __init__(self,token,user,message,timestamp,image_flag=False,incoming=True,funnel_step=None,campaign_name=None):
		'''
		Initialize Text message
		event object.
		'''
		Event.__init__(self,token,'/TextMessageEvent',user,timestamp)
		self.content = message
		self.is_image = image_flag
		self.is_incoming = incoming
		self.step = funnel_step
		self.campaign = campaign_name

	def to_dict(self):
		'''
		Convert to dictionary object.
		'''
		text_message_obj = {
			'user_id':self.user_id,
			'content':self.content,
			'timestamp':self.ts,
			'is_image':self.is_image,
			'is_incoming':self.is_incoming,
			'funnel_step':self.step,
			'campaign_name':self.campaign
		}
		return text_message_obj

	def __repr__(self):
		return json.dumps(self.to_dict())

class TemplateImpressionEvent(Event):
	def __init__(self,token,user,template_name,timestamp,template_type,bubble_url=None,funnel_step=None,campaign_name=None):
		assert(template_type.lower() in ['button','generic'])
		Event.__init__(self,token,'/TemplateImpressionEvent',user,timestamp)
		self.t_name = template_name
		self.t_type = template_type
		self.bubble_url_ = bubble_url
		self.step = funnel_step
		self.campaign = campaign_name

	def to_dict(self):
		'''
		Convert to dictionary object.
		'''
		template_impression_obj = {
			'user_id':self.user_id,
			'template_name':self.t_name,
			'template_type':self.t_type,
			'timestamp':self.ts,
			'bubble_url':self.bubble_url_,
			'funnel_step':self.step,
			'campaign_name':self.campaign
		}
		return template_impression_obj

	def __repr__(self):
		return json.dumps(self.to_dict())

class ButtonImpressionEvent(Event):
	def __init__(self,token,user,timestamp,template_name,button_name,button_type='postback',target_url=None,funnel_step=None,campaign_name=None):
		assert(button_type.lower() in ['web_url','postback'])
		assert(not target_url or target_url!=None and button_type=='web_url')
		Event.__init__(self,token,'/ButtonImpressionEvent',user,timestamp)
		self.t_name = template_name
		self.b_name = button_name
		self.b_type = button_type
		self.target = target_url
		self.step = funnel_step
		self.campaign = campaign_name

	def to_dict(self):
		'''
		Convert to dictionary object.
		'''
		button_impression_obj = {
			'user_id':self.user_id,
			'timestamp':self.ts,
			'template_name':self.t_name,
			'button_name':self.b_name,
			'button_type':self.b_type,
			'url_target':self.target,
			'funnel_step':self.step,
			'campaign_name':self.campaign
		}
		return button_impression_obj

	def __repr__(self):
		return json.dumps(self.to_dict())

class TransactionEvent(Event):
	def __init__(self,user,timestamp,order_number,currency_type,payment_method,total_cost,subtotal,shipping_cost,total_tax,adjusted_flag,adjustment_amount=None,funnel_step=None,campaign_name=None):
		Event.__init__(self,token,'/TransactionEvent',user,timestamp)
		self.order = order_number
		self.currency = currency_type
		self.method = payment_method
		self.total = total_cost
		self.subtotal_ = subtotal
		self.shipping = shipping_cost
		self.tax = total_tax
		self.is_adjusted = adjusted_flag
		self.adjustment = adjustment_amount
		self.step = funnel_step
		self.campaign = campaign_name

	def to_dict(self):
		'''
		Convert to dictionary object.
		'''
		receipt_object = {
			'user_id':self.user_id,
			'timestamp':self.ts,
			'order_number':self.order,
			'currency_type':self.currency,
			'payment_method':self.method,
			'total_cost':self.total,
			'subtotal':self.subtotal_,
			'shipping_cost':self.shipping,
			'total_tax':self.tax,
			'is_adjusted':self.is_adjusted,
			'adjustment_amount':self.adjustment,
			'funnel_step':self.step,
			'campaign_name':self.campaign
		}
		return receipt_object

	def __repr__(self):
		return json.dumps(self.to_dict())

class ClickEvent(Event):
	def __init__(self,user_id,timestamp,template_name,button_click_flag=False,button_name=None):
		Event.__init__(self,token,'/ClickEvent',user,timestamp)
		self.t_name = template_name
		self.is_button_click=button_click_flag
		self.b_name = button_name

	def to_dict(self):
		'''
		Convert to dictionary object.
		'''
		click_obj = {
			'user_id':self.user,
			'timestamp':self.ts,
			'template_name':self.t_name,
			'is_button_click':self.is_button_click,
			'button_name':self.b_name
		}
		return click_obj

	def __repr__(self):
		return json.dumps(self.to_dict())