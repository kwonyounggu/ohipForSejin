class RVHR1Bean:
    _isValid = True
    #_invalidMessage = ''
    def __init__(self, line):
        ## print('len(line): ', len(line))
        if len(line) != 80: ## in java the length is not 80 but 79
            self._isValid = False
            self._invalidMessage = 'Error: this file does not contain HR1V030 in the first record_1.'
        elif line.index('HR1V030') != 0:
            self._isValid = False
            self._invalidMessage = 'Error: this file does not contain HR1V030 in the first record_2.'
        else:
            self._groupNumber = line[7:7+4]
            self._healthCareProvider = line[11:11+6]
            self._speciality = line[17:17+2]
            self._mohOfficeCode = line[19:20]
            self._remittanceAdviceSequence = line[20:21]
            self._paymentDate = line[21:21+4] + '/' + line[25:25+2] + '/' + line[27:27+2]
            self._payeeName = line[29:29+30]
            self._totalAmountPayable = float(line[59:59+9])/100
            self._totalAmountPayableSign = line[68:69]
            self._chequeNumber = line[69:69+8].strip()
            self._reservedForMOH2 = line[77:77+2]
            
        
    
    def getIsValid(self):
        return self._isValid
    
    def getInvalidMessage(self):
        return self._invalidMessage
    
    def getGroupNumber(self):
        return self._groupNumber
    
    def getHealthCareProvider(self):
        return self._healthCareProvider
    
    def getSpeciality(self):
        return self._speciality
    
    def getMohOfficeCode(self):
        return self._mohOfficeCode
    
    def getRemittanceAdviceSequence(self):
        return self._remittanceAdviceSequence
    
    def getPaymentDate(self):
        return self._paymentDate
    
    def getPayeeName(self):
        return self._payeeName
    
    def getTotalAmountPayable(self):
        return self._totalAmountPayable
    
    def getTotalAmountPayableSign(self):
        return self._totalAmountPayableSign
    
    def getChequeNumber(self):
        return self._chequeNumber
    
    def getReservedForMOH2(self):
        return self._reservedForMOH2
    
    def __str__(self):
        toString = ''
        if self._isValid:
            toString = 'Group Number: ' + self._groupNumber + '\n' + \
                       'Health Care Provider: ' + self._healthCareProvider + '\n' + \
                       'Speciality: ' + self._speciality + '\n' + \
                       'Moh Office Code: ' + self._mohOfficeCode + '\n' + \
                       'Remittance Advice Sequence: ' + self._remittanceAdviceSequence + '\n' + \
                       'Payment Date: ' + self._paymentDate + '\n' + \
                       'Payee Name: ' + self._payeeName + '\n' + \
                       'Total Amount Payable: ' + str(self._totalAmountPayable) + '\n' + \
                       'Total Amount Payable Sign: ' + self._totalAmountPayableSign + '\n' + \
                       'Cheque Number: ' + self._chequeNumber + '\n' + \
                       'Reserved for MOH2: ' + self._reservedForMOH2
                       
        else:
            toString = 'Invalid because parsing is failed\n' + \
                       'Invalid Message: ' + self._invalidMessage
                       
        return toString