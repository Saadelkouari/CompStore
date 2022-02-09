import sys
sys.path.append('C:\Program Files\Saxonica\SaxonHEC1.2.1\Saxon.C.API\python-saxon')
import saxonc
import os
with saxonc.PySaxonProcessor(license=False) as process:
    xqueryproc=process.new_xquery_processor()
    xqueryproc.clear_properties()
    xqueryproc.clear_parameters()
    xmlFile='D:\ComputerStore\invoices\database\invoices.xml'
    xqueryproc.set_property("s",xmlFile)
    print(sys.argv[1])
    xqueryproc.set_property("qs","for $facture in /factures/facture where $facture/@userId="+str(sys.argv[1])+" order by $facture/dateFacturation return $facture")
    result = xqueryproc.run_query_to_string()
with open('D:\ComputerStore\invoices\database\invoicev.xml', 'w') as fp:
    fp.writelines(result.split('\n'))