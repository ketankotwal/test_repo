import jks
import OpenSSL

cacerts = jks.KeyStore.load('C:\Program Files\Java\jdk1.8.0_25\jre\lib\security\cacerts', 'changeit')

print '\n\n'

for cert in cacerts.certs:
    x509obj = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, cert.cert)
    print x509obj.get_subject().commonName
    
    