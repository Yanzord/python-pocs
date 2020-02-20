import redis

r = redis.Redis()

r.mset({
    "Name": "Yan",
    "Champion": "Kai'Sa"
})

print(r.get("Champion"))