class RVHR3Bean:
    _isValid = True
    #_invalidMessage = ''
    def __init__(self, line):
        ## print('len(line): ', len(line))
        if len(line) != 80: ## in java the length is not 80 but 79
            self._isValid = False
            self._invalidMessage = 'Error: the 3rd line of this file does not contain specified number of characters (ie:80).'
        else:
            self._transactionIdentifier = line[0:2]
            self._recordType = line[2:2+1]
            self._addressLine2 = line[3:3+25]
            self._addressLine3 = line[28:28+25]
            self._reservedForMOH = line[53:53+26]
            
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
                       'Address Line2: ' + self._addressLine2 + '\n' + \
                       'Address Line3: ' + self._addressLine3 + '\n' +  \
                       'Reserved for MOH: ' + self._reservedForMOH
        else:
            toString = 'Invalid because parsing is failed\n' + \
                       'Invalid Message: ' + self._invalidMessage
                       
        return toString