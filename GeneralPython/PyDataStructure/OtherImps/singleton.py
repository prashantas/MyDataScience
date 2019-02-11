## https://gist.github.com/werediver/4396488
import threading

class Singleton(object):
    __singleton_lock = threading.Lock()
    __singleton_instance = None

    @classmethod
    def instance(cls):
        if not cls.__singleton_instance :
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()

        return cls.__singleton_instance

if __name__ == '__main__':

    a,a2 = Singleton.instance(), Singleton.instance()
    b,b2 = Singleton.instance(), Singleton.instance()
    assert a is a2
    assert b is b2
    #assert a is not b  # Gives assertion error

    print('a:  %s\na2: %s' % (a, a2))
    print('b:  %s\nb2: %s' % (b, b2))
