from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    return "Üdvözlöm az oldalon!, Számláló = "+counter+" látogatás"

@app.route('/null')
def null():
    redis.set('hits', 0)
    return "Nullázva"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    print("Server runing...")
