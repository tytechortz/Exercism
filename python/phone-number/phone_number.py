class Phone(object):

    def __init__(self, phone_number):
        self.phone_number = phone_number
    
    def rmv_space(self):
        digits = (''.join(i for i in self.phone_number if i.isdigit()))
        if len(digits) > 11:
            raise ValueError('Too many digits')
        else: 
            return digits[1:]

    def 

    # def check_length(self, digits):
    #     digits = digits
    #     if len(digits) > 10:
    #         raise ValueError('Too many digits')
        
        


# phone = Phone("+1 (613)-995-0253")  
# print(phone.rmv_space())
# print(phone.check_length())



