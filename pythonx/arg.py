class Arg(object):
    def __init__(self, arg):
        self.arg = arg.split('=')[0].strip()
        self.type = ' '.join(self.arg.split()[0:-1])
        self.name = self.arg.split()[-1].strip()

    def __str__(self):
        return self.arg

    def __unicode__(self):
        return self.arg

    def get_args(arglist):
        args = [Arg(arg) for arg in arglist.split(',') if arg]
        return args

class PyArg(Arg):
    def __init__(self, arg):
        super(PyArg, self).__init__(arg)
        self.__is_kwarg = '**' in self.arg

    def is_kwarg(self):
        return self.__is_kwarg

    def get_args(arglist):
        args = [PyArg(arg) for arg in arglist.split(',') if arg]
        args = [arg for arg in args if arg.name != 'self']
        return args

if __name__ == '__main__':
    arglist = 'brap, **kwargs'
    args = PyArg.get_args(arglist)
    for arg in args: print(arg.name + ", " + str(arg.is_kwarg()))
