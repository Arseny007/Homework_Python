class A:
    @staticmethod
    def new_method():
        pass

# A.new_method()

class Phone:
    @staticmethod
    def code_country(phone):
        return phone[1:-14]

    @staticmethod
    def phone_isvalid(num):
        flag = num[-3] == num[-6] == num[-10] == num[-14] == '-'
        list_ = num[1:].split('-')
        return ''.join(list_).isdigit() and flag and num[0] == '+'


print(Phone.phone_isvalid(input()))