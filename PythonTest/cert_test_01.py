from pyasn1_modules import pem, rfc2459
from pyasn1.codec.der import decoder
from pyasn1_modules.rfc2459 import GeneralNames
from pyasn1.type import univ
#from ndg.httpsclient.subj_alt_name import SubjectAltName

substrate = pem.readPemFromFile(open('certs/cert.cer'))
cert = decoder.decode(substrate, asn1Spec=rfc2459.Certificate())[0]
print type(cert)
print str(cert.__class__)
tbsCertificate = cert.getComponentByName('tbsCertificate')
print str(tbsCertificate.__class__)
subject = tbsCertificate.getComponentByName('subject')
print str(subject.__class__)
print subject
extensions = tbsCertificate.getComponentByName('extensions')
print str(extensions.__class__)
for i in extensions:  
    extnID = str(i.getComponentByName('extnID'))
    extnValue = str(i.getComponentByName('extnValue'))
    print  extnID + ' : ' + extnValue
    decodedStr = decoder.decode(extnValue, asn1Spec = univ.Any())[0]
    print decodedStr
    print str(decodedStr.__class__)
    tagMap = decodedStr.getTagMap()
    print tagMap
    print str(tagMap.__class__)
    posMap = tagMap.getPosMap()
    print posMap
    print str(posMap.__class__)
    value0 = posMap.values()[0]
    print str(value0.__class__)
    hexStr = value0.prettyPrint()
    print hexStr
    #print bytearray.fromhex(hexStr).decode()
    #plainStr = hexStr.decode('hex')
    #print plainStr    
    #print tagMap.getDef()
    #print tagMap.getNegMap()
    #Check if extension is subjectAltName.  
    #if "2.5.29.17" == str(i.getComponentByName('extnID')):  
    #    buf = str(i.getComponentByName('extnValue'))  
    #    gName = decoder.decode(buf, asn1Spec = GeneralNames())[0]  
    #    print gName.prettyPrint()  
#print type(cert.prettyPrint())