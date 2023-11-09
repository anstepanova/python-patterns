import platform
import subprocess

from abc import (
    ABC,
    abstractmethod,
)


class CommandImplementer(ABC):
    @abstractmethod
    def get_directory_listing(self):
        pass

    @abstractmethod
    def get_current_directory(self):
        pass


class UnixCommandImplementer(CommandImplementer):
    def get_directory_listing(self):
        print(f'The directory contains:')
        directory_listing_command_result = subprocess.run(['ls', '-al'])
        return directory_listing_command_result

    def get_current_directory(self):
        print(f'The current directory is:')
        current_directory_command_result = subprocess.run(['pwd', ])
        return current_directory_command_result


class WindowsCommandImplementer(CommandImplementer):
    def get_directory_listing(self):
        print(f'The directory contains:')
        directory_listing_command_result = subprocess.run(['cmd', '/c', 'chdir', ])
        return directory_listing_command_result

    def get_current_directory(self):
        print(f'The current directory is:')
        current_directory_command_result = subprocess.run(['cmd', '/c', 'dir', ])
        return current_directory_command_result


class CommandFactory(ABC):
    @abstractmethod
    def create_command_implementer(self) -> CommandImplementer:
        pass


class UnixFactory:
    def create_command_implementer(self) -> UnixCommandImplementer:
        return UnixCommandImplementer()


class WindowsFactory:
    def create_command_implementer(self) -> WindowsCommandImplementer:
        return WindowsCommandImplementer()


def get_correct_factory():
    os_name = platform.uname().system
    print(f'The current OS is {os_name}')
    if os_name in ('Linux', 'Darwin'):
        return UnixFactory()
    elif os_name == 'Windows':
        return WindowsFactory()
    raise OSError('The current OS isn\'t compatible')


class CommandAbstract:
    def __init__(self):
        self.command_implementer = get_correct_factory().create_command_implementer()

    def get_directory_listing(self):
        self.command_implementer.get_directory_listing()

    def get_current_directory(self):
        self.command_implementer.get_current_directory()

    def get_current_directory_and_listing(self):
        self.command_implementer.get_current_directory()
        self.command_implementer.get_directory_listing()


if __name__ == '__main__':
    command_abstract = CommandAbstract()
    command_abstract.get_current_directory()
    command_abstract.get_directory_listing()
    command_abstract.get_current_directory_and_listing()
