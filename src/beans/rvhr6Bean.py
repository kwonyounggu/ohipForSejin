# do accordingly tomorrow
class RVHR6Bean:
    _isValid = True
    #_invalidMessage = ''
    def __init__(self, line):
        ## print('len(line): ', len(line))
        if len(line) != 80: ## in java the length is not 80 but 79
            self._isValid = False
            self._invalidMessage = 'Error: the HR6 record line of this file does not contain specified number of characters (ie:80).'
        else:
            self._transactionIdentifier = line[0:2]
            self._recordType = line[2:2+1]           
            self._amtBrtFwdClaimsAdjustment = float(line[3:3+9])/100
            self._amtBrtFwdClaimsAdjustmentSign = line[12:12+1]
            self._amtBrtFwdClaimsAdvances = float(line[13:13+9])/100
            self._amtBrtFwdClaimsAdvancesSign = line[22:22+1]
            self._amtBrtFwdReductions = float(line[23:23+9])/100
            self._amtBrtFwdReductionsSign = line[32:32+1]
            self._amtBrtFwdOtherDeductions = float(line[33:33+9])/100
            self._amtBrtFwdOtherDeductionsSign = line[42:42+1]
            self._reservedForMOH = line[43:43+36].strip()
                        
    def getIsValid(self):
        return self._isValid
    
    def getInvalidMessage(self):
        return self._invalidMessage
    
    def getTransactionIdentifier(self):
        return self._transactionIdentifier
    
    def getRecordType(self):
        return self._recordType
    
    def getAmtBrtFwdClaimsAdjustment(self):
        return self._amtBrtFwdClaimsAdjustment
    
    def getAmtBrtFwdClaimsAdjustmentSign(self):
        return self._amtBrtFwdClaimsAdjustmentSign
    
    def getAmtBrtFwdClaimsAdvances(self):
        return self._amtBrtFwdClaimsAdvances
    
    def getAmtBrtFwdClaimsAdvancesSign(self):
        return self._amtBrtFwdClaimsAdvancesSign
    
    def getAmtBrtFwdReductions(self):
        return self._amtBrtFwdReductions
    
    def getAmtBrtFwdReductionsSign(self):
        return self._amtBrtFwdReductionsSign

    def getAmtBrtFwdOtherDeductions(self):
        return self._amtBrtFwdOtherDeductions    
    
    def getAmtBrtFwdOtherDeductionsSign(self):
        return self._amtBrtFwdOtherDeductionsSign
    
    def getReservedForMOH(self):
        return self._reservedForMOH
    
    def __str__(self):
        toString = ''
        if self._isValid:
            toString = 'TransactionIdentifier: ' + self._transactionIdentifier+ '\n' + \
                       'Record Type: ' + self._recordType + '\n' + \
                       'Amt Brt Fwd Claims Adjustment: ' + self._amtBrtFwdClaimsAdjustment + '\n' + \
                       'Amt Brt Fwd Claims Adjustment Sign: ' + self._amtBrtFwdClaimsAdjustmentSign + '\n' +  \
                       'Amt Brt Fwd Claims Advances: ' + self._amtBrtFwdClaimsAdvances+ '\n' + \
                       'Amt Brt Fwd Claims Advances Sign: ' + self._amtBrtFwdClaimsAdvancesSign + '\n' + \
                       'Amt Brt Fwd Reductions: ' + self._amtBrtFwdReductions + '\n' + \
                       'Amt Brt Fwd Reductions Sign: ' + self._amtBrtFwdReductionsSign + '\n' +  \
                       'Amt Brt Fwd Other Reductions: ' + str(self._amtBrtFwdOtherDeductions)+ '\n' + \
                       'Amt Brt Fwd Other Reductions Sign: ' + str(self._amtBrtFwdOtherDeductionsSign) + '\n' + \
                       'Reserved for MOH: ' + self._reservedForMOH + '\n'
        else:
            toString = 'Invalid because parsing is failed\n' + \
                       'Invalid Message: ' + self._invalidMessage
                       
        return toString