from pyasn1.codec.der import decoder, encoder
from x509 import Certificate, Name, DirectoryString, MAX
  
from pyasn1.type import tag,namedtype,namedval,univ,constraint,char,useful,base  
  
class OtherName(univ.OctetString): pass  
class ORAddress(univ.OctetString): pass  
class EDIPartyName(univ.Sequence):  
    componentType = namedtype.NamedTypes(  
        namedtype.OptionalNamedType('nameAssigner', DirectoryString().subtype(  
            explicitTag=tag.Tag(  
                tag.tagClassContext,  
                tag.tagFormatSimple,  
                0  
            ))  
        ),  
        namedtype.NamedType('partyName', DirectoryString().subtype(  
            explicitTag=tag.Tag(  
                tag.tagClassContext,  
                tag.tagFormatSimple,  
                1  
            ))  
        )  
    )  
class GeneralName(univ.Choice):  
    componentType = namedtype.NamedTypes(  
        namedtype.NamedType('otherName', OtherName().subtype(  
            explicitTag=tag.Tag(  
                tag.tagClassContext,  
                tag.tagFormatSimple,  
                0  
            ))  
        ),  
        namedtype.NamedType('rfc822Name', char.IA5String().subtype(  
            explicitTag=tag.Tag(  
                tag.tagClassContext,  
                tag.tagFormatSimple,  
                1  
            ))  
        ),  
        namedtype.NamedType('dNSName', char.IA5String().subtype(  
            explicitTag=tag.Tag(  
                tag.tagClassContext,  
                tag.tagFormatSimple,  
                2  
            ))  
        ),  
        namedtype.NamedType('ORAddress', ORAddress().subtype(  
            explicitTag=tag.Tag(  
                tag.tagClassContext,  
                tag.tagFormatSimple,  
                3  
            ))  
        ),  
        namedtype.NamedType('directoryName', Name().subtype(  
            explicitTag=tag.Tag(  
                tag.tagClassContext,  
                tag.tagFormatSimple,  
                4  
            ))  
        ),  
        namedtype.NamedType('ediPartyName', EDIPartyName().subtype(  
            explicitTag=tag.Tag(  
                tag.tagClassContext,  
                tag.tagFormatSimple,  
                5  
            ))  
        ),  
        namedtype.NamedType('uniformResourceIdentifier', char.IA5String().subtype(  
            explicitTag=tag.Tag(  
                tag.tagClassContext,  
                tag.tagFormatSimple,  
                6  
            ))  
        ),  
        namedtype.NamedType('iPAddress', univ.OctetString().subtype(  
            explicitTag=tag.Tag(  
                tag.tagClassContext,  
                tag.tagFormatSimple,  
                7  
            ))  
        ),  
        namedtype.NamedType('registeredID', univ.ObjectIdentifier().subtype(  
            explicitTag=tag.Tag(  
                tag.tagClassContext,  
                tag.tagFormatSimple,  
                8  
            ))  
        )  
    )  
  
class GeneralNames(univ.SequenceOf):  
    componentType = GeneralName()  
    sizeSpec = univ.SequenceOf.sizeSpec + constraint.ValueSizeConstraint(1, MAX)  
 
print "START..."  
buf = open("certs/cert.cer", "rb").read(-1)  
print "Step 1"  
cert = decoder.decode(buf, asn1Spec = Certificate())[0]  
print "Got cert..."
  
tbsCert = cert.getComponentByName('tbsCertificate')  
extensions = tbsCert.getComponentByName('extensions')  
print "Entering loop..."
for i in extensions:  
    print i.getComponentByName('extnID')
    #Check if extension is subjectAltName.  
    if "2.5.29.17" == str(i.getComponentByName('extnID')):  
        buf = str(i.getComponentByName('extnValue'))  
        gName = decoder.decode(buf, asn1Spec = GeneralNames())[0]  
        print gName.prettyPrint()  