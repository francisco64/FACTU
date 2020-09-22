## usuario no registrado
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* pagoFactura OR yaRegistrado OR pagoFactura+infoFactura   
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_sigueSinRegistro
* afirmacion
  - utter_sonriente

## usuario no registrado
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* yaRegistrado   
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo

## usuario no registrado
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* pagoFactura  
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enviaFactura

## usuario no registrado
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* pagoFactura+infoFactura{"tipoFactura":"agua"}  
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enviaFactura

## usuario no registrado
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* afirmacion
  - utter_sonriente  
* pagoFactura+infoFactura{"tipoFactura":"agua"}  
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enviaFactura

## sigue sin registro
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* afirmacion
  - utter_sonriente
* yaRegistrado    
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_sigueSinRegistro
* afirmacion
  - utter_sonriente
* pagoFactura+infoFactura{"numeroFactura":"64374"} OR pagoFactura
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_sigueSinRegistro

## sigue sin registro
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* afirmacion
  - utter_sonriente
* yaRegistrado    
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_sigueSinRegistro
* afirmacion
  - utter_sonriente
* pagoFactura
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_sigueSinRegistro

## sigue sin registro
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* afirmacion
  - utter_sonriente
* yaRegistrado    
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_sigueSinRegistro
* afirmacion
  - utter_sonriente
* pagoFactura+infoFactura{"empresa":"codensa"}
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_sigueSinRegistro

## sigue sin registro
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* afirmacion
  - utter_sonriente
* yaRegistrado    
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_sigueSinRegistro
* afirmacion
  - utter_sonriente
* pagoFactura+infoFactura{"numeroFactura":"364343","empresa":"chec"}
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_sigueSinRegistro

## usuario no registrado
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* pagoFactura+infoFactura{"numeroFactura":"745634-3","empresa":"codensa"}  
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enviaFactura

## usuario no registrado
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* afirmacion
  - utter_sonriente
* pagoFactura+infoFactura{"numeroFactura":"745634-3","empresa":"codensa"}  
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enviaFactura

## usuario no registrado
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* pagoFactura+infoFactura{"numeroFactura":"745634-3"}  
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_queEmpresa
* infoFactura{"empresa":"acueducto de bogotá"}  
  - utter_confirmarFactura

## usuario no registrado
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* afirmacion
  - utter_sonriente
* pagoFactura+infoFactura{"numeroFactura":"745634-3"}  
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_queEmpresa
* infoFactura{"empresa":"acueducto de bogotá"}  
  - utter_confirmarFactura

## usuario no registrado
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* pagoFactura+infoFactura{"empresa":"chec"}  
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_queNumeroFactura
* infoFactura{"numeroFactura":"3627632-2"}  
  - utter_confirmarFactura

## usuario no registrado
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* afirmacion
  - utter_sonriente  
* pagoFactura+infoFactura{"empresa":"chec"}  
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_queNumeroFactura
* infoFactura{"numeroFactura":"3627632-2"}  
  - utter_confirmarFactura

##usuario registrado + pagoFactura sin entities + infoFactura (empresa y numero) +datos estan bien+no hay error rpa+no necesita algo mas
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura
  - utter_enviaFactura
* infoFactura{"empresa":"acueducto de bogotá","numeroFactura":"44252-5"}
  - utter_confirmarFactura
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* afirmacion
  - guardarFactura  
  - utter_algoMas
* negacion
  - utter_fueUnPlacer
* afirmacion OR gracias
  - utter_sonriente

## sin saludo
* pagoFactura
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enviaFactura
* infoFactura{"empresa":"acueducto de bogotá","numeroFactura":"44252-5"}
  - utter_confirmarFactura
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* afirmacion
  - guardarFactura  
  - utter_algoMas
* negacion
  - utter_fueUnPlacer
* afirmacion OR gracias
  - utter_sonriente

##--
* pagoFactura
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* afirmacion
  - utter_sonriente
* yaRegistrado
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enviaFactura

##--
* pagoFactura
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* yaRegistrado
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enviaFactura

##--
* pagoFactura
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* yaRegistrado
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_sigueSinRegistro

##--
* pagoFactura+infoFactura{"empresa":"codensa"} OR pagoFactura+infoFactura{"numeroFactura":"3562562"} OR pagoFactura+infoFactura{"numeroFactura":"3562562","empresa":"codensa"}
  - slot{"usuarioRegistrado":"no"}
  - utter_noRegistrado
* yaRegistrado
  - validarRegistro
  - slot{"usuarioRegistrado":"no"}
  - utter_sigueSinRegistro

##usuario registrado + pagoFactura sin entities + infoFactura (empresa y numero) +datos estan bien+hay error rpa
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura
  - utter_enviaFactura
* infoFactura{"empresa":"acueducto de bogotá","numeroFactura":"44252-5"}
  - utter_confirmarFactura
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"si"}

