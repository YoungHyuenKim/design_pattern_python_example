class SingletonBase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance


class RealSingleton(SingletonBase):
    pass


if __name__ == '__main__':
    instance1 = RealSingleton()
    instance2 = RealSingleton()

    print("first id : ", id(instance1))
    print("first id : ", id(instance2))
