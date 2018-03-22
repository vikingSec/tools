<h3>IP to ASN Library </h3>

Library for converting IP addresses to their respective ASN/Org/location information. Includes functionality for reading from a text file and exporting to a .xlsx file.<br><br>

(BTW credit goes to the MaxMind database for City, Country, and ASN DBs included here. Find them at https://www.maxmind.com/en/)<br><br>


<h3>IP to ASN Maltego Transform</h3>
<b>Requirements:</b><br><br>

<a href="https://docs.paterva.com/en/developer-portal/transform_libraries/">[Maltego Transforms Library]</a> - This is the Maltego Transforms Library. Place it in the same folder as the IPtoASN.py file, and when you import it into Maltego, be sure to use this directory as the working directory<br><br>
<a href="https://github.com/vikingSec/tools/blob/master/IPtoASN/IPtoASN.py">[IPtoASN Library]</a> - Seems obvious but this will be necessary as well. Same as above, place it in the same directory as the iptoasn_maltego.py file and the DBs folder.<br><br>


<h3>VirusTotal Library</h3>
Super simple Library that interacts with the <a href="https://www.virustotal.com/en/documentation/public-api/"> VirusTotal API </a>. Functionality will be updated as I find more use for it.<br><br>

<h3>VirusTotal Maltego Transform</h3>
At the time of writing, this transform takes an input as an IP and lists known-malicious domains registered to that IP, using the VirusTotal library. This is a standalone transform at the moment, but I'll definitely be writing more in the future.
