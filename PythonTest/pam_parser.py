from string import whitespace

class Constants:
    
    DIFF_OK     = 101
    DIG_CREDIT  = 102
    LOW_CREDIT  = 103
    MIN_LENGTH  = 104
    OTH_CREDIT  = 105
    UP_CREDIT   = 106
    

#path = 'system-auth'
sys_auth_path = 'system-auth'
sys_auth = open(sys_auth_path, 'r')

pam_cracklib_text = 'pam_cracklib.so'

matching_lines  = []
attributes_dict = {
                    'minlen'    :   'MIN_LENGTH',
                    'lcredit'   :   'LOW_CREDIT',
                    'ucredit'   :   'UP_CREDIT',
                    'ocredit'   :   'OTH_CREDIT',
                    'dcredit'   :   'DIG_CREDIT',
                    'difok'     :   'DIFF_OK'
                  }

#['ASCII_LOWERCASE', 'ASCII_UPPERCASE', 'DIFF_OK', 'DIG_CREDIT', 'FascistCheck', 'LOW_CREDIT', 
#'MIN_LENGTH', 'OTH_CREDIT', 'UP_CREDIT', 'VeryFascistCheck', '__builtins__', '__doc__', 
#'__file__', '__name__', '__package__', '__version__', 'distance', 'distcalculate', 
#'distdifferent', 'palindrome', 'similar', 'simple', 'string', 'test']

for line in sys_auth:
    if pam_cracklib_text in line:
        if line.startswith('password'):
            matching_lines.append(line)

if len(matching_lines) > 1:
    print "ERROR - Multiple Entries"
    exit()
    
pam_cracklib_rules_entry = matching_lines[0]

#print pam_cracklib_rules_entry
tokens = pam_cracklib_rules_entry.split()
print tokens
for index in range(len(tokens)):
    token = tokens[index]
    if token.find('=') != -1:
        print token
        key = token.split('=')[0]
        value = token.split('=')[1]
        print '\t' + key + ' : ' + value
        
        constants = Constants()

        if key in attributes_dict.keys():
            cracklib_property = attributes_dict.get(key)
            prop = getattr(constants, cracklib_property)
            print '\t\t' + str(prop)
            prop = value
            print '\t\t' + str(prop)
            
    