##usuario registrado + pagoFactura sin entities + infoFactura (empresa) +datos estan bien+no hay error rpa+no necesita algo mas
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura
  - utter_enviaFactura
* infoFactura{"numeroFactura":"63536-4"}
  - buscarFactura
  - slot{"facturaRegistrada":"no"}
  - utter_queEmpresa
* infoFactura{"empresa":"acueducto de bogotá"}  
  - utter_confirmarFactura
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* afirmacion
  - guardarFactura  
  - utter_algoMas
* negacion
  - utter_fueUnPlacer
* afirmacion OR gracias
  - utter_sonriente

##usuario registrado + pagoFactura sin entities + infoFactura (empresa) +datos estan bien+no hay error rpa+no necesita algo mas
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura
  - utter_enviaFactura
* infoFactura{"empresa":"acueducto de bogotá"}
  - buscarFactura
  - slot{"facturaRegistrada":"no"}
  - utter_queNumeroFactura
* infoFactura{"numeroFactura":"63536-4"}  
  - utter_confirmarFactura
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* afirmacion
  - guardarFactura  
  - utter_algoMas
* negacion
  - utter_fueUnPlacer
* afirmacion OR gracias
  - utter_sonriente

##usuario registrado + pagoFactura sin entities+ infoFactura (numeroFactura) +datos estan bien+hubo un error rpa
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura
  - utter_enviaFactura
* infoFactura{"numeroFactura":"535356-2"}
  - buscarFactura
  - slot{"facturaRegistrada":"no"}
  - utter_queEmpresa
* infoFactura{"empresa":"chec"}  
  - utter_confirmarFactura
* afirmacion
  - utter_generareLink
  - generarLinkRPA  
  - slot{"errorRPA":"si"}

##usuario registrado+pago de factura con numero + factura no existe  + datos estan bien + no hya error rpa
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura+infoFactura{"numeroFactura":"53535-4"}
  - buscarFactura
  - slot{"facturaRegistrada":"no"}
  - utter_queEmpresa
* infoFactura{"empresa":"acueducto de bogotá"}
  - utter_confirmarFactura
* afirmacion
  - utter_generareLink
  - generarLinkRPA   
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* afirmacion
  - guardarFactura  
  - utter_algoMas
* negacion
  - utter_fueUnPlacer
* afirmacion OR gracias  
  - utter_sonriente

##--
* pagoFactura+infoFactura{"numeroFactura":"53535-4"}
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - buscarFactura
  - slot{"facturaRegistrada":"si"}
  - slot{"tipoFactura":"agua"}
  - slot{"empresa":"codensa"}
  - slot{"numeroFactura":"56253-2"}
  - utter_yaPagado
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_algoMas

##--
* pagoFactura+infoFactura{"empresa":"efigas"}
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - buscarFactura
  - slot{"facturaRegistrada":"si"}
  - slot{"tipoFactura":"agua"}
  - slot{"empresa":"codensa"}
  - slot{"numeroFactura":"56253-2"}
  - utter_yaPagado
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_algoMas

##--
* pagoFactura+infoFactura{"numeroFactura":"53535-4"}
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - buscarFactura
  - slot{"facturaRegistrada":"si"}
  - slot{"tipoFactura":"agua"}
  - slot{"empresa":"codensa"}
  - slot{"numeroFactura":"56253-2"}
  - utter_yaPagado
* negacion
  - utter_queEmpresa
* infoFactura{"empresa":"codensa"}
  - slot{"empresa":"codensa"}
  - utter_confirmarFactura

##--
* pagoFactura+infoFactura{"empresa":"efigas"}
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - buscarFactura
  - slot{"facturaRegistrada":"si"}
  - slot{"tipoFactura":"agua"}
  - slot{"empresa":"codensa"}
  - slot{"numeroFactura":"56253-2"}
  - utter_yaPagado
* negacion
  - utter_queNumeroFactura
* infoFactura{"numeroFactura":"7646734"}
  - slot{"numeroFactura":"7646734"}
  - utter_confirmarFactura

##--
* pagoFactura+infoFactura{"empresa":"acueducto de bogotá","numeroFactura":"44252-5"}
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_confirmarFactura

##--
* pagoFactura+infoFactura{"tipoFactura":"gas"}
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - buscarFactura
  - slot{"facturaRegistrada":"si"}
  - slot{"tipoFactura":"agua"}
  - slot{"empresa":"codensa"}
  - slot{"numeroFactura":"56253-2"}
  - utter_yaPagado
* negacion
  - utter_enviaFactura

##--
* pagoFactura+infoFactura{"tipoFactura":"gas"}
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - buscarFactura
  - slot{"facturaRegistrada":"si"}
  - slot{"tipoFactura":"agua"}
  - slot{"empresa":"codensa"}
  - slot{"numeroFactura":"56253-2"}
  - utter_yaPagado
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_algoMas

