import platform
import subprocess

from abc import (
    ABC,
    abstractmethod,
)


class CommandExecutor(ABC):
    @abstractmethod
    def get_directory_listing(self):
        pass

    @abstractmethod
    def get_current_directory(self):
        pass


class UnixCommandExecutor(CommandExecutor):
    def get_directory_listing(self):
        print(f'The directory contains:')
        directory_listing_command_result = subprocess.run(['ls', '-al'])
        return directory_listing_command_result

    def get_current_directory(self):
        print(f'The current directory is:')
        current_directory_command_result = subprocess.run(['pwd', ])
        return current_directory_command_result


class WindowsCommandExecutor(CommandExecutor):
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
    def create_command_executor(self) -> CommandExecutor:
        pass


class UnixFactory:
    def create_command_executor(self) -> UnixCommandExecutor:
        return UnixCommandExecutor()


class WindowsFactory:
    def create_command_executor(self) -> WindowsCommandExecutor:
        return WindowsCommandExecutor()


def get_correct_factory():
    os_name = platform.uname().system
    print(f'The current OS is {os_name}')
    if os_name in ('Linux', 'Darwin'):
        return UnixFactory()
    elif os_name == 'Windows':
        return WindowsFactory()
    raise OSError('The current OS isn\'t compatible')


if __name__ == '__main__':
    command_executor_factory = get_correct_factory()
    command_executor = command_executor_factory.create_command_executor()
    command_executor.get_current_directory()
    command_executor.get_directory_listing()
