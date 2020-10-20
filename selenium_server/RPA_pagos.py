#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:53:02 2020

@author: franciscoreales
"""

#from visionAPI import infoFacturaVision

from selenium import webdriver
#from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from flask import Flask
import flask
import requests
# # file='vanti.jpg'
# #numeroFactura,monto,empresa=infoFacturaVision(file)
# #numeroFactura,monto,empresa,entidadFinanciera = '1353470-9','','codensa','BANCO DAVIVIENDA'
# numeroFactura,monto,empresa,entidadFinanciera = '446583','','efigas','BANCO DAVIVIENDA'
# # #print('el numero de la factura es: '+str(numeroFactura)+' por un monto de: '+str(monto))
# correoPSE='freales@javeriana.edu.co'
# banco='BANCO DAVIVIENDA'#'BANCOLOMBIA'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def generar_link():
    numeroFactura = flask.request.args.get('numeroFactura', '')
    empresa = flask.request.args.get('empresa', '')
    banco = flask.request.args.get('banco', '')
    correoPSE=flask.request.args.get('correoPSE', '')
    sender_id=flask.request.args.get('sender_id', '')
    try:
        # corre en el background
        # options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        #CHROMEDRIVER_PATH = './actions/chromedriver'
        CHROMEDRIVER_PATH='./chromedriver'
        #
        # browser = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
        browser = webdriver.Chrome(CHROMEDRIVER_PATH)
        url=''
        if empresa=='chec':
            browser.get('https://www.zonapagos.com/t_hidrocaldasbd/pagos.asp')
            elementID = browser.find_element_by_id('ContentPlaceHolder1_IdCliente')
            elementID.send_keys(numeroFactura)
    
    
            elementID.send_keys(Keys.RETURN)
    
            time.sleep(1)
            browser.find_element_by_xpath("//input[@name='ctl00$ContentPlaceHolder1$gvFacturas$ctl02$chk']").click()
            browser.find_element_by_xpath("//input[@name='ctl00$ContentPlaceHolder1$btnPagar']").click()
    
    
            time.sleep(1)
            #soup = BeautifulSoup(browser.page_source, 'html.parser')
            browser.find_element_by_xpath("//select[@name='lst_bancos_pse']/option[text()='banco']".replace('banco',banco)).click()
            browser.find_element_by_id('botonpago0').click()
            time.sleep(1)
            browser.find_element_by_id('PNEMail').send_keys(correoPSE)
            time.sleep(2)
            banco=browser.find_element_by_id('btnSeguir')
            browser.execute_script("arguments[0].click();", banco)
            time.sleep(1)
            print('Finaliza el pago con el siguiente link: '+browser.current_url)
            url=browser.current_url
            browser.close()
    
        if empresa=='vanti':
            start=time.time()
            browser.get('https://pagospse.grupovanti.com:7201')
            time.sleep(0.5)
            browser.execute_script("arguments[0].click();",browser.find_element_by_xpath('//img[@src="../../assets/img/home/domestico.png"]'))
            browser.find_element_by_xpath("//select[@id='inputCompany']/option[text()='Vanti S.A. ESP']").click()
            browser.find_element_by_id('inputReferencia').send_keys(numeroFactura)
            browser.find_element_by_xpath("//button[@class='btn btn-block btn-outline-primary']").click()
            time.sleep(0.5)
            browser.execute_script("arguments[0].click();",browser.find_element_by_xpath("//button[@class='btn btn-block btn-primary']"))
            time.sleep(1)
            # # select_box = browser.find_element_by_id("pseCodigoBanco")
            # # options = [x for x in select_box.find_elements_by_tag_name("option")]
            # # for element in options:
            # #     print (element.get_attribute("text"))
            browser.find_element_by_id('correo').send_keys(correoPSE)
            browser.find_element_by_xpath("//select[@id='pseCodigoBanco']/option[text()='banco']".replace('banco',banco)).click()
            browser.find_element_by_xpath("//a[@id='pagar']").click()
            time.sleep(1)
            #time.sleep(10.5)
            
            browser.find_element_by_id('PNEMail').send_keys(correoPSE)
            
            time.sleep(0.5)
            
            banco=browser.find_element_by_id('btnSeguir')
            
            browser.execute_script("arguments[0].click();", banco)
            time.sleep(3)
            # alert_obj = browser.switch_to.alert
            # alert_obj.accept() 
            # banco=browser.find_element_by_id('btnSeguir')
            # browser.execute_script("arguments[0].click();", banco)
            #     time.sleep(1.5)
            #     print('Finaliza el pago con el siguiente link: '+browser.current_url)
            url=browser.current_url
            print(url)
            end=time.time()
            print('tiempo en el proceso: '+str(end-start)+' segundos')
            #browser.execute_script("document.getElementById('PNEMail').value='correoPSE'".replace('correoPSE',correoPSE))
            
            
            
            browser.close()
            return(url)
    
        if empresa=='aguasDeManizales':
            browser.get('https://www.aguasdemanizales.com.co/Clientes-Proveedores/Portal-Clientes-pago')
            time.sleep(1)
            print(browser.execute_script('document.getElementById("txtSuscriptor");'))
            # a.send_keys('SI')
            #browser.find_element_by_xpath('')#.send_keys('SI')
            # browser.find_element_by_xpath("//select[@id='seleccionFactura']/option[text()='Servicio de Acueducto, Alcantarillado y Aseo']").click()
            # elementID = browser.find_element_by_name('ID_AUTDATOS')
            # elementID.send_keys('SI')
            browser.close()
    
        if empresa=='efigas':
            browser.get('https://www.e-collect.com/customers/Plus/EfigasReferenciadoPagosPlus.htm')
            time.sleep(1)
            browser.find_element_by_name("ctl00$PagePlaceHolder$txtUsername$ctl00").send_keys(numeroFactura)
            browser.find_element_by_id('PagePlaceHolder_btnSignIn').click()
            
            browser.execute_script("arguments[0].click();", WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="gvPayments"]/tbody/tr/td[1]/span[1]/div/ins'))))
            
            browser.execute_script("arguments[0].click();", WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID,
                                                'PagePlaceHolder_btnPay'))))
            
            time.sleep(2)
                                               
            browser.find_element_by_id('PagePlaceHolder_txtForm.0.4.19').send_keys(correoPSE)
            browser.find_element_by_xpath('//*[@id="PagePlaceHolder_ddlForm.0.0.1"]/option[text()="banco"]'.replace('banco',banco)).click()
            browser.find_element_by_xpath('//*[@id="PagePlaceHolder_ddlForm.0.1.2"]/option[text()="Persona Natural"]').click()
            browser.find_element_by_xpath('//*[@id="PagePlaceHolder_ddlForm.0.2.3"]/option[text()="Cédula de Ciudadanía"]').click()
            browser.find_element_by_id('PagePlaceHolder_txtForm.0.3.4').clear()
            browser.find_element_by_id('PagePlaceHolder_txtForm.0.3.4').send_keys('100000000')
            browser.find_element_by_id('PagePlaceHolder_btnPay').click()
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="PNEMail"]')))
            browser.find_element_by_xpath('//*[@id="PNEMail"]').send_keys(correoPSE)
            time.sleep(1)
            banco=browser.find_element_by_id('btnSeguir2')
            
            
            browser.execute_script("arguments[0].click();", banco)
            time.sleep(2)
            print('Finaliza el pago con el siguiente link: '+browser.current_url)
            url=browser.current_url
            browser.close()
    
        if empresa == 'codensa':
            digitoDeVerificacion=numeroFactura.split('-')[1]
            numeroFactura=numeroFactura.split('-')[0]
            start = time.time()
            browser = webdriver.Chrome('driver/chromedriver')
            browser.get('https://www.enel.com.co/es/personas/servicio-al-cliente/boton-de-pago.html')
            time.sleep(0.5)
            browser.execute_script("arguments[0].setAttribute('value', '" + digitoDeVerificacion + "')",
                                   browser.find_element_by_xpath(
                                       '/html/body/main/div/div/section[1]/form/div/fieldset/div[3]/input'))
            browser.execute_script("arguments[0].setAttribute('value', '" + numeroFactura + "')",
                                   browser.find_element_by_id('client'))
            # browser.execute_script("arguments[0].setAttribute('value', '" +digitoDeVerificacion+"')",browser.find_element_by_xpath('/html/body/main/div/div/section[1]/form/div/fieldset/div[3]/input'))
            # browser.execute_script("arguments[0].setAttribute('value', '" +numeroFactura+"')",browser.find_element_by_id('client'))
            # # browser.execute_script("arguments[0].setAttribute('value', '" +digitoDeVerificacion+"')",browser.find_element_by_id('dv'))
            # browser.find_element_by_id('client').send_keys(numeroFactura)
            time.sleep(0.5)
            browser.execute_script("arguments[0].click();", browser.find_element_by_id('solicitar'))
            myElem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="1"]')))
    
            browser.execute_script("arguments[0].click();", myElem)
    
            browser.execute_script("arguments[0].click();", browser.find_element_by_xpath('//*[@id="btn-pago-table"]'))
            imgPSE = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="form_contact-step-3"]/div[2]/div/div/div/div[2]/div[1]/img')))
            browser.execute_script("arguments[0].click();", imgPSE)
            browser.execute_script("arguments[0].click();", browser.find_element_by_xpath('//*[@id="btn-pago"]'))
            imgPSE2 = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root-app"]/div[1]/div/div[1]/div[1]/form/ul[2]/li/label/div/div[1]/div/img')))
            browser.execute_script("arguments[0].click();", imgPSE2)
            #    browser.execute_script("arguments[0].click();",WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[1]/div/div[1]/div/form/div/div[1]/fieldset/div[1]/label/div[1]/input'))))
            browser.execute_script("arguments[0].click();", WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/main/div[1]/div/div[1]/div/form/div/div[1]/div/button'))))
            browser.execute_script("arguments[0].click();", WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/div[1]/main/div[1]/div/div[1]/div/form/div/div[1]/div/div[2]/ul/li[3]/div/div/div'))))
            browser.execute_script("arguments[0].click();", WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/div[1]/main/div[1]/div/div[1]/div/form/div/div[2]/div/div[2]/ul/li[4]/div/div/div'))))
            browser.execute_script("arguments[0].click();", WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/main/div[1]/div/div[2]/div[2]/div/button'))))
            browser.find_element_by_id('identification_number').send_keys("12345670")
            browser.find_element_by_id('email').send_keys(correoPSE)
            browser.execute_script("arguments[0].click();", WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/main/div[1]/div/div[2]/div[2]/div/button/span'))))
    
            browser.execute_script("arguments[0].click();", WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/main/div[1]/div/div/div/div/div/div/div[2]/a'))))
    
            browser.switch_to.window(browser.window_handles[1])
            time.sleep(1)
            browser.find_element_by_id('PNEMail').send_keys(correoPSE)
            time.sleep(1)
            banco = browser.find_element_by_id('btnSeguir2')
            browser.execute_script("arguments[0].click();", banco)
            time.sleep(1)
            print('Finaliza el pago con el siguiente link: ' + browser.current_url)
            end = time.time()
            print('tiempo del proceso: ' + str(end - start) + ' segundos')
            url=browser.current_url
            browser.close()
        return(url)
    
        # headers = {'Content-type': 'application/json',}
        # data = '{"sender":"sender_id", "message":"msj"}'.replace('msj',url).replace('sender_id',sender_id)
        
        # response = requests.post('https://04729ef77836.ngrok.io/webhooks/twilio/webhook', headers=headers, data=data)
        # print('status code: '+str(response.status_code))
        # if response.status_code != 200:
        #     data = '{"sender":"sender_id", "message":"msj"}'.replace('msj','el link no se pudo generar').replace('sender_id',sender_id)
        #     response = requests.post('https://localhost:5005/webhooks/twilio/webhook', headers=headers, data=data)
    except:
            print('no funciono')
            #browser.set_window_size(1920, 4000)
            #browser.save_screenshot("./screenshot.png")
            browser.close()
            return(url)
            # headers = {'Content-type': 'application/json',}
            # data = '{"sender":"sender_id", "message":"msj"}'.replace('msj','el link no se pudo generar').replace('sender_id',sender_id)
            # response = requests.post('https://04729ef77836.ngrok.io/webhooks/twilio/webhook', headers=headers, data=data)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)