  self.app.post('/add-task', data={'task': "task2"})
        response = self.app.get('/')
        self.assertIn(b'task2', response.data)