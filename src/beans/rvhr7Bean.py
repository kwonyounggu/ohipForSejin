# do accordingly tomorrow
## This line displays the Accounting Tx Record for Health Reconciliation
## The record starts with 'HR7'
class RVHR7Bean:
    _isValid = True
    #_invalidMessage = ''
    def __init__(self, line):
        ## print('len(line): ', len(line))
        if len(line) != 80: ## in java the length is not 80 but 79
            self._isValid = False
            self._invalidMessage = 'Error: the HR7 record line of this file does not contain specified number of characters (ie:80).'
        else:
            self._transactionIdentifier = line[0:2]
            self._recordType = line[2:2+1]                      
            self._transactionCode = line[3:3+2]
            self._chequeIndicator = line[5:5+1]
            self._transactionDate = line[6:6+4] + '/' + line[10:10+2] + '/' + line[12:12+2]
            self._transactionAmount = float(line[14:14+8])/100
            self._transactionAmountSign = line[22:23]
            self._transactionMessage = line[23:23+50].strip()
            self._reservedForMOH = line[73:73+6].strip()
                        
    def getIsValid(self):
        return self._isValid
    
    def getInvalidMessage(self):
        return self._invalidMessage
    
    def getTransactionIdentifier(self):
        return self._transactionIdentifier
    
    def getRecordType(self):
        return self._recordType
    
    def getTransactionCode(self):
        return self._transactionCode
    
    def getChequeIndicator(self):
        return self._chequeIndicator
    
    def getTransactionDate(self):
        return self._transactionDate
    
    def getTransactionAmount(self):
        return self._transactionAmount
    
    def getTransactionAmountSign(self):
        return self._transactionAmountSign
    
    def getTransactionMessage(self):
        return self._transactionMessage
    
    def getReservedForMOH(self):
        return self._reservedForMOH
    
    def __str__(self):
        toString = ''
        if self._isValid:
            toString = 'TransactionIdentifier: ' + self._transactionIdentifier+ '\n' + \
                       'Record Type: ' + self._recordType + '\n' + \
                       'Transaction Code: ' + self._transactionCode + '\n' + \
                       'Cheque Indicator: ' + self._chequeIndicator + '\n' +  \
                       'Transaction Date: ' + self._transactionDate+ '\n' + \
                       'Transaction Amount: ' + self._transactionAmount + '\n' + \
                       'Transaction Amount Sign: ' + self._transactionAmountSign + '\n' + \
                       'Transaction Message: ' + self._transactionMessage + '\n' +  \
                       'Reserved for MOH: ' + self._reservedForMOH + '\n'
        else:
            toString = 'Invalid because parsing is failed\n' + \
                       'Invalid Message: ' + self._invalidMessage
                       
        return toString