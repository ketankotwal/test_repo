import OpenSSL
from pyasn1.codec.der import decoder as der_decoder
from subj_alt_name import SubjectAltName
from pyasn1_modules.rfc2459 import CRLDistPointsSyntax , AuthorityInfoAccessSyntax, AccessDescription
import urllib

certname = 'cert.cer'
certfile = open('certs/'+ certname, 'r').read()
c = OpenSSL.crypto
cert = OpenSSL.crypto.load_certificate(c.FILETYPE_PEM, certfile)



dns_name = []
general_names = SubjectAltName()
crl_dist_points = CRLDistPointsSyntax()
for i in range(cert.get_extension_count()):
    ext = cert.get_extension(i)
    ext_name = ext.get_short_name()
    print ext_name
    if ext_name == 'subjectAltName':
        # PyOpenSSL returns extension data in ASN.1 encoded form
        ext_dat = ext.get_data()
        decoded_dat = der_decoder.decode(ext_dat, 
                                         asn1Spec=general_names)
        
        for name in decoded_dat:
            #print name
            if isinstance(name, SubjectAltName):
                for entry in range(len(name)):
                    #print entry
                    component = name.getComponentByPosition(entry)
                    #print component
                    san = str(component.getComponent())
                    print '\t' + san
                    dns_name.append(san)
    
    
    if ext_name == 'crlDistributionPoints':
        # PyOpenSSL returns extension data in ASN.1 encoded form
        ext_dat = ext.get_data()
        decoded_dat = der_decoder.decode(ext_dat, 
                                         asn1Spec=crl_dist_points)
        
        for name in decoded_dat:
            #print name
            if isinstance(name, CRLDistPointsSyntax):
                for entry in range(len(name)):
                    #print entry
                    component = name.getComponentByPosition(entry)
                    distpoint = component.getComponentByName('distributionPoint')
                    #print distpoint
                    #print dir(distpoint)
                    distpointvalue = distpoint.getComponentByName('fullName')
                    #print distpointvalue
                    for gen_name in distpointvalue:
                        #print gen_name.prettyPrint()
                        #print gen_name.getName()
                        url_name = gen_name.getComponentByName('uniformResourceIdentifier')
                        #print url_name
                        url_name_str = str(url_name)
                        print '\t' + url_name_str
                        crl_file = urllib.URLopener()
                        crl_file.retrieve(url_name_str, 'latest123.crl')
                    #san = str(component.getComponent())
                    #print '\t\t' + san
                    #dns_name.append(san)
    
    authInfoAccessSyntax = AuthorityInfoAccessSyntax()
    if ext_name == 'authorityInfoAccess':
        # PyOpenSSL returns extension data in ASN.1 encoded form
        ext_dat = ext.get_data()
        decoded_dat = der_decoder.decode(ext_dat, 
                                         asn1Spec=authInfoAccessSyntax)
        
        for authInfoAccess in decoded_dat:
            #print authInfoAccess
            if isinstance(authInfoAccess, AuthorityInfoAccessSyntax):
                for entry in range(len(authInfoAccess)):
                    accessDescription = authInfoAccess.getComponentByPosition(entry)
                    accessMethod = str(accessDescription.getComponentByName('accessMethod'))
                    ocsp_oid = '1.3.6.1.5.5.7.48.1'
                    if  ocsp_oid == accessMethod:
                        ocsp_url_generalname = accessDescription.getComponentByName('accessLocation')
                        ocsp_url = ocsp_url_generalname.getComponentByName('uniformResourceIdentifier')
                        print '\t' + str(ocsp_url)
                    