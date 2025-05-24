# Gunicorn official docs: https://docs.gunicorn.org/en/stable/settings.html

from multiprocessing import cpu_count

wsgi_app = "main:app"

# Logging
## https://docs.gunicorn.org/en/stable/settings.html#logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Server Socket
## https://docs.gunicorn.org/en/stable/settings.html#server-socket
bind = "0.0.0.0:8000"

# Worker Processes
## https://docs.gunicorn.org/en/stable/settings.html#worker-processes
workers = cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"

## ref: https://github.com/benoitc/gunicorn/pull/862#issuecomment-53175919
max_requests = 500
max_requests_jitter = 200
