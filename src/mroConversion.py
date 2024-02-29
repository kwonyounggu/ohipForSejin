#!/usr/bin/python3
import sys

from beans.fileInfoBean import FileInfoBean
from beans.rvhr1Bean import RVHR1Bean
from beans.rvhr2Bean import RVHR2Bean
from beans.rvhr3Bean import RVHR3Bean
from beans.rvhr4Bean import RVHR4Bean

def remittanceReport(fb):
    f = open(fb.getPathFile(), 'rt', encoding='utf-8')
    for index, line in enumerate(f, 0):
        #print('type(line): ', type(line))
        if line.startswith('HR1'):
            hr1Bean = RVHR1Bean(line)
            print(index, '=>', hr1Bean)
        elif line.startswith('HR2'):
            hr2Bean = RVHR2Bean(line)
            print(index, '=>', hr2Bean)
        elif line.startswith('HR3'):
            hr3Bean = RVHR3Bean(line)
            print(index, '=>', hr3Bean)
        elif line.startswith('HR4'): #multiple times
            hr4Bean = RVHR4Bean(line)
            print(index, '=>', hr4Bean)
        elif line.startswith('HR5'):
            pass
    f.close()
    
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
                    remittanceReport(fb)       
                case '_': print('Unknown report type ...')
            print(fb)
            print('----------------------------------')   
        else: print(fb)

if __name__ == '__main__':
    main()
