import math

# Ceaser Cipher Encryption
class CeaserCipher(object):

    def __init__(self, message) -> None:

        SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?,.-_;:/()'"
        
        self.SYMBOLS = SYMBOLS
        self.message = message

    def encrypt_message(self, key):

        translated = ''

        # loop through each character in message

        for symbol in self.message:
    
            if symbol in self.SYMBOLS:
                
                # Get the encrypted (or decrypted) number for this symbol.
                
                num = self.SYMBOLS.find(symbol) # Get the number of the symbol.
            
                num = num + int(key)

                # Handle the wrap-around if num is larger than the length of SYMBOLS or less than 0:
                    
                if num >= len(self.SYMBOLS):
                    
                    num = num - len(self.SYMBOLS)
                    
                elif num < 0:
                    
                    num = num + len(self.SYMBOLS)

                # Add encrypted/decrypted number's symbol to translated:
                
                translated = translated + self.SYMBOLS[num]
            
            else:

                # Just add the symbol without encrypting/decrypting:

                translated = translated + symbol

        return translated

    def decrypt_message(self, key):

        translated = ''

        # loop through each character in message

        for symbol in self.message:
    
            if symbol in self.SYMBOLS:
                
                # Get the encrypted (or decrypted) number for this symbol.
                
                num = self.SYMBOLS.find(symbol) # Get the number of the symbol.
            
                num = num - int(key)

                # Handle the wrap-around if num is larger than the length of SYMBOLS or less than 0:
                    
                if num >= len(self.SYMBOLS):
                    
                    num = num - len(self.SYMBOLS)
                    
                elif num < 0:
                    
                    num = num + len(self.SYMBOLS)

                # Add encrypted/decrypted number's symbol to translated:
                
                translated = translated + self.SYMBOLS[num]
            
            else:

                # Just add the symbol without encrypting/decrypting:

                translated = translated + symbol

        return translated

# Transposition Cipher Encryption

# Specifically columnar transposition cipher.
class TranspositionCipher(object):

    def __init__(self, message) -> None:
        
        self.message = message

    def encrypt_message(self, key):

        key = int(key)

        # Each string in ciphertext represents a column in the grid:

        ciphertext = [''] * key

        # Loop through each column in ciphertext:

        for column in range(key):
    
            currentIndex = column

            # Keep looping until currentIndex goes past the message length:

            while currentIndex < len(self.message):
                
                # Place the character at currentIndex in message at the

                # end of the current column in the ciphertext list:

                ciphertext[column] += self.message[currentIndex]

                # Move currentIndex over:

                currentIndex += key

        # Convert the ciphertext list into a single string value and return it:

        ciphertext = ''.join(ciphertext)

        return ciphertext

    def decrypt_message(self, key):

        # The number of "columns" in our transposition grid:

        numOfColumns = int(math.ceil(len(self.message) / float(key)))

        # The number of "rows" in our grid:

        numOfRows = int(key)

        # The number of "shaded boxes" in the last "column" of the grid:

        numOfShadedBoxes = (numOfColumns * numOfRows) - int(len(self.message))

        # Each string in plaintext represents a column in the grid:

        plaintext = [''] * numOfColumns

        # The column and row variables point to where in the grid the next

        # character in the encrypted message will go:

        column = 0

        row = 0

        for symbol in self.message:
            
            plaintext[column] += symbol

            column += 1 # Point to the next column.

            # If there are no more columns OR we're at a shaded box, go back

            # to the first column and the next row:

            if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):

                column = 0

                row += 1

        plaintext = ''.join(plaintext)

        return plaintext