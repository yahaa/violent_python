import sys
from inspect import getdoc

from compose.cli.docopt_command import NoSuchCommand
from compose.cli.docopt_command import docopt_full_help


def format_doc(doc):
    return doc.replace('dce [options] [COMMAND] [ARGS...]',
                       'bash -c "$(docker run -i --rm %s [options] [COMMAND] [ARGS...])"' % '')


class DocoptCommand(object):
    def docopt_options(self):
        return {'options_first': True}

    def sys_dispatch(self):
        self.dispatch(sys.argv[1:], None)

    def dispatch(self, argv, global_options):
        self.perform_command(*self.parse(argv, global_options))

    def perform_command(self, *args):
        raise NotImplementedError()

    def parse(self, argv, global_options):
        options = docopt_full_help(getdoc(self), argv, **self.docopt_options())
        command = options['COMMAND']

        if command is None:
            raise SystemExit(format_doc(getdoc(self)))

        handler = self.get_handler(command)
        docstring = getdoc(handler)

        if docstring is None:
            raise Exception('docstring is None')

        command_options = docopt_full_help(
            docstring, options['ARGS'], options_first=True)
        return options, handler, command_options

    def get_handler(self, command):
        command = command.replace('-', '_')

        if not hasattr(self, command):
            raise NoSuchCommand(command, self)

        return getattr(self, command)


class TopLevelCommand(DocoptCommand):
    """DaoCloud Enterprise Toolbox.

        Usage:
          dce [options] [COMMAND] [ARGS...]

        Options:
          --verbose          Show more output.

        Commands:
          aaa            Install the DCE Controller.
        """

    def perform_command(self, options, handler, command_options):
        handler(command_options)
        return

    def aaa(self, options):
        """
        Install the DCE Controller.

        Usage: aaa

        Description:
            The command will install the DCE Controller on this machine.

        """
        print 'aaa'

    def bbb(self, options):
        """
        Install the DCE Controller.

        Usage: bbb

        Description:
            The command will install the DCE Controller on this machine.

        """
        print 'bbb'


if __name__ == '__main__':
    command = TopLevelCommand()
    command.sys_dispatch()
