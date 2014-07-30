class Arg(object):
    def __init__(self, arg):
        self.arg = arg.split('=')[0].strip()
        self.type = ' '.join(self.arg.split()[0:-1])
        try:
            self.name = self.arg.split()[-1].strip()
        except IndexError:
            self.name = ''
            pass

    def __str__(self):
        return self.arg

    def __unicode__(self):
        return self.arg

    @staticmethod
    def get_args(arglist):
        args = [Arg(arg) for arg in arglist.split(',') if arg]
        return args
