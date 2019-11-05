from locust import HttpLocust, TaskSet, task

class UserDefinedTask(TaskSet):
    #prueba de iingreso a la pagina principal
    @task(1)
    def home(self):
        self.client.get("/students/31082019/")

    @task(2)
    def home(self):
        self.client.get("/students/31082019/libro_mate")
    
    #abrir el libro de matematicas y TIC
    @task(3)
    def home(self):
        self.client.get("/students/31082019/Libro")

    #abrir el libro de ingles tecnico
    @task(4)
    def home(self):
        self.client.get("/students/31082019/ibro_Ingles1")

    #abrir el libro de fisica 1
    @task(5)
    def home(self):
        self.client.get("/students/31082019/libro_Fisica1")


class User(HttpLocust):
    task_set = UserDefinedTask
    min_wait = 1000
    max_wait = 2000
