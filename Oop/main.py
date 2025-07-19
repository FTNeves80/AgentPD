from user import User
from post import Post

user1 = User("user@example.com", "John Doe", "password123", "Software Engineer")
post1 = Post("My First Post", "This is the content of my first post.", user1.name)

user1.display_user_info()

user1.change_password("newpassword456")
user1.update_job_title("Senior Software Engineer")

user1.display_user_info()

post1.get_post_info()
