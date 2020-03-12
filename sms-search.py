import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask,request, redirect
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

now = datetime.now()

ctime = now.strftime("%H:%M:%S")

app = Flask(__name__)

@app.route("/sms", methods=['GET','POST'])
def sms_reply():
    resp = MessagingResponse()
    body = request.form['Body'].lower()

    if body  == '/time':
        resp.message('Current time is {}'.format(ctime))
    if 'ping' in body:
        rund = os.system("ping -n 1 -w 1 {} > nul".format(body[5:]))
        if rund == 0:
           resp.message('{} is online!'.format(body[5:]))
        else:
            resp.message('{} is offline!'.format(body[5:]))
    if '/do' in body:
        os.system(body[4:])

    if 'search' in body:
        driver=webdriver.Chrome(executable_path=r'C:\\Users\\Techy\\Documents\\Python\\Big Projects\\Karim\\chromedriver.exe')
        driver.get('https://www.google.com')
        time.sleep(1)
        search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        time.sleep(1)
        search.send_keys(body[7:])
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        results = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]')
        results = (u'{}'.format(results.text))
        resp.message(results)

    return str(resp)


app.run(debug=True)
