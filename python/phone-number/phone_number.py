class Phone(object):

    def __init__(self, phone_number):
        self.digits = self.clean(phone_number)
    
    def clean(self, digits):
        clean_digits = (''.join(i for i in self.digits if i.isdigit()))
        if len(clean_digits) > 11:
            raise ValueError('Too many digits')
        else: 
            return digits[1:]

        


phone = Phone("+1 (613)-995-0253")  
print(phone.clean("+1 (613)-995-0253"))
# print(phone.check_length())



