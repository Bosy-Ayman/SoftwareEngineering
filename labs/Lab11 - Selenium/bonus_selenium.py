from seleniumbase import BaseCase

class TaskManagement(BaseCase):
    
    def test_add_task(self):
        self.open('http://127.0.0.1:5000')

        self.assert_title('Task Management')
        self.assert_text('Tasks Management', 'h1') 
        self.assert_text('No tasks are added', 'ul')  
