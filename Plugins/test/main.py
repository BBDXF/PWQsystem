
"""\
in the main framework, it's job is to register all the functions
which the plugins will use, and the framework will also call the
functions defined in the plugins when neccessary
"""
import sys
import os

class PluginsFramework():
    def __init__(self):
        self.attributes = {}
        self.plugins_names = []
        self.plgins_name_func = {}

    def set_attributes(self, **kwargs):
        for k, v in kwargs.iteritems():
            self.attributes[str(k)] = v
    def get_attributes(self, k):
        return self.attributes[str(k)]
    def set_plugin(self, name, func):
        self.plugins_names.append(name)
        self.plgins_name_func[str(name)] = func
    def printall(self):
        print("The Attributes:")
        for k, v in self.attributes.iteritems():
            print(k, v)
        print("the plugins and func:")
        for k, v in self.plgins_name_func.iteritems():
            print(k, v)

if __name__ == "__main__":
    rf = PluginsFramework()
    rf.set_attributes(color='red', text='my name is plugins sys', version='1.0')
    for i in range(0, 30):
        rf.set_plugin('pluginName{}'.format(i), 'functions_{}'.format(i))

    rf.printall()


