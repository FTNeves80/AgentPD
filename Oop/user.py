class User:
    def __init__(self, user_email , name,  password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title


    def change_password(self, new_password):
        if len(new_password) >= 8:
            self.password = new_password
            print("Password changed successfully.")
        else:
            print("Password must be at least 8 characters long.")
    
    def update_job_title(self, new_job_title):
        if new_job_title:
            self.current_job_title = new_job_title
            print("Job title updated successfully.")
        else:
            print("Job title cannot be empty.")

    def display_user_info(self):
        print(f"Email: {self.email}")
        print(f"Name: {self.name}")
        print(f"Current Job Title: {self.current_job_title}")
        print(f"Password: {self.password}")