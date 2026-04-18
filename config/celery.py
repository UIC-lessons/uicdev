from celery import Celery

app = Celery("celery", broker = "redis://localhost")

@app.task
def add(x, y):
    return x + y