class RVHR2Bean:
    _isValid = True
    #_invalidMessage = ''
    def __init__(self, line):
        ## print('len(line): ', len(line))
        if len(line) != 80: ## in java the length is not 80 but 79
            self._isValid = False
            self._invalidMessage = 'Error: the 2nd line of this file does not contain specified number of characters (ie:80).'
        else:
            self._transactionIdentifier = line[0:2]
            self._recordType = line[2:2+1]
            self._billingAgent = line[3:3+30]
            self._billingAgentAddress = line[33:33+25]
            self._reservedForMOH = line[58:58+21]
            
    def getIsValid(self):
        return self._isValid
    
    def getInvalidMessage(self):
        return self._invalidMessage
    
    def getTransactionIdentifier(self):
        return self._transactionIdentifier
    
    def getrecordType(self):
        return self._recordType
    
    def getbillingAgent(self):
        return self._billingAgent
    
    def getBillingAgentAddress(self):
        return self._billingAgentAddress
    
    def getreservedForMOH(self):
        return self._reservedForMOH
    
    def __str__(self):
        toString = ''
        if self._isValid:
            toString = 'TransactionIdentifier: ' + self._transactionIdentifier+ '\n' + \
                       'Record Type: ' + self._recordType + '\n' + \
                       'Billing Agent: ' + self._billingAgent + '\n' + \
                       'Billing Agent Address: ' + self._billingAgentAddress + '\n' +  \
                       'Reserved for MOH: ' + self._reservedForMOH
        else:
            toString = 'Invalid because parsing is failed\n' + \
                       'Invalid Message: ' + self._invalidMessage
                       
        return toString