import os
import re

MRO_MAX_FILE_SIZE = 1000000
EXPECTED_FILE_NAME = r'(^[BEFPX]{1})+([ABCDEFGHIJKL]{1})+([0-9]{4,6})+.(\d{3})$'

class FileInfoBean:
    _type = 'A'
    _month = 'Z'
    _number = '0000'
    _extension = '000'
    _isValid = False
    
    def __init__(self, pathFile):
        self._pathFile = pathFile
        self._fileName = os.path.basename(pathFile)
        
        match = re.search(EXPECTED_FILE_NAME, self._fileName)
        
        if match:
            self._type = match.group(1)
            self._month = match.group(2)
            self._number = match.group(3)
            self._extension = match.group(4)
            self._isValid = True
            
    # report type
    def getType(self):
        return self._type
    
    def getMonth(self):
        return self._month
    
    def getNumber(self):
        return self._number
    
    def getExtension(self):
        return self._extension
    
    def getFileName(self):
        return self._fileName
    
    def getPathFile(self):
        return self._pathFile
    
    def isValid(self):
        return self._isValid
    
    def __str__(self):
        
        toString = ''
        if self._isValid:
            toString = 'Report Type: ' + self._type + '\n' + \
                       'Report Month: ' + self._month + '\n' + \
                       'Group/Provider Number: ' + self._number + '\n' + \
                       'File Extension: ' + self._extension + '\n' + \
                       'File Name Validity: ' + str(self._isValid) + '\n' + \
                       'File Name: ' + self._fileName + '\n'
        else:
            toString = 'File Name Validity: ' + str(self._isValid) + '\n' + \
                       'File Name: ' + self._fileName + '\n'
                       
        return toString
            