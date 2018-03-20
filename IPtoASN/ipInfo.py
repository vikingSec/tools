import requests
from bs4 import BeautifulSoup
import geoip2.database
import xlsxwriter

def main(f='testIPlist.txt'):
    Data = open(f)
    ips_full = addInfo(Data)
    toXlsx(ips_full, './ip_list.xlsx')
    
    
    


def addInfo(data):
    fullData = [[]]
    reader_city = geoip2.database.Reader('./City/City.mmdb')
    reader_country = geoip2.database.Reader('./Country/Country.mmdb')
    reader_asn = geoip2.database.Reader('./ASN/ASN.mmdb')
    
    for line in data:
        if len(line) > 0:

            line = line.strip()
            city_response = reader_city.city(line)
            city = city_response.city.name
            country_response = reader_country.country(line)
            country = country_response.country.name
            try:
                asn_response = reader_asn.asn(line)
                asn = str(asn_response.autonomous_system_number)+': '+asn_response.autonomous_system_organization
            except:
                asn = 'UNKNOWN'
            fullData.append([line,country,city,asn])
    return fullData

def toXlsx(data, filename):
    
    row = 0
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    for line in data:
        col = 0
        for item in line:
            worksheet.write(row, col, item)
            col+=1
        row+=1
        
    
                           
main()
