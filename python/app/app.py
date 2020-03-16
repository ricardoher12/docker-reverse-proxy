from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
result = redis.ping()
print("Resultado de Ping: " + str(result))

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello this has been viewed %s time(s).' % redis.get('hits')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)