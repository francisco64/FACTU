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
from selenium.webdriver.chrome.options import Options
# file='vanti.jpg'
#numeroFactura,monto,empresa=infoFacturaVision(file)
# numeroFactura,monto,empresa,banco = '942298','','vanti','BANCO DAVIVIENDA'
# #print('el numero de la factura es: '+str(numeroFactura)+' por un monto de: '+str(monto))
# correoPSE='freales@javeriana.edu.co'
# banco='BANCO DAVIVIENDA'#'BANCOLOMBIA'

#corre en el background
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
CHROMEDRIVER_PATH='./actions/chromedriver'
#CHROMEDRIVER_PATH='./chromedriver'
#
browser = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
#browser = webdriver.Chrome(CHROMEDRIVER_PATH)

def generar_link(numeroFactura,empresa,banco,correoPSE):
    try:
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
            time.sleep(0.5)
            #time.sleep(10.5)
            
            browser.find_element_by_id('PNEMail').send_keys(correoPSE)
            
            time.sleep(0.5)
            
            banco=browser.find_element_by_id('btnSeguir')
            
            browser.execute_script("arguments[0].click();", banco)
            time.sleep(2)
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
            
            
            
            #browser.close()
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
            time.sleep(5)
            browser.find_element_by_xpath('//*[@id="gvPayments"]/tbody/tr/td[1]/span[1]/div/ins').click()
            browser.find_element_by_id('PagePlaceHolder_btnPay').click()
            time.sleep(5)
            browser.find_element_by_xpath('//*[@id="PagePlaceHolder_ddlForm.0.0.1"]/option[text()="banco"]'.replace('banco',banco)).click()
            browser.find_element_by_xpath('//*[@id="PagePlaceHolder_ddlForm.0.1.2"]/option[text()="Persona Natural"]').click()
            browser.find_element_by_xpath('//*[@id="PagePlaceHolder_ddlForm.0.2.3"]/option[text()="Cédula de Ciudadanía"]').click()
            browser.find_element_by_id('PagePlaceHolder_txtForm.0.4.19').send_keys(correoPSE)
            browser.find_element_by_id('PagePlaceHolder_txtForm.0.3.4').clear()
            browser.find_element_by_id('PagePlaceHolder_txtForm.0.3.4').send_keys('100000000')
            browser.find_element_by_id('PagePlaceHolder_btnPay').click()
            time.sleep(2)
            browser.find_element_by_xpath('//*[@id="PNEMail"]').send_keys(correoPSE)
            try:
                banco=browser.find_element_by_id('btnSeguir2')
            except:
                time.sleep(10.5)
                banco=browser.find_element_by_id('btnSeguir2')
    
    
            browser.execute_script("arguments[0].click();", banco)
            time.sleep(2)
            print('Finaliza el pago con el siguiente link: '+browser.current_url)
            url=browser.current_url
            browser.close()

        return(url)
    except:
        print('no funciono')
        time.sleep(1)
        #browser.set_window_size(1920, 4000)
        #browser.save_screenshot("./screenshot.png")
        #browser.close()
        return(url)

# url=generar_link(numeroFactura,empresa,banco,correoPSE)
# print(url)