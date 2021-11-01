import requests
url = "http://portalquery.just.ro/Query.asmx"

headers = {"content-type" : "text/xml", "content-Length": "length"}
body = """
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CautareDosare xmlns="portalquery.just.ro">
      <obiectDosar>furt calificat</obiectDosar>
    </CautareDosare>
  </soap:Body>
</soap:Envelope>
"""



response = requests.post(url, data = body, headers = headers)
print(response)
print(response.text)
"""
<numarDosar>2779/108/2019</numarDosar>
<institutie>CurteadeApelTIMISOARA</institutie>
<numarDosar>string</numarDosar>
<obiectDosar>string</obiectDosar>
<numeParte>string</numeParte>
<institutie>CurteadeApelBUCURESTI or TribunalulBUCURESTI or JudecatoriaSECTORUL4BUCURESTI or TribunalulTIMIS or CurteadeApelBACAU or CurteadeApelCLUJ or CurteadeApelORADEA or CurteadeApelCONSTANTA or CurteadeApelSUCEAVA or TribunalulBOTOSANI or CurteadeApelPLOIESTI or CurteadeApelTARGUMURES or CurteadeApelGALATI or CurteadeApelIASI or CurteadeApelPITESTI or CurteadeApelCRAIOVA or JudecatoriaARAD or CurteadeApelALBAIULIA or CurteadeApelTIMISOARA or TribunalulBRASOV or TribunalulDOLJ or CurteadeApelBRASOV or CurteaMilitaradeApelBUCURESTI or TribunalulSATUMARE or TribunalulSALAJ or TribunalulSIBIU or TribunalulSUCEAVA or TribunalulTELEORMAN or TribunalulTULCEA or TribunalulVASLUI or TribunalulVALCEA or TribunalulVRANCEA or TribunalulMilitarBUCURESTI or TribunalulILFOV or JudecatoriaBUFTEA or TribunalulGORJ or TribunalulHARGHITA or TribunalulHUNEDOARA or TribunalulIALOMITA or TribunalulIASI or TribunalulMARAMURES or TribunalulMEHEDINTI or TribunalulMURES or TribunalulNEAMT or TribunalulOLT or TribunalulPRAHOVA or TribunalulALBA or TribunalulARAD or TribunalulARGES or TribunalulBACAU or TribunalulBIHOR or TribunalulBISTRITANASAUD or TribunalulBRAILA or TribunalulBUZAU or TribunalulCARASSEVERIN or TribunalulCALARASI or TribunalulCLUJ or TribunalulCONSTANTA or TribunalulCOVASNA or TribunalulDAMBOVITA or TribunalulGALATI or TribunalulGIURGIU or JudecatoriaADJUD or JudecatoriaAGNITA or JudecatoriaAIUD or JudecatoriaALBAIULIA or JudecatoriaALESD or JudecatoriaBABADAG or JudecatoriaBACAU or JudecatoriaBAIADEARAMA or JudecatoriaBAIAMARE or JudecatoriaBAILESTI or JudecatoriaBALS or JudecatoriaBALCESTI or JudecatoriaBECLEAN or JudecatoriaBEIUS or JudecatoriaBICAZ or JudecatoriaBARLAD or JudecatoriaBISTRITA or JudecatoriaBLAJ or JudecatoriaBOLINTINVALE or JudecatoriaBOTOSANI or JudecatoriaBOZOVICI or JudecatoriaBRAD or JudecatoriaBRAILA or JudecatoriaBRASOV or JudecatoriaBREZOI or JudecatoriaBUHUSI or JudecatoriaBUZAU or JudecatoriaCALAFAT or JudecatoriaCALARASI or JudecatoriaCAMPENI or JudecatoriaCAMPINA or JudecatoriaCAMPULUNG or JudecatoriaCAMPULUNGMOLDOVENESC or JudecatoriaCARACAL or JudecatoriaCARANSEBES or JudecatoriaCHISINEUCRIS or JudecatoriaCLUJNAPOCA or JudecatoriaCONSTANTA or JudecatoriaCORABIA or JudecatoriaCOSTESTI or JudecatoriaCRAIOVA or JudecatoriaCURTEADEARGES or JudecatoriaDarabani or JudecatoriaCAREI or JudecatoriaDEJ or JudecatoriaDETA or JudecatoriaDEVA or JudecatoriaDOROHOI or JudecatoriaDRAGASANI or JudecatoriaDRAGOMIRESTI or JudecatoriaDROBETATURNUSEVERIN or JudecatoriaFAGARAS or JudecatoriaFALTICENI or JudecatoriaFAUREI or JudecatoriaFETESTI or JudecatoriaFILIASI or JudecatoriaFOCSANI or JudecatoriaGAESTI or JudecatoriaGALATI or JudecatoriaGHEORGHENI or JudecatoriaGHERLA or JudecatoriaGIURGIU or JudecatoriaGURAHUMORULUI or JudecatoriaGURAHONT or JudecatoriaHARLAU or JudecatoriaHATEG or JudecatoriaHOREZU or JudecatoriaHUEDIN or JudecatoriaHUNEDOARA or JudecatoriaHUSI or JudecatoriaIASI or JudecatoriaINEU or JudecatoriaINSURATEI or JudecatoriaINTORSURABUZAULUI or JudecatoriaLEHLIUGARA or JudecatoriaLIPOVA or JudecatoriaLUDUS or JudecatoriaLUGOJ or JudecatoriaMACIN or JudecatoriaMANGALIA or JudecatoriaMARGHITA or JudecatoriaMEDGIDIA or JudecatoriaMEDIAS or JudecatoriaMIERCUREACIUC or JudecatoriaMIZIL or JudecatoriaMOINESTI or JudecatoriaMOLDOVANOUA or JudecatoriaMORENI or JudecatoriaMOTRU or JudecatoriaMURGENI or JudecatoriaNASAUD or JudecatoriaNEGRESTIOAS or JudecatoriaNOVACI or JudecatoriaODORHEIULSECUIESC or JudecatoriaOLTENITA or JudecatoriaONESTI or JudecatoriaORADEA or JudecatoriaORASTIE or JudecatoriaORAVITA or JudecatoriaORSOVA or JudecatoriaPANCIU or JudecatoriaPATARLAGELE or JudecatoriaPETROSANI or JudecatoriaPIATRANEAMT or JudecatoriaPITESTI or JudecatoriaPLOIESTI or JudecatoriaPOGOANELE or JudecatoriaPUCIOASA or JudecatoriaRACARI or JudecatoriaRADAUTI or JudecatoriaRADUCANENI or JudecatoriaRAMNICUSARAT or JudecatoriaRAMNICUVALCEA or JudecatoriaREGHIN or JudecatoriaRESITA or JudecatoriaROMAN or JudecatoriaROSIORIDEVEDE or JudecatoriaRUPEA or JudecatoriaSALISTE or JudecatoriaSANNICOLAULMARE or JudecatoriaSATUMARE or JudecatoriaSAVENI or JudecatoriaSEBES or JudecatoriaSECTORUL1BUCURESTI or JudecatoriaSECTORUL2BUCURESTI or JudecatoriaSECTORUL3BUCURESTI or JudecatoriaSECTORUL5BUCURESTI or JudecatoriaSECTORUL6BUCURESTI or JudecatoriaSEGARCEA or JudecatoriaSFANTUGHEORGHE or JudecatoriaSIBIU or JudecatoriaSIGHETUMARMATIEI or JudecatoriaSIGHISOARA or JudecatoriaSIMLEULSILVANIEI or JudecatoriaSINAIA or JudecatoriaSLATINA or JudecatoriaSLOBOZIA or JudecatoriaSTREHAIA or JudecatoriaSUCEAVA or JudecatoriaTARGOVISTE or JudecatoriaTARGUBUJOR or JudecatoriaTARGUCARBUNESTI or JudecatoriaTARGUJIU or JudecatoriaTARGULAPUS or JudecatoriaTARGUMURES or JudecatoriaTARGUNEAMT or JudecatoriaTARGUSECUIESC or JudecatoriaTARNAVENI or JudecatoriaTECUCI or JudecatoriaTIMISOARA or JudecatoriaTOPLITA or JudecatoriaTULCEA or JudecatoriaTURDA or JudecatoriaTURNUMAGURELE or JudecatoriaURZICENI or JudecatoriaVALENIIDEMUNTE or JudecatoriaVANJUMARE or JudecatoriaVASLUI or JudecatoriaVATRADORNEI or JudecatoriaVIDELE or JudecatoriaVISEUDESUS or JudecatoriaZALAU or JudecatoriaZARNESTI or JudecatoriaZIMNICEA or TribunalulMilitarIASI or JudecatoriaALEXANDRIA or TribunalulMilitarTIMISOARA or TribunalulMilitarCLUJNAPOCA or TribunalulMilitarTeritorialBUCURESTI or JudecatoriaAVRIG or JudecatoriaTOPOLOVENI or JudecatoriaPODUTURCULUI or JudecatoriaFAGET or JudecatoriaSALONTA or JudecatoriaLIESTI or JudecatoriaHARSOVA or JudecatoriaSOMCUTAMARE or JudecatoriaPASCANI or TribunalulComercialARGES or TribunalulComercialCLUJ or TribunalulComercialMURES or TribunalulpentruminoriSifamilieBRASOV or JudecatoriaCORNETU or JudecatoriaJIBOU</institutie>
<dataStart>dateTime</dataStart>
<dataStop>dateTime</dataStop>
"""