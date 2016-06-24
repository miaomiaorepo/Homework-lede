
# coding: utf-8

# In[105]:

import requests


# In[73]:

response = requests.get('https://api.forecast.io/forecast/1a4991f3feb9de329fc1407de3265f13/40.8006,-73.9653')


# In[87]:

data = response.json()


# In[242]:

today = data['daily']['data']
def temp_feeling(x):
    for i in today:
        if i['temperatureMax'] >= 77:
            return "hot"
        elif i['temperatureMax'] >= 60 and tody['temperatureMax'] < 76:
            return 'warm'
        elif i['temperatureMax'] < 60:
            return 'cold'


# In[243]:

def rain_warning(x):
    for i in today:
        if i['precipIntensity'] > 0.017:
            return("bring your umbrella!")  
        else:
            return("Have a good day!")


# In[244]:

today_high = str(today[0]['temperatureMax'])
today_low = str(today[0]['temperatureMin'])
current_temp = str(data['currently']['temperature'])
current_sum = str(data['currently']['summary'])


# In[245]:

# Right now it is TEMPERATURE degrees out and SUMMARY. 
# Today will be TEMP_FEELING with a high of HIGH_TEMP and 
# a low of LOW_TEMP. RAIN_WARNING.


# In[249]:

text =  "Right now it is "+current_temp+" degrees out and "+current_sum+". Today will be "+temp_feeling(x)+"with a high of "+today_high+" and a low of "+today_low+". "+rain_warning(x)
print(text)


# In[250]:

import dateutil.parser
import time,datetime
now = time.strftime("%B %d, %Y")


# In[248]:

key = 'key-b6f07c1a84b9c8d231ddb0f4fe00d648'
sandbox = 'sandbox41d433508cd3471480f96efde8aaa441.mailgun.org'
recipient = 'shuyao1201@gmail.com'
request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key), data={
    'from': 'hello@example.com',
    'to': recipient,
    'subject': "8am Weather forecast:" + now,
    'text': text,
})

print('Status: {0}'.format(request.status_code))
print('Body:   {0}'.format(request.text))


# In[ ]:



