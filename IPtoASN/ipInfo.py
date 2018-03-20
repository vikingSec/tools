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
            fullData.append([line,getCountry(line),getCity(line),getASN(line)])
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
        
def getASN(ip):
    reader_asn = geoip2.database.Reader('./ASN/ASN.mmdb')
    try:
        asn_response = reader_asn.asn(ip.strip())
        asn = str(asn_response.autonomous_system_number)+': '+asn_response.autonomous_system_organization
    except:
        asn = 'UNKNOWN'
    return asn
    
    
def getCity(ip):
    reader_city = geoip2.database.Reader('./City/City.mmdb')
    city_response = reader_city.city(ip.strip())
    city = city_response.city.name

    return city
def getCountry(ip):
    reader_country = geoip2.database.Reader('./Country/Country.mmdb')
    country_response = reader_country.country(ip.strip())
    country = country_response.country.name

    return country
                           
main()
