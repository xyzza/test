from envparse import Env

env = Env()

DB_DSN = env.str(
    "DB_DSN", default="postgresql://postgres:postgres@localhost:5432/counter"
)
# timeout in seconds
DB_TIMEOUT = env.int("DB_TIMEOUT", default=1)
DB_POOLSIZE = env.int("DB_POOLSIZE", default=10)
