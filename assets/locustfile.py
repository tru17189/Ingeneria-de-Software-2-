from locust import HttpLocust, TaskSet, task

class UserDefinedTask(TaskSet):
    @task(1)
    def home(self):
        self.client.get("/students/31082019/")

class User(HttpLocust):
    task_set = UserDefinedTask
    min_wait = 1000
    max_wait = 2000
