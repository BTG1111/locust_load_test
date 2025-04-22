from locust import SequentialTaskSet, HttpUser, between, task
from locust_plugins.csvreader import CSVReader


reader = CSVReader("test_data.csv")


class ApiTasks1(SequentialTaskSet):
    @task
    def list_user_test(self):
        data = next(reader)
        api_path = f"/api/users?page={data[0]}"
        with self.client.get(api_path, catch_response=True) as response:
            if "data" not in response.text:
                response.failure(
                    f"Success is not true, test input: {data[0]}, test output: {response.status_code},{response.text}"
                )


class UserBehaviour(SequentialTaskSet):
    tasks = [ApiTasks1]


class ApiUsers(HttpUser):
    wait_time = between(1, 1)
    tasks = [UserBehaviour]
