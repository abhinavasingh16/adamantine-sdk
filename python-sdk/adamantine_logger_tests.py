from adamantine_logger import ClickEvent,TextMessageEvent,TemplateImpressionEvent
from adamantine_logger import ButtonImpressionEvent,TransactionEvent
from datetime import datetime as dt
from test_utils import indicator
import sys


"""
Loose Invariants:

    (1) All logged events must generate the correct dictionary.
    (2) ClickEvents must map to an existing Template Name or Button Name.
    (3) All logs sent to the api must get a 202 or a 500 status message back. [Check w/API]
    (3) ButtonImpressionEvent must map to an existing Template Name. [Check w/API]
    (4) Optional Fields must also be included in the correct dictionary. [Check w/API]
"""

test_token = '12345'

def test1(verbose):
    '''
    Checks to see if TextMessageEvent
    logging produces the correct dictionary
    given just mandatory fields.
    '''
    now = dt.now()
    text_event = TextMessageEvent('12345',21211,'hello',now)
    d1 = text_event.to_dict()
    d2 = {
            'user_id':21211,
            'content':'hello',
            'timestamp':now,
            'is_image':False,
            'is_incoming':True,
            'funnel_step':None,
            'campaign_name':None
        }
    if verbose:
        print "D1 is: {}".format(d1)
        print "D2 is: {}".format(d2)
    print "Test 1 Result: {}".format(d1==d2)
    return indicator(d1==d2)

def test2(verbose):
    '''
    Checks to see if TextMessageEvent
    produces the correct dictionary
    given optional fields.
    '''
    now = dt.now()
    text_event = TextMessageEvent('12345',21211,'/url/',now,image_flag=True,incoming=False,funnel_step=1,campaign_name='Hello Campaign')
    d1 = text_event.to_dict()
    d2 = {
        'user_id':21211,
        'content':'/url/',
        'timestamp':now,
        'is_image':True,
        'is_incoming':False,
        'funnel_step':1,
        'campaign_name':'Hello Campaign'
    }
    if verbose:
        print "D1 is: {}".format(d1)
        print "D2 is: {}".format(d2)
    print "Test 2 Result: {}".format(d1==d2)
    return indicator(d1==d2)

def test3(verbose):
    '''
    Checks to see if TemplateImpressionEvent
    logging produces the correct dictionary
    given just mandatory fields.
    '''
    now = dt.now()
    template_impression_event = TemplateImpressionEvent('12345',21211,'New Template',now,'button')
    d1 = template_impression_event.to_dict()
    d2 = {
        'user_id':21211,
        'template_name':'New Template',
        'template_type':'button',
        'timestamp':now,
        'bubble_url':None,
        'funnel_step':None,
        'campaign_name':None
    }
    if verbose:
        print "D1 is: {}".format(d1)
        print "D2 is: {}".format(d2)
    print "Test 3 Result: {}".format(d1==d2)
    return indicator(d1==d2)

def test4(verbose):
    '''
    Checks to see if TemplateImpressionEvent
    produces the correct dictionary
    given optional fields.
    '''
    now = dt.now()
    template_impression_event = TemplateImpressionEvent('12345',21211,'New Template',now,'button','/hello/',1,'Hello Campaign')
    d1 = template_impression_event.to_dict()
    d2 = {
        'user_id':21211,
        'template_name':'New Template',
        'template_type':'button',
        'timestamp':now,
        'bubble_url':'/hello/',
        'funnel_step':1,
        'campaign_name':'Hello Campaign'
    }
    if verbose:
        print "D1 is: {}".format(d1)
        print "D2 is: {}".format(d2)
    print "Test 4 Result: {}".format(d1==d2)
    return indicator(d1==d2)

def test5(verbose):
    '''
    Checks to see if ButtonImpressionEvent
    logging produces the correct dictionary
    given just mandatory fields.
    '''
    now = dt.now()
    button_impression_event = ButtonImpressionEvent('12345',21211,now,'New Template','Click Button')
    d1 = button_impression_event.to_dict()
    d2 = {
        'user_id':21211,
        'timestamp':now,
        'template_name':'New Template',
        'button_name':'Click Button',
        'button_type':'postback',
        'url_target':None,
        'funnel_step':None,
        'campaign_name':None
    }
    if verbose:
        print "D1 is: {}".format(d1)
        print "D2 is: {}".format(d2)
    print "Test 5 Result: {}".format(d1==d2)
    return indicator(d1==d2)

def test6(verbose):
    '''
    Checks to see if ButtonImpressionEvent
    produces the correct dictionary
    given optional fields.
    '''
    now = dt.now()
    button_impression_event = ButtonImpressionEvent('12345',21211,now,'New Template','Click Button',button_type='web_url',target_url='/hello/',funnel_step=1,campaign_name='Hello Campaign')
    d1 = button_impression_event.to_dict()
    d2 = {
        'user_id':21211,
        'timestamp':now,
        'template_name':'New Template',
        'button_name':'Click Button',
        'button_type':'web_url',
        'url_target':'/hello/',
        'funnel_step':1,
        'campaign_name':'Hello Campaign'
    }
    if verbose:
        print "D1 is: {}".format(d1)
        print "D2 is: {}".format(d2)
    print "Test 6 Result: {}".format(d1==d2)
    return indicator(d1==d2)

def execute_unit_tests(verbose):
    unit_tests = [
        test1(verbose),
        test2(verbose),
        test3(verbose),
        test4(verbose),
        test5(verbose),
        test6(verbose)
    ]
    result = sum(unit_tests)/len(unit_tests)
    print "Test Summary: {0}/{1} tests passed".format(sum(unit_tests),len(unit_tests))
    print "Code Score: {}%".format(result*100)

if __name__=="__main__":
    verbose = False
    if len(sys.argv) >= 2 and sys.argv[1]=='-v':
        verbose=True
    execute_unit_tests(verbose)
