#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:19:16 2020

@author: francisco
"""

import requests

sender_id='whatsapp:+573003445373'
url='http://davivienda.com/pagos'
headers = {'Content-Type': 'application/json',}

params = (('output_channel', 'twilio'),)

data = '{"name": "infoLink", "entities": {"banco": "url"}}'.replace('url','DAVIVIENDA')

response = requests.post('http://localhost:5005/conversations/sender_id/trigger_intent'.replace('sender_id',sender_id), headers=headers, params=params, data=data)