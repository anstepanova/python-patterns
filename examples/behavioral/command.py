from abc import (
    ABC,
    abstractmethod,
)
from collections import deque
from typing import Type


class Word:
    def __init__(self, context: str):
        self.__context = context

    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, new_value: str):
        self.__context = new_value


    def make_upper_case(self):
        self.__context = self.__context.upper()

    def make_lower_case(self):
        self.__context = self.__context.lower()



class Command(ABC):
    def __init__(self, word: Word):
        self._word = word
        self.previous_context = self._word.context

    @abstractmethod
    def execute(self, **kwargs) -> None:
        pass

    @abstractmethod
    def unexecute(self) -> None:
        pass


class CommandHistory:
    def __init__(self):
        self.actions = deque()

    def push(self, command: Command) -> None:
        self.actions.append(command)

    def pop(self) -> Command | None:
        try:
            previous_command = self.actions.pop()
        except IndexError:
            return
        return previous_command


class UpperCaseCommand(Command):
    def execute(self):
        self._word.make_upper_case()

    def unexecute(self) -> None:
        self._word.context = self.previous_context


class LowerCaseCommand(Command):
    def execute(self) -> None:
        self._word.make_lower_case()

    def unexecute(self) -> None:
        self._word.context = self.previous_context


class WordAction:
    def __init__(self, word: Word):
        self.word = word
        self.command_history = CommandHistory()

    def __apply_command_to_word(self, command_type: Type[Command], **kwargs) -> str:
        command = command_type(word=self.word)
        command.execute(**kwargs)
        self.command_history.push(command)
        print(self.word.context)
        return self.word.context

    def make_upper_case(self) -> str:
        return self.__apply_command_to_word(UpperCaseCommand)

    def make_lower_case(self) -> str:
        return self.__apply_command_to_word(LowerCaseCommand)

    def rollback_last_command(self) -> bool:
        last_command = self.command_history.pop()
        if last_command is None:
            print('There is no any commands left to rollback')
            return False
        last_command.unexecute()
        print(self.word.context)



if __name__ == '__main__':
    word_action = WordAction(Word('Test!'))
    word_action.make_lower_case()
    word_action.make_lower_case()
    word_action.make_upper_case()
    word_action.make_upper_case()

    print('Rollback last commands')
    word_action.rollback_last_command()
    word_action.rollback_last_command()
    word_action.rollback_last_command()
    word_action.rollback_last_command()
    word_action.rollback_last_command()
    word_action.rollback_last_command()

    print('Apply commands')
    word_action.make_lower_case()
    word_action.make_upper_case()
    print('Rollback last commands:')
    word_action.rollback_last_command()
    word_action.rollback_last_command()
    word_action.rollback_last_command()


