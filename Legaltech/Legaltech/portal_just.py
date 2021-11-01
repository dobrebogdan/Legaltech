import requests
import xml.etree.ElementTree as ET

def get_cases(obiect_dosar, institutie='CurteadeApelBUCURESTI'):
    obiect_dosar_tag = ''
    if obiect_dosar:
        obiect_dosar_tag = f'<obiectDosar>{obiect_dosar}</obiectDosar>'

    institutie_tag = f'<institutie>{institutie}</institutie>'
    url = "http://portalquery.just.ro/Query.asmx"
    headers = {"content-type": "text/xml", "content-Length": "length"}
    body = f"""
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CautareDosare xmlns="portalquery.just.ro">
          {obiect_dosar_tag}
          {institutie_tag}
        </CautareDosare>
      </soap:Body>
    </soap:Envelope>
    """
    response = requests.post(url, data=body, headers=headers)
    return response.text


document_number = None
def get_ids_and_solutions(obiect_dosar, institutie='CurteadeApelBUCURESTI'):
    ids_and_solutions = []
    cases = get_cases(obiect_dosar, institutie)
    xml_tree_root = ET.fromstring(cases)
    for xml_file_element in xml_tree_root.iter('{portalquery.just.ro}DosarSedinta'):
        children = list(xml_file_element)
        for child in children:
            if child.tag == '{portalquery.just.ro}numarDocument' and child.text:
                global document_number
                document_number = child.text
            if child.tag == '{portalquery.just.ro}solutieSumar' and document_number:
                solution_summary = str(child.text)
                ids_and_solutions.append((document_number, solution_summary))
    return ids_and_solutions

ids_and_solutions = get_ids_and_solutions(obiect_dosar='divort')
print(ids_and_solutions)
