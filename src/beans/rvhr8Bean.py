# do accordingly tomorrow
## This line displays Message Facility Record for Health Reconciliation
## The record starts with 'HR7'
class RVHR8Bean:
    _isValid = True
    #_invalidMessage = ''
    def __init__(self, line):
        ## print('len(line): ', len(line))
        if len(line) != 80: ## in java the length is not 80 but 79
            self._isValid = False
            self._invalidMessage = 'Error: the HR8 record line of this file does not contain specified number of characters (ie:80).'
        else:
            self._transactionIdentifier = line[0:2]
            self._recordType = line[2:2+1]                      
            self._messageText = line[3:3+70].strip()
            self._reservedForMOH = line[73:73+6].strip()
                        
    def getIsValid(self):
        return self._isValid
    
    def getInvalidMessage(self):
        return self._invalidMessage
    
    def getTransactionIdentifier(self):
        return self._transactionIdentifier
    
    def getRecordType(self):
        return self._recordType
    
    def getMessageText(self):
        return self._messageText
    
    def getReservedForMOH(self):
        return self._reservedForMOH
    
    def __str__(self):
        toString = ''
        if self._isValid:
            toString = 'TransactionIdentifier: ' + self._transactionIdentifier+ '\n' + \
                       'Record Type: ' + self._recordType + '\n' + \
                       'Message Text: ' + self._messageText + '\n' + \
                       'Reserved for MOH: ' + self._reservedForMOH + '\n'
        else:
            toString = 'Invalid because parsing is failed\n' + \
                       'Invalid Message: ' + self._invalidMessage
                       
        return toString