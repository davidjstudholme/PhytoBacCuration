import sys
import re
#from datetime import datetime as dt

### Read the NCBI taxIDs
with open('names.dmp') as fh:
    lines = fh.readlines()
    lines = [line.rstrip() for line in lines]
fh.close()

### Make a dictionary of names to taxIDs
name_to_taxid = {}
for readline in lines:
    values = readline.split('|')
    tax_id = values[0]
    name_txt = values[1].strip()
    unique_name = values[2].strip()
    #sys.stderr.write(tax_id)
    #sys.stderr.write(name_txt)
    name_to_taxid[name_txt] = tax_id
    
### Read the list of taxon names that are within scope
with open('taxa_in_scope.txt') as fh:
    lines = fh.readlines()
    lines = [line.rstrip() for line in lines]
fh.close()
    
for readline in lines:
    name = readline.strip()
    name = re.sub('\s+',' ',name)
    sys.stderr.write('\n')
    sys.stderr.write('"')
    sys.stderr.write(name)
    sys.stderr.write('"')
    tax_id = ""
    if name in name_to_taxid:
        sys.stderr.write(' IS in list\n')
        print(name, '\t', name_to_taxid[name])
    else: 
        sys.stderr.write(' is NOT in list\n')            
        print(name, '\t', ' ')
        