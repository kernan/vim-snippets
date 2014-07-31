class Arg(object):
    def __init__(self, arg):
        self.arg = arg.split('=')[0].strip()
        try:
            self.name = self.arg.split()[-1].strip()
        except IndexError:
            self.name = ''
            pass

    @staticmethod
    def get_args(arglist):
        args = [Arg(arg) for arg in arglist.split(',') if arg]
        return args

class TypeArg(Arg):
    def __init__(self, arg):
        super(TypeArg, self).__init__(arg)
        self.type = ' '.join(self.arg.split()[0:-1]).strip()

    @staticmethod
    def get_args(arglist):
        args = [TypeArg(arg) for arg in arglist.split(',') if arg]
        return args
