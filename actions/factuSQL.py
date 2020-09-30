#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:29:55 2020

@author: franciscoreales
"""

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
def guardarFB(id_usuario,nombre_usuario,correo_pse,numero_wpp,feed_back):
    if id_usuario is not None:
        consulta='''
        insert into userFeedback(id,nombre,correoPSE,numeroWPP,feedback) values (id_usuario,"nombre_usuario", "correo_pse","numero_wpp","feed_back")
        ;'''.replace("id_usuario",str(id_usuario)).replace("nombre_usuario",str(nombre_usuario)).replace("correo_pse",str(correo_pse)).replace("numero_wpp",str(numero_wpp)).replace("feed_back",str(feed_back))
        cursor.execute(consulta)
        db.commit()
        print("guardado exitoso")
        return []
    else:
        print("no se pudo guardar")
        return []


db=sql.connect('factu-db.c15hdm9dgrjl.us-east-2.rds.amazonaws.com','admin','Hostinguer.123')

cursor=db.cursor()

query='''use usuarios'''
cursor.execute(query)



# numeroFactura='5555'#None
# empresa='chec'#None
# tipoFactura='electricidad'
# id_usuario='2'
# registrarFacturaDB(id_usuario,numeroFactura,empresa,tipoFactura)


# id_usuario='2'

# print(validarFactura(id_usuario,numeroFactura,empresa,tipoFactura))
# numeroWpp="+573003377373"

# print(validarUsuario(numeroWpp))

# cursor.execute("select version()")

# #query='''create database usuarios'''
# #cursor.execute(query)


# query='''use usuarios'''
# cursor.execute(query)

# # query='''
# # create table userData(
# # id int not null auto_increment,
# # nombre text,
# # numeroWpp text,
# # correoPSE text,
# # banco text,
# # primary key (id)
# # );
# # '''
# # cursor.execute(query)

# query='''
# create table facturas(
# idFactura int not null auto_increment,
# id int not null,
# numeroFactura text,
# empresa text,
# tipoFactura text,
# primary key (idFactura),
# foreign key (id) references userData(id)
# );
# '''
# cursor.execute(query)

# query='''show tables'''
# cursor.execute(query)


