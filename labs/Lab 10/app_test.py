import unittest
from app import app, add_task, get_tasks  

class TaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        global tasks
        tasks = [] 

    def test_add_task(self):
        add_task("task1")
        self.assertIn("task1", get_tasks()) 

    def test_get_tasks(self):
        add_task("task1")
        add_task("task2")
        self.assertEqual(get_tasks(), ["task1", "task2"])

    def test_add_task_route(self):
        response = self.app.post('/add_task', data={'task': "task1"})
        self.assertEqual(response.status_code, 302)
        self.assertIn('task1', get_tasks())

        response = self.app.get('/')
        self.assertIn(b'task1', response.data)
        self.app.post('/add_task', data={'task': "task2"})
        response = self.app.get('/')
        self.assertIn(b'task2', response.data)

if __name__ == '__main__':
    unittest.main()
