
from sf2_userclass import User


class Admin(User):

    def __init__(self, user_id, username, email_address, password, phone_number,fullname,qualifications):

        super().__init__(user_id, username, email_address, password, phone_number)
        self.fullname = fullname
        self.qualifications = qualifications

    def add_lessons():
        pass

    def modify_lessons():
        pass

    def delete_lessons():
        pass

    def remove_user():
        pass

