<html>
<h1>IP to ASN QuickScript </h1>

Quick script I wrote to take a text list of IPs and export them to an EXCEL file with ASN and location data. May be useful for threat hunting stuff. Included a test file with 5 ips that were said to be malicious online.<br><br>

(BTW credit goes to the MaxMind database for City, Country, and ASN DBs included here. Find them at https://www.maxmind.com/en/)<br><br>

<b>[UPDATE (3.20.18)]</b> IP to ASN Library<br><br>
<b>Functions:</b><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;<b>getASN(String ip):</b> IP address (String) -> ASN : Org<br><br>

&nbsp;&nbsp;&nbsp;&nbsp;<b>getCity(String ip) :</b> IP address (String) -> City<br><br>

&nbsp;&nbsp;&nbsp;&nbsp;<b>getCountry(String ip):</b> IP address (String) -> Country<br><br>

&nbsp;&nbsp;&nbsp;&nbsp;<b>addInfo(String[[]):</b> IP addresses (String []) -> IP addresses with Country, city, and ASN:Org data (String [[]])<br><br>

&nbsp;&nbsp;&nbsp;&nbsp;<b>toXlsx(String [[]] data, String filename):</b> IP address+country+city
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ASN:Org structure (String [[]]) ,filename (String)-> .xlsx file<br><br><br>

<h1>IP to ASN Maltego Transform</h1>
<b>Requirements:</b><br><br>

<a href="https://docs.paterva.com/en/developer-portal/transform_libraries/">[Maltego Transforms Library]</a> - This is the Maltego Transforms Library. Place it in the same folder as the IPtoASN.py file, and when you import it into Maltego, be sure to use this directory as the working directory<br><br>
<a href="https://github.com/vikingSec/tools/blob/master/IPtoASN/IPtoASN.py">[IPtoASN Library]</a> - Seems obvious but this will be necessary as well. Same as above, place it in the same directory as the iptoasn_maltego.py file and the DBs folder.<br><br>

</html>