##usuario registrado+pago de factura con empresa+ factura no existe  + datos estan bien
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura+infoFactura{"empresa":"codensa"}
  - buscarFactura
  - slot{"facturaRegistrada":"no"}
  - utter_queNumeroFactura
* infoFactura{"numeroFactura":"53562-5"}
  - utter_confirmarFactura
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* afirmacion
  - guardarFactura  
  - utter_algoMas
* negacion
  - utter_fueUnPlacer
* afirmacion OR gracias
  - utter_sonriente

##usuario registrado+pago de factura con numero y empresa + factura no existe  + datos estan bien + hubo error rpa
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura+infoFactura{"empresa":"acueducto de bogotá","numeroFactura":"44252-5"}
  - utter_confirmarFactura
* afirmacion
  - utter_generareLink
  - generarLinkRPA   
  - slot{"errorRPA":"si"}

##usuario registrado + pagoFactura + infoFactura (con tipo de factura) +datos estan bien+ no hubo error rpa
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura+infoFactura{"tipoFactura":"agua"}
  - buscarFactura
  - slot{"facturaRegistrada":"no"}
  - utter_enviaFactura
* infoFactura{"empresa":"acueducto de bogotá","numeroFactura":"44252-5"}
  - utter_confirmarFactura
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* afirmacion
  - guardarFactura  
  - utter_algoMas
* negacion
  - utter_fueUnPlacer
* afirmacion OR gracias  
  - utter_sonriente

##fue un placer----ok
  - utter_fueUnPlacer
* afirmacion OR gracias
  - utter_sonriente

## factura si existe tipoFactura
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura+infoFactura{"tipoFactura":"agua"}
  - buscarFactura
  - slot{"facturaRegistrada":"si"}
  - slot{"tipoFactura":"agua"}
  - slot{"empresa":"codensa"}
  - slot{"numeroFactura":"56253-2"}
  - utter_yaPagado
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_algoMas
* negacion
  - utter_fueUnPlacer
* afirmacion OR gracias
  - utter_sonriente

## factura si existe empresa
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura+infoFactura{"empresa":"codensa"}
  - buscarFactura
  - slot{"facturaRegistrada":"si"}
  - slot{"tipoFactura":"agua"}
  - slot{"empresa":"codensa"}
  - slot{"numeroFactura":"56253-2"}
  - utter_yaPagado
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_algoMas
* negacion
  - utter_fueUnPlacer
* afirmacion OR gracias
  - utter_sonriente

## factura si existe empresa
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura+infoFactura{"empresa":"codensa"}
  - buscarFactura
  - slot{"facturaRegistrada":"si"}
  - slot{"tipoFactura":"agua"}
  - slot{"empresa":"codensa"}
  - slot{"numeroFactura":"56253-2"}
  - utter_yaPagado
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_algoMas
* afirmacion
  - utter_enQueTeAyudo

## factura si existe numero
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura+infoFactura{"numeroFactura":"63663-2"}
  - buscarFactura
  - slot{"facturaRegistrada":"si"}
  - slot{"tipoFactura":"agua"}
  - slot{"empresa":"codensa"}
  - slot{"numeroFactura":"56253-2"}
  - utter_yaPagado
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_algoMas
* negacion
  - utter_fueUnPlacer  
* afirmacion OR gracias
  - utter_sonriente

##factura si existe pero no se paga la misma
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura+infoFactura{"numeroFactura":"63663-2"}
  - buscarFactura
  - slot{"facturaRegistrada":"si"}
  - slot{"tipoFactura":"agua"}
  - slot{"empresa":"codensa"}
  - slot{"numeroFactura":"56253-2"}
  - utter_yaPagado
* negacion
  - utter_queEmpresa
* infoFactura{"empresa":"codensa"}
  - slot{"empresa":"codensa"}
  - utter_confirmarFactura
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* afirmacion
  - guardarFactura  
  - utter_algoMas
* negacion
  - utter_fueUnPlacer
* afirmacion OR gracias
  - utter_sonriente

##factura si existe pero no se paga la misma
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura+infoFactura{"empresa":"enel"}
  - buscarFactura
  - slot{"facturaRegistrada":"si"}
  - slot{"tipoFactura":"agua"}
  - slot{"empresa":"codensa"}
  - slot{"numeroFactura":"56253-2"}
  - utter_yaPagado
* negacion
  - utter_queNumeroFactura
  * infoFactura{"numeroFactura":"3523-2"}
  - slot{"numeroFactura":"3523-2"}
  - utter_confirmarFactura
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* afirmacion
  - guardarFactura  
  - utter_algoMas
* negacion
  - utter_fueUnPlacer
* afirmacion OR gracias
  - utter_sonriente

##no guarde la factura
  - utter_guardarFactura
* negacion  
  - utter_algoMas
* negacion
  - utter_fueUnPlacer
* afirmacion OR gracias
  - utter_sonriente

##no guarde factura
  - utter_guardarFactura
* negacion  
  - utter_algoMas
* afirmacion
  - utter_enQueTeAyudo

##factura si existe pero no se paga la misma
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura+infoFactura{"tipoFactura":"agua"}
  - buscarFactura
  - slot{"facturaRegistrada":"si"}
  - slot{"tipoFactura":"agua"}
  - slot{"empresa":"codensa"}
  - slot{"numeroFactura":"56253-2"}
  - utter_yaPagado
* negacion
  - utter_enviaFactura

##factura si existe pero no se paga la misma
* saludo
  - utter_saludo
  - validarRegistro
  - slot{"usuarioRegistrado":"si"}
  - utter_enQueTeAyudo  
* pagoFactura+infoFactura{"tipoFactura":"agua"}
  - buscarFactura
  - slot{"facturaRegistrada":"si"}
  - slot{"tipoFactura":"agua"}
  - slot{"empresa":"codensa"}
  - slot{"numeroFactura":"56253-2"}
  - utter_yaPagado
* afirmacion
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_algoMas
* negacion
  - utter_fueUnPlacer
* afirmacion OR gracias
  - utter_sonriente

## confirma factura equivocada
  - utter_confirmarFactura
* negacion
  - utter_queCambio
* infoFactura{"numeroFactura":"574535","empresa":"codensa"}
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* afirmacion
  - guardarFactura
  - utter_algoMas
* negacion
  - utter_fueUnPlacer
* afirmacion OR gracias
  - utter_sonriente

## confirma factura equivocada
  - utter_confirmarFactura
* negacion
  - utter_queCambio
* infoFactura{"numeroFactura":"574535"}
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* afirmacion
  - guardarFactura
  - utter_algoMas

## confirma factura equivocada
  - utter_confirmarFactura
* negacion
  - utter_queCambio
* infoFactura{"empresa":"codensa"}
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* negacion
  - utter_algoMas

## con info factura
  - utter_confirmarFactura
* infoFactura{"numeroFactura":"574535"}
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* afirmacion
  - guardarFactura
  - utter_algoMas

## con info factura
  - utter_confirmarFactura
* infoFactura{"numeroFactura":"574535","empresa":"codensa"}
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* negacion
  - utter_algoMas

## con info factura
  - utter_confirmarFactura
* infoFactura{"empresa":"codensa"}
  - utter_generareLink
  - generarLinkRPA
  - slot{"errorRPA":"no"}
  - utter_guardarFactura
* afirmacion
  - guardarFactura
  - utter_algoMas

## New Story

* saludo
    - utter_saludo
    - validarRegistro
    - slot{"usuarioRegistrado":"si"}
    - slot{"correoPSE":"freales@javeriana.edu.co"}
    - slot{"banco":"davivienda"}
    - slot{"id":1}
    - slot{"nombre":"Francisco"}
    - utter_enQueTeAyudo
* pagoFactura+infoFactura{"tipoFactura":"agua"}
    - slot{"tipoFactura":"agua"}
    - slot{"tipoFactura":"agua"}
    - buscarFactura
    - slot{"facturaRegistrada":"no"}
    - utter_enviaFactura
* infoFactura{"empresa":"codensa"}
    - slot{"empresa":"codensa"}
    - slot{"empresa":"codensa"}
    - buscarFactura
    - slot{"facturaRegistrada":"no"}
    - utter_queNumeroFactura
* infoFactura{"empresa":"acueducto de bogotá"}
    - slot{"empresa":"acueducto de bogotá"}
    - slot{"tipoFactura":"agua"}
    - slot{"empresa":"codensa"}
    - slot{"empresa":"acueducto de bogotá"}
    - utter_queNumeroFactura
* infoFactura{"numeroFactura":"646362"}
    - slot{"numeroFactura":"646362"}
    - slot{"numeroFactura":"646362"}
    - utter_confirmarFactura
* afirmacion
    - utter_generareLink
    - generarLinkRPA
    - slot{"errorRPA":"no"}
    - utter_guardarFactura
    - slot{"tipoFactura":"agua"}
    - slot{"empresa":"codensa"}
    - slot{"empresa":"acueducto de bogotá"}
    - slot{"numeroFactura":"646362"}
* afirmacion
    - guardarFactura
    - utter_algoMas
    - slot{"tipoFactura":"agua"}
    - slot{"empresa":"codensa"}
    - slot{"empresa":"acueducto de bogotá"}
    - slot{"numeroFactura":"646362"}
* negacion
    - utter_fueUnPlacer
* afirmacion
    - utter_sonriente
