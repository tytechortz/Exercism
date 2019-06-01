class Phone(object):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def rmv_space(self):
        print(''.join(i for i in self.phone_number if i.isdigit()))


phone = Phone("223.456.7890")  
phone.rmv_space()

