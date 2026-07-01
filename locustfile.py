from locust import HttpUser, between, task

class vllmUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def chat_completion(self):
        self.client.post(
            "/v1/completions",
            json={
                "model":"google/gemma-2b-it",
                "prompt":"Explain LangGraph in ine sentence",
                "max_tokens":100,
                "temperature":0.3
            },
            headers={
                "Content-Type":"application/json"
            }
        )