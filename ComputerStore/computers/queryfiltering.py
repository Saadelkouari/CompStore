import sys
sys.path.append('C:\Program Files\Saxonica\SaxonHEC1.2.1\Saxon.C.API\python-saxon')
import saxonc
import os
with saxonc.PySaxonProcessor(license=False) as process:
    xqueryproc=process.new_xquery_processor()
    xqueryproc.clear_properties()
    xqueryproc.clear_parameters()
    xmlFile='D:\ComputerStore\computers\database\computers.xml'
    xqueryproc.set_property("s",xmlFile)
    if sys.argv[3].isnumeric():
        if sys.argv[2]=="gt":
            sys.argv[2]='>'
        if sys.argv[2]=="ls":
            sys.argv[2]='<'
        xqueryproc.set_property("qs","/computers/computer["+sys.argv[1]+sys.argv[2]+sys.argv[3]+"]")
    else:
        xqueryproc.set_property("qs","/computers/computer["+sys.argv[1]+sys.argv[2]+"\'"+sys.argv[3]+"\']")
    result = xqueryproc.run_query_to_string()
with open('D:\ComputerStore\computers\query.xml', 'w') as fp:
    fp.writelines(result.split('\n'))