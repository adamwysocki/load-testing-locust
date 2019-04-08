from locust import HttpLocust, TaskSet, TaskSequence, task, seq_task

# random API checks
class GeneralTasks(TaskSet):
    @task(2)
    def product(self):
        self.client.get("/v1/product?id=14552")
        
    @task(1)
    def dispensaries(self):
        self.client.get("/v2/dispensary")

    @task(1)
    def dispensaries_paged(self):
        self.client.get("/v2/dispensary?skip=100")

    @task(3)
    def dispensary(self):
        self.client.get("/v2/dispensary?id=176364")

    @task(1)
    def brands(self):
        self.client.get("/v1/brand")

    @task(3) 
    def menuitems(self):
        self.client.get("/v3/menuitem?dispensary_id=127818")

# simulates finding and viewing a dispensary
class ViewDispensaryTasks(TaskSequence):
    @seq_task(1)    
    @task(1)
    def dispensaries(self):
        self.client.get("/v2/dispensary")

    @seq_task(2)
    @task(1)
    def dispensaries_paged(self):
        self.client.get("/v2/dispensary?skip=0&name_includes=diego")

    @seq_task(3)
    @task(1)
    def dispensary(self):
        self.client.get("/v2/dispensary?id=176364")

    @seq_task(4)
    @task(3) 
    def menuitems(self):
        self.client.get("/v3/menuitem?dispensary_id=127818")


class GeneralUser(HttpLocust):
    task_set = GeneralTasks
    min_wait = 5000
    max_wait = 15000

class DispensaryViewer(HttpLocust):
    task_set = ViewDispensaryTasks
    min_wait = 5000
    max_wait = 15000