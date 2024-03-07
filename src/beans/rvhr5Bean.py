# do accordingly tomorrow
class RVHR5Bean:
    _isValid = True
    #_invalidMessage = ''
    def __init__(self, line):
        ## print('len(line): ', len(line))
        if len(line) != 80: ## in java the length is not 80 but 79
            self._isValid = False
            self._invalidMessage = 'Error: the HR5 record line of this file does not contain specified number of characters (ie:80)_1.'
        elif line.index('HR5') != 0:
            self._isValid = False
            self._invalidMessage = 'Error: the HR5 record line of this file does not contain HR5 in it_2.'
        else:
            self._transactionIdentifier = line[0:2]
            self._recordType = line[2:2+1]
            self._claimNumber = line[3:3+11]
            self._transactionType = line[14:15]
            self._serviceDate = line[15:15+4] + '/' + line[19:19+2] + '/' + line[21:21+2]
            self._numberOfServices = line[23:23+2]
            self._serviceCode = line[25:25+5]
            self._reservedForMOH1 = line[30:31]
            self._amountSubmitted = float(line[31:31+6])/100
            self._amountPaid = float(line[37:37+6])/100
            self._amountPaidSign = line[43:44]
            self._explanatoryCode = line[44:44+2].strip()
            self._reservedForMOH2 = line[46:46+33].strip()
                        
    def getIsValid(self):
        return self._isValid
    
    def getInvalidMessage(self):
        return self._invalidMessage
    
    def getTransactionIdentifier(self):
        return self._transactionIdentifier
    
    def getRecordType(self):
        return self._recordType
    
    def getClaimNumber(self):
        return self._claimNumber
    
    def getTransactionType(self):
        return self._transactionType
    
    def getServiceDate(self):
        return self._serviceDate
    
    def getNumberOfServices(self):
        return self._numberOfServices
    
    def getServiceCode(self):
        return self._serviceCode
    
    def getReservedForMOH1(self):
        return self._reservedForMOH1

    def getAmountSubmitted(self):
        return self._amountSubmitted    
    
    def getAmountPaid(self):
        return self._amountPaid
    
    def getAmountPaidSign(self):
        return self._amountPaidSign

    def getExpanatoryCode(self):
        return self._explanatoryCode
    
    def getReservedForMOH2(self):
        return self._reservedForMOH2
    
    def __str__(self):
        toString = ''
        if self._isValid:
            toString = 'TransactionIdentifier: ' + self._transactionIdentifier+ '\n' + \
                       'Record Type: ' + self._recordType + '\n' + \
                       'Claim Number: ' + self._claimNumber + '\n' + \
                       'Transaction Type: ' + self._transactionType + '\n' +  \
                       'Service Date: ' + self._serviceDate+ '\n' + \
                       'Number Of Services: ' + self._numberOfServices + '\n' + \
                       'Service Code: ' + self._serviceCode + '\n' + \
                       'Reserved for MOH1: ' + self._reservedForMOH1 + '\n' +  \
                       'Amount Submitted: ' + str(self._amountSubmitted)+ '\n' + \
                       'Amount Paid: ' + str(self._amountPaid) + '\n' + \
                       'Amount Paid Sign: ' + self._amountPaidSign + '\n' + \
                       'Explanatory Code: ' + self._explanatoryCode + '\n' +  \
                       'Reserved for MOH2: ' + self._reservedForMOH2 + '\n'
        else:
            toString = 'Invalid because parsing is failed\n' + \
                       'Invalid Message: ' + self._invalidMessage
                       
        return toString