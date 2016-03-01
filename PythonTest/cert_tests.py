import OpenSSL
from OpenSSL import *
import inspect


def show_cert(certname):
    from cryptography.hazmat.bindings.openssl.binding import Binding
    lib = Binding().lib    
    
    print '\n'
    print certname
    certfile = open('certs/'+ certname, 'r').read()
    c = OpenSSL.crypto
    cert = OpenSSL.crypto.load_certificate(c.FILETYPE_PEM, certfile)

    key = cert.get_pubkey()
    #print key.type() 
    #print key.bits()
    
    for index in range(0, cert.get_extension_count()):
        extn = cert.get_extension(index)
        print extn.get_short_name()
        print extn.get_data()

    from cryptography.hazmat.bindings.openssl.binding import Binding
    lib = Binding().lib
    print lib.EVP_PKEY_RSA
    print lib.EVP_PKEY_DSA
    print lib.EVP_PKEY_EC
    
    #print inspect.getargspec(lib.EVP_PKEY_get_attr)
    #print lib.EVP_PKEY_get_attr(key, None)
    #print lib.EVP_get_digestbyname(408)

c = OpenSSL.crypto
#dir(c)
#print lib.EC_GROUP_get_curve_name(lib.EVP_PKEY_EC)
#ENGINE_get_name
#print lib.EVP_get_cipherbyname(lib.EVP_PKEY_EC)
#EVP_get_digestbyname
#SSL_CIPHER_get_name

#print dir(lib)

#show_cert('cert.cer')
show_cert('google.cer')
#show_cert('digicert.cer')