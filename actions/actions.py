# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from actions.factuSQL import *

import asyncio
import aiohttp

def generarTipoFactura(empresa):
    switcher={
            'acueducto de bogota':'agua',
            'aguas de manizales':'agua',
            'chec':'electricidad',
            'efigas':'gas',
            'codensa':'electricidad',
            'vanti':'gas',
             }
    return switcher.get(empresa,"")
class validarRegistroUsuario(Action):

    def name(self) -> Text:
        return "validarRegistro"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#        numeroWpp="+573003445373"
        if tracker.current_state().get('latest_input_channel')=='twilio':
            numeroWpp=tracker.current_state()['sender_id'].split(':')[1] 
        else: numeroWpp="+573003445373"
        
        datosUsuario=validarUsuario(numeroWpp)
        if datosUsuario==False:
            #tracker.slots['usuarioRegistrado']="no"
            print('el usuario no esta registrado')
            return [SlotSet('usuarioRegistrado', 'no')]
        else:
            id= datosUsuario[0]
            nombre= datosUsuario[1]
            correo=datosUsuario[2]
            banco=datosUsuario[3]
            print('el usuario si esta registrado con '+'correo: '+correo+ ' y '+' banco: '+banco) #correo: '+tracker.get_slot('correoPSE')+' banco: '+tracker.get_slot('banco'))
            #dispatcher.utter_message(text='el slot usuarioRegistrado es '+ str(tracker.get_slot('usuarioRegistrado')))
            return [SlotSet('usuarioRegistrado', 'si'),SlotSet('correoPSE', correo),SlotSet('banco', banco),SlotSet('id', id),SlotSet('nombre', nombre),SlotSet('numeroWpp', numeroWpp)]
class BuscarFactura(Action):

    def name(self) -> Text:
        return "buscarFactura"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        id=tracker.get_slot('id')
        tipoFactura=tracker.get_slot('tipoFactura')
        numeroFactura=tracker.get_slot('numeroFactura')
        empresa=tracker.get_slot('empresa')
        datosFactura=validarFactura(str(id),numeroFactura,empresa,tipoFactura)

        if datosFactura==False:
            print('la factura no esta registrada')
            return[SlotSet('facturaRegistrada', 'no')]
        else:
            print('la factura si esta registrada')
            tipoFactura=datosFactura[2]
            empresa=datosFactura[1]
            numeroFactura=datosFactura[0]
            print('la factura si esta registrada: '+'Factura de '+tipoFactura+' con numero '+numeroFactura+'de la empresa '+empresa)
            return[SlotSet('facturaRegistrada', 'si'),SlotSet('tipoFactura', tipoFactura),SlotSet('empresa', empresa),SlotSet('numeroFactura', numeroFactura)]

# def get_link(numeroFactura,empresa,banco,correoPSE,sender_id):

#     response = requests.get(
#         'http://localhost:5000/',
#         params={'numeroFactura': numeroFactura, 'empresa':empresa,'banco':banco,'correoPSE':correoPSE,'sender_id':sender_id},
#         )
#     return(response)


class GenerarLink(Action):

    def name(self) -> Text:
        return "generarLinkRPA"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        empresa=tracker.get_slot('empresa')
        banco=tracker.get_slot('banco')
        correoPSE=tracker.get_slot('correoPSE')
        numeroFactura=tracker.get_slot('numeroFactura')
        sender_id=tracker.current_state()['sender_id']
        #get_link(numeroFactura,empresa,banco,correoPSE,sender_id)
        params={'numeroFactura': numeroFactura, 'empresa':empresa,'banco':banco,'correoPSE':correoPSE,'sender_id':sender_id}
        async with aiohttp.ClientSession() as session:
            async with session.get('http://localhost:5000/',params=params) as resp:
                print(resp.status)
                link=await resp.text()
        print(link)
        if len(link)>2:
            error=False
        else: error =True    
        if error==False:
            print('no hay error')
            dispatcher.utter_message(text='Puedes pagar tu factura en este link de '+tracker.get_slot('banco')+': '+link)
            return[SlotSet('errorRPA', 'no')]
        else:
            print('hubo un error')
            dispatcher.utter_message(text='Parece ser que hubo un error')
            return[SlotSet('errorRPA', 'si')]

class guardarFactura(Action):

    def name(self) -> Text:
        return "guardarFactura"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            id=tracker.get_slot('id')
            empresa=tracker.get_slot('empresa')
            tipoFactura=generarTipoFactura(empresa)
            numeroFactura=tracker.get_slot('numeroFactura')
            registrado=registrarFacturaDB(str(id),numeroFactura,empresa,tipoFactura)
            if registrado:
                dispatcher.utter_message(text='La factura se ha guardado exitosamente')
            else:
                dispatcher.utter_message(text='La factura no se ha podido guardar')
            return []    
                
                
class GuardarFeedback(Action):

    def name(self) -> Text:
        return "guardarFeedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            id_usuario=tracker.get_slot('id')
            nombre_usuario=tracker.get_slot('nombre')
            correo_pse=tracker.get_slot('correoPSE')
            numero_wpp=tracker.get_slot('numeroWpp')
            feed_back=tracker.latest_message['text']
            guardarFB(id_usuario,nombre_usuario,correo_pse,numero_wpp,feed_back)
            return []


class DarLink(Action):

    def name(self) -> Text:
        return "darLink"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link=tracker.get_slot('banco')#cambiar por link
        if True:
            dispatcher.utter_message(text='Puedes pagar tu factura en: '+link)
        else:
            dispatcher.utter_message(text='no se pudo generar link')

        return[]
