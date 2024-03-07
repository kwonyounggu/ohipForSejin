#!/usr/bin/python3
import sys

from beans.fileInfoBean import FileInfoBean
from beans.rvhr1Bean import RVHR1Bean
from beans.rvhr2Bean import RVHR2Bean
from beans.rvhr3Bean import RVHR3Bean
from beans.rvhr4Bean import RVHR4Bean
from beans.rvhr5Bean import RVHR5Bean

def writeToCSV(fb, data):
    ##print('======>')
    ##print(data)
    hr1Bean = data['hr1Bean']
    hr2Bean = data['hr2Bean']
    hr3Bean = data['hr3Bean']
    
    print('PAYEE NAME: ', hr1Bean.getPayeeName())
    print('HEALTH CARE PROVIDER: ', hr1Bean.getHealthCareProvider())
    print('GROUP NUMBER: ', hr1Bean.getGroupNumber())
    print('PAYMENT DATE: ')
    print('PAYMENT METHOD: ')
    print('TOTAL AMOUNT: ')
    print('RA SEQUENCE: ')
    print('SPECIALITY: ')
    print('BILLING AGENT: ')

def remittanceReport(fb):
    
    dataDictionary = \
    { \
        'hr1Bean': None, \
        'hr2Bean': None, \
        'hr3Bean': None, \
        'hr4BeanList': [], \
        'hr5BeanList': [], \
        'hr45BeanList': []
    }
    isValid = True
    
    f = open(fb.getPathFile(), 'rt', encoding='utf-8')
    for index, line in enumerate(f, 0):
        #print('type(line): ', type(line))
        if line.startswith('HR1'):
            hr1Bean = RVHR1Bean(line)
            if hr1Bean.getIsValid():
                dataDictionary['hr1Bean'] = hr1Bean
            else:
                print(hr1Bean,'\n', fb.getPathFile())
                isValid = False
                break               
            # print(index, '=>', hr1Bean)
        elif line.startswith('HR2'):
            hr2Bean = RVHR2Bean(line)
            if hr2Bean.getIsValid():
                dataDictionary['hr2Bean'] = hr2Bean
            else:
                print(hr2Bean,'\n', fb.getPathFile())
                isValid = False
                break 
            # print(index, '=>', hr2Bean)
        elif line.startswith('HR3'):
            hr3Bean = RVHR3Bean(line)
            if hr3Bean.getIsValid():
                dataDictionary['hr3Bean'] = hr3Bean
            else:
                print(hr3Bean,'\n', fb.getPathFile())
                isValid = False
                break 
            # print(index, '=>', hr3Bean)
        elif line.startswith('HR4'): #multiple times
            hr4Bean = RVHR4Bean(line)
            if hr4Bean.getIsValid():
                dataDictionary['hr4BeanList'].append(hr4Bean)
            else:
                print(hr4Bean,'\n', fb.getPathFile())
                isValid = False
                break 
            # print(index, '=>', hr4Bean)
        elif line.startswith('HR5'):
            hr5Bean = RVHR5Bean(line)
            if hr5Bean.getIsValid():
                dataDictionary['hr5BeanList'].append(hr5Bean)
                hr4Bean = dataDictionary['hr4BeanList'][-1]
                if hr4Bean.getClaimNumber() == hr5Bean.getClaimNumber():
                    hr45Bean = {}
                    hr45Bean['accountingNumber'] = hr4Bean.getAccountingNumber()
                    hr45Bean['claimNumber'] = hr4Bean.getClaimNumber()
                    hr45Bean['transactionType'] = hr4Bean.getTransactionType()
                    hr45Bean['healthcareProvider'] = hr4Bean.getHealthcareProvider()
                    hr45Bean['speciality'] = hr4Bean.getSpeciality()
                    hr45Bean['provinceCode'] = hr4Bean.getProvinceCode()
                    hr45Bean['healthRegistrationNumber'] = hr4Bean.getHealthRegistrationNumber()
                    hr45Bean['versionCode'] = hr4Bean.getVersionCode()
                    hr45Bean['paymentProgram'] = hr4Bean.getPaymentProgram()
                    
                    hr45Bean['serviceDate'] = hr5Bean.getServiceCode()
                    hr45Bean['numberOfServices'] = hr5Bean.getNumberOfServices()
                    hr45Bean['serviceCode'] = hr5Bean.getServiceCode()
                    hr45Bean['amountSubmitted'] = hr5Bean.getAmountSubmitted()
                    hr45Bean['amountPaid'] = hr5Bean.getAmountPaid()
                    hr45Bean['explanatoryCode'] = hr5Bean.getExpanatoryCode()
                    
                    dataDictionary['hr45BeanList'].append(hr45Bean)
                else:
                    print('Error: claim number between HR4 and HR5 is different in the record index = ', index)
                    print(hr5Bean,'\n', fb.getPathFile())
                    isValid = False
                    break 
            else:
                print(hr5Bean,'\n', fb.getPathFile())
                isValid = False
                break 
            # print(index, '=>', hr5Bean)
    f.close()
    
    if isValid: return dataDictionary
    return None
    
def main():

    args = sys.argv[1:]

    if not args:
        print('usage: >mroConversion.py file [file ...]')
        sys.exit(1)
    
    for fileName in args :
        fb = FileInfoBean(fileName)
        
        if fb.isValid(): 
            
            match fb.getType():
                case 'B': print('Batch Edit')
                case 'E': print('Claim Error')
                case 'F': print('Claim Error')
                case 'P': 
                    print('Report')
                    data = remittanceReport(fb) 
                    if data is not None: writeToCSV(fb, data)  
                    else: print('None is returned ...')    
                case '_': print('Unknown report type ...')
            print(fb)
            print('----------------------------------')   
        else: print(fb)

if __name__ == '__main__':
    main()
