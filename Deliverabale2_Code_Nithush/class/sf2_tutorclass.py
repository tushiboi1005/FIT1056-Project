
from sf2_userclass import User



class Tutor(User):

    def __init__(self, user_id, username, email_address, password, phone_number,fullname,qualifications,available_times,assigned_times):

        super().__init__(user_id, username, email_address, password, phone_number)
        self.fullname = fullname
        self.qualifications = qualifications
        self.available_times = available_times
        self.assigned_times = assigned_times

    
    def update_times():
        pass

    def add_lessons():
        pass