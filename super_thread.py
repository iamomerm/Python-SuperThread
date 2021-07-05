import threading
import ctypes


class SuperThread(threading.Thread):
    active_threads = []  # List of Active Super Threads

    def __init__(self, name, method):
        threading.Thread.__init__(self)
        self.name = name
        self.method = method
        self.setDaemon(True)
        SuperThread.active_threads.append(self)

    def __del__(self):
        del self

    def get_id(self):
        # Returns Id of The Respective Thread
        return self.ident

    @staticmethod
    def terminate_by_name(name):
        for thread in SuperThread.active_threads:
            if thread.name == name:
                thread.terminate()

    @staticmethod
    def terminate_all():
        for thread in SuperThread.active_threads:
            thread.terminate()

    def terminate(self):
        SuperThread.active_threads.remove(self)
        id = self.get_id()
        # Terminate (Throw Exception)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(id), ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(id), 0)
        self.__del__()

    def run(self):
        self.method()
