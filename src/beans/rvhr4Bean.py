class RVHR4Bean:
    _isValid = True
    #_invalidMessage = ''
    def __init__(self, line):
        ## print('len(line): ', len(line))
        if len(line) != 80: ## in java the length is not 80 but 79
            self._isValid = False
            self._invalidMessage = 'Error: the HR4 record line of this file does not contain specified number of characters (ie:80).'
        else:
            self._transactionIdentifier = line[0:2]
            self._recordType = line[2:2+1]
            self._claimNumber = line[3:3+11]
            self._transactionType = line[14:15]
            self._healthcareProvider = line[15:15+6]
            self._speciality = line[21:21+2]
            self._accountingNumber = line[23:23+8]
            self._patientLastName = line[31:31+14].strip()
            self._patientFirstName = line[45:45+5].strip()
            self._provinceCode = line[50:50+2]
            self._healthRegistrationNumber = line[52:52+12].strip()
            self._versionCode = line[64:64+2].strip()
            self._paymentProgram = line[66:66+3]
            self._serviceLocator = line[69:69+4].strip()
            self._mohGroupIdentifier = line[73:73+4]            
            self._reservedForMOH = line[77:77+2].strip()
            
    def getIsValid(self):
        return self._isValid
    
    def getInvalidMessage(self):
        return self._invalidMessage
    
    def getTransactionIdentifier(self):
        return self._transactionIdentifier
    
    def getrecordType(self):
        return self._recordType
    
    def getAddressLine2(self):
        return self._addressLine2
    
    def getAddressLine3(self):
        return self._addressLine3
    
    def getreservedForMOH(self):
        return self._reservedForMOH
    
    def __str__(self):
        toString = ''
        if self._isValid:
            toString = 'TransactionIdentifier: ' + self._transactionIdentifier+ '\n' + \
                       'Record Type: ' + self._recordType + '\n' + \
                       'Claim Number: ' + self._claimNumber + '\n' + \
                       'Transaction Type: ' + self._transactionType + '\n' +  \
                       'Health Care Provider: ' + self._healthcareProvider+ '\n' + \
                       'Speciality: ' + self._speciality + '\n' + \
                       'Accounting Number: ' + self._accountingNumber + '\n' + \
                       'Patient Last Name: ' + self._patientLastName + '\n' +  \
                       'Patient First Name: ' + self._patientFirstName+ '\n' + \
                       'Province Code: ' + self._provinceCode + '\n' + \
                       'Health Registration Number: ' + self._healthRegistrationNumber + '\n' + \
                       'Version Code: ' + self._versionCode + '\n' +  \
                       'Payment Program: ' + self._paymentProgram + '\n' + \
                       'Service Locator: ' + self._serviceLocator + '\n' + \
                       'MOH Group Identifier: ' + self._mohGroupIdentifier + '\n' +  \
                       'Reserved for MOH: ' + self._reservedForMOH
        else:
            toString = 'Invalid because parsing is failed\n' + \
                       'Invalid Message: ' + self._invalidMessage
                       
        return toString