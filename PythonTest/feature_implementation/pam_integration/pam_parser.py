
class Cracklib_Dummy_Class:
    
    DIFF_OK = 101
    DIG_CREDIT = 102
    LOW_CREDIT = 103
    MIN_LENGTH = 104
    OTH_CREDIT = 105
    UP_CREDIT = 106
    
    def FascistCheck(self):
        print '\n'
        print 'Printing cracklib values ...'
        print 'DIFF_OK = ' + str(self.DIFF_OK)
        print 'DIG_CREDIT = ' + str(self.DIG_CREDIT)
        print 'LOW_CREDIT = ' + str(self.LOW_CREDIT)
        print 'MIN_LENGTH = ' + str(self.MIN_LENGTH)
        print 'OTH_CREDIT = ' + str(self.OTH_CREDIT)
        print 'UP_CREDIT = ' + str(self.UP_CREDIT)

# path = 'system-auth'
sys_auth_path = 'system-auth'
sys_auth = open(sys_auth_path, 'r')

pam_cracklib_text = 'pam_cracklib.so'

matching_lines = []
attributes_dict = {
                    'minlen'    :   'MIN_LENGTH',
                    'lcredit'   :   'LOW_CREDIT',
                    'ucredit'   :   'UP_CREDIT',
                    'ocredit'   :   'OTH_CREDIT',
                    'dcredit'   :   'DIG_CREDIT',
                    'difok'     :   'DIFF_OK'
                  }



for line in sys_auth:
    if pam_cracklib_text in line:
        if line.startswith('password'):
            matching_lines.append(line)

if len(matching_lines) > 1:
    print "ERROR - Multiple Entries"
    exit()
    
pam_cracklib_rules_entry = matching_lines[0]

cracklib_dummy_class = Cracklib_Dummy_Class()
cracklib_dummy_class.FascistCheck()

# print pam_cracklib_rules_entry
tokens = pam_cracklib_rules_entry.split()
# print tokens

        
for index in range(len(tokens)):
    token = tokens[index]
    if token.find('=') != -1:
        # print token
        key, value = token.split('=')
        # value = token.split('=')[1]
        # print '\t' + key + ' : ' + value

        if key in attributes_dict.keys():
            cracklib_property = attributes_dict.get(key)
            prop = setattr(cracklib_dummy_class, cracklib_property, value)
            # print '\t\t' + str(prop)
            # prop = value
            # print type(prop)
            # print '\t\t' + str(prop)
        

cracklib_dummy_class.FascistCheck()    
    


