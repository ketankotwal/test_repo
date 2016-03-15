from oscrypto import asymmetric
from ocspbuilder import OCSPRequestBuilder
from pyasn1_modules.rfc2560 import OCSPResponse, BasicOCSPResponse
from OpenSSL import crypto
import OpenSSL


id_cert_path = 'certs/pem/citi.co.in.pem'
issuer_cert_path = 'certs/pem/citi.intermediate.ca.pem'

id_cert_buf = open(id_cert_path, 'r').read()
issuer_cert_buf = open(issuer_cert_path, 'r').read()

id_cert = asymmetric.load_certificate(id_cert_buf)
issuer_cert = asymmetric.load_certificate(issuer_cert_buf)

id_cert_filebuf = open(id_cert_path, 'r').read()
id_cert_x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, id_cert_filebuf)

# print dir(id_cert_x509)
# print id_cert_x509.get_serial_number()
id_cert_serial_number = format(id_cert_x509.get_serial_number(), 'x')
print "Checking OCSP status for cert : " + id_cert_serial_number
print '\n'

builder = OCSPRequestBuilder(id_cert, issuer_cert)
ocsp_request = builder.build()
# print type(ocsp_request)

ocsp_req_dump = ocsp_request.dump()

with open('ocsp_request_citi.der', 'wb') as f:
    f.write(ocsp_request.dump())
    

ocsp_request_file_contents = open('ocsp_request.der', 'r').read()

# import httplib

ocsp_url = 'http://clients1.google.com/ocsp'
ocsp_url_citi = 'http://sr.symcd.com'

# conn = httplib.HTTPConnection(ocsp_url)
# conn.request("GET", ocsp_request_file_contents)
# resp = conn.getresponse()
# print resp
# print resp.status
# print resp.read()


import requests

resp = requests.post(ocsp_url_citi, ocsp_req_dump)

ocsp_response = resp.content

# print str(ocsp_response)

from pyasn1.codec.der import decoder as der_decoder
import pyasn1_modules.rfc2560

ocspResponse = OCSPResponse()
basicOcspResponse = BasicOCSPResponse()

decoded_resp = der_decoder.decode(ocsp_response, asn1Spec=ocspResponse)
# print dir(decoded_resp)
for resp in decoded_resp:
    # print type(resp)
    if isinstance(resp, OCSPResponse):
        ocsp_response_status = resp.getComponentByName('responseStatus')
        # print ocsp_response_status
        # print type(ocsp_response_status)
        ocsp_resp_bytes = resp.getComponentByName('responseBytes')
        ocsp_resp = ocsp_resp_bytes.getComponentByName('response') 
        basic_ocsp_response, _ = der_decoder.decode(ocsp_resp, asn1Spec=basicOcspResponse)
        tbs_response_data = basic_ocsp_response.getComponentByName('tbsResponseData')
        responses = tbs_response_data.getComponentByName('responses')
        for response in responses:
            print 'OCSP RESPONSE'
            # print response
            serial_no_long = long(response.getComponentByName('certID').getComponentByName('serialNumber'))
            serial_no = format(serial_no_long, 'x')            
            # print type(serial_no)
            # print str(serial_no)
            print 'Verified cert with Serial Number : ' + serial_no
            print 'Status : ' + response.getComponentByName('certStatus').getName()
        

# ocsp_resp_status = decoded_resp.getComponentByName('responseStatus')
# print ocsp_resp_status







