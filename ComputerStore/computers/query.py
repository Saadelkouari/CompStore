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
    xqueryproc.set_property("qs","for $computer in /computers/computer where $computer/@id="+str(sys.argv[1])+" return $computer")
    result = xqueryproc.run_query_to_string()
with open('D:\ComputerStore\computers\query.xml', 'w') as fp:
    fp.writelines(result.split('\n'))