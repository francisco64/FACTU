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
#from factuSQL import validarUsuario, validarFactura, registrarFacturaDB
import pymysql as sql

def validarUsuario(numeroWpp):

    consulta='''select id, nombre, correoPSE, banco from userData where numeroWpp = "xyzpq";'''.replace('xyzpq',numeroWpp)
    cursor.execute(consulta)
    infoUsuario=cursor.fetchall()
    if len(infoUsuario)==0:
        infoUsuario=False
    else:
        infoUsuario=[infoUsuario[0][0],infoUsuario[0][1].split(' ')[0],infoUsuario[0][2],infoUsuario[0][3]]
    return infoUsuario

def validarFactura(id_usuario,numeroFactura,empresa,tipoFactura):
    if tipoFactura is None and empresa is None and numeroFactura is None:
        datosFactura=False
        return datosFactura
    if tipoFactura is not None:
        consulta='''select numeroFactura,empresa,tipoFactura FROM userData
        INNER JOIN facturas
        ON usuarios.userData.id  = usuarios.facturas.id
        where usuarios.userData.id = xyzpk and tipoFactura="xyzlp"
        ;'''.replace('xyzpk',id_usuario).replace('xyzlp',tipoFactura)
    elif empresa is not None:
        consulta='''select numeroFactura,empresa,tipoFactura FROM userData
        INNER JOIN facturas
        ON usuarios.userData.id  = usuarios.facturas.id
        where usuarios.userData.id = xyzpk and empresa="xyzlp"
        ;'''.replace('xyzpk',id_usuario).replace('xyzlp',empresa)
    elif numeroFactura is not None:
        consulta='''select numeroFactura,empresa,tipoFactura FROM userData
        INNER JOIN facturas
        ON usuarios.userData.id  = usuarios.facturas.id
        where usuarios.userData.id = xyzpk and numeroFactura="xyzlp"
        ;'''.replace('xyzpk',id_usuario).replace('xyzlp',numeroFactura)

    cursor.execute(consulta)
    datosFactura=cursor.fetchall()
    if len(datosFactura)==0:
        datosFactura=False
    else:
        datosFactura=[datosFactura[0][0],datosFactura[0][1],datosFactura[0][2]]
    return datosFactura
def registrarFacturaDB(id_usuario,numeroFactura,empresa,tipoFactura):
    if id_usuario is None or numeroFactura is None or empresa is None or tipoFactura is None:
        return False
    else:
        consulta='''
        insert into facturas(id, numeroFactura, empresa, tipoFactura) values (id_usuario,"xyzpq", "xyzok","xyzso")
        ;'''.replace("id_usuario",id_usuario).replace("xyzpq",numeroFactura).replace("xyzok",empresa).replace("xyzso",tipoFactura)
        cursor.execute(consulta)
        db.commit()
        return True

db=sql.connect('factu-db.c15hdm9dgrjl.us-east-2.rds.amazonaws.com','admin','Hostinguer.123')

cursor=db.cursor()

query='''use usuarios'''
cursor.execute(query)

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

        numeroWpp="+573003445373"
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
            return [SlotSet('usuarioRegistrado', 'si'),SlotSet('correoPSE', correo),SlotSet('banco', banco),SlotSet('id', id),SlotSet('nombre', nombre)]
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
class GenerarLink(Action):

    def name(self) -> Text:
        return "generarLinkRPA"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        error=False#obtener de la busqueda en la base de datos las facturas pagadas
        link='https://davivienda.com/pagoFactura'
        if error==False:
            #tracker.slots['errorRPA']='no'
            print('no hay error')
            dispatcher.utter_message(text='Puedes pagar tu factura en este link de '+tracker.get_slot('banco')+': '+link)
            return[SlotSet('errorRPA', 'no')]
        else:
            #tracker.slots['errorRPA']='si'
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
