
from sf2_userclass import User


class Leaner(User):

    def __init__(self, user_id, username, email_address, password, phone_number):
        
        super().__init__(user_id, username, email_address, password, phone_number)