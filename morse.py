import winsound
import time

class MorseCode:
    def __init__(self):
        print("")
        
    def dot(self):
        winsound.Beep(440,200)
    def dash(self):
        winsound.Beep(440,600)
        
    def translate(self,char):
        if (char=='A' or char=='a'):
            self.dot()
            self.dash()

    def encode(text):
        print (text)
        
    def decode(code)
        print (code)
        
        
if __name__ == "__main__":
    print ("welcome to morse encoder-decoder")
