"""Main app"""
import os
from functools import cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)


@app.get("/")
def index():
    """
    :return:
    """
    try:
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")
        return "Sorry, something went wrong \N{pensive face}"
    return f"This page has been seen {page_views} times."


@cache
def redis():
    """
    :return:
    """
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))
