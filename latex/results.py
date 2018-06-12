import re
import os

def update_result(results_file, key_value, trailing_xspace=True, format_="{}"):
    #if the file doesn't exist, touch it.
    if not(os.path.isfile(results_file)):
        with open(results_file,'w') as F:
            pass

    #if we want the trailing xspace, add it in here.
    if trailing_xspace:
        ending='\\xspace}'
    else:
        ending='}'

    #read the file
    with open(results_file, 'r') as F:
        s_ = F.read()
    s_new = s_

    #for each key in the dictionary
    for key in key_value:
        #build a regex
        pattern = re.compile(r'\\newcommand\{\\' + str(key) + '\}\{.*(?:\})')
        #decide on the new text
        line_text = '\\\\newcommand{\\\\' + str(key) + '}{' + format_.format(key_value[key]) + ending
        if pattern.search(s_new) is not None:
            #if the key is already in the file, substitute its old value with the new one
            s_new = pattern.sub(line_text, s_new)
        else:
            #otherwise append the new newcommand line to the file
            line_text = '\\newcommand{\\' + str(key) + '}{' + format_.format(key_value[key]) + ending
            s_new = s_new  + line_text + '\n'

    #save the resulting file
    with open(results_file,'w') as F:
        F.write(s_new)


