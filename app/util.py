import redis

from flask import current_app


class Redis(object):
    """
    redis数据库操作
    """

    @staticmethod
    def _get_r():
        host = current_app.config['REDIS_HOST']
        port = current_app.config['REDIS_PORT']
        db = current_app.config['REDIS_DB']
        r = redis.StrictRedis(host, port, db)
        return r

    @classmethod
    def hset(cls, name, key, value):
        """
        写入hash表
        """
        r = cls._get_r()
        r.hset(name, key, value)

    @classmethod
    def hmset(cls, name, mapping):
        """
        指定hash表的所有给定字段的值
        """
        r = cls._get_r()
        r.hmset(name, mapping)


    @classmethod
    def hget(cls, name, key):
        """
        读取指定hash表的键值
        """
        r = cls._get_r()
        value = r.hget(name, key)
        if value is not None:
            value_decode = value.decode()
        else:
            value_decode = None
        return value_decode

    @classmethod
    def hgetall(cls, name):
        """
        获取指定hash表所有的值
        """
        r = cls._get_r()
        return r.hgetall(name)

    @classmethod
    def delete(cls, *names):
        """
        删除一个或者多个
        """
        r = cls._get_r()
        r.delete(*names)

    @classmethod
    def hdel(cls, name, key):
        """
        删除指定hash表的键值
        """
        r = cls._get_r()
        r.hdel(name, key)

    @classmethod
    def expire(cls, name, expire=None):
        """
        设置过期时间
        """
        if expire:
            expire_in_seconds = expire
        else:
            expire_in_seconds = current_app.config['REDIS_EXPIRE']
        r = cls._get_r()
        r.expire(name, expire_in_seconds)
