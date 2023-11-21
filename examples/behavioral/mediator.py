from collections import namedtuple


Message = namedtuple('Message', ['author', 'text'])


class Mediator:
    users: list["User"] = []

    @staticmethod
    def register_user(user: "User") -> None:
        Mediator.users.append(user)

    @staticmethod
    def unregister_user(user: "User") -> bool:
        try:
            Mediator.users.remove(user)
        except ValueError:
            return False
        return True

    @staticmethod
    def translate_message_to_user(sender: "User", receiver: "User", text: str):
        try:
            receiver_index = Mediator.users.index(receiver)
        except ValueError:
            return
        message = Message(str(sender), text)
        Mediator.users[receiver_index].receive_message(message)

    @staticmethod
    def translate_message_to_everybody(sender: "User", text: str):
        message = Message(str(sender), text)
        for current_user in Mediator.users:
            current_user.receive_message(message)


class User:
    def __init__(self, username: str, mediator: Mediator = Mediator):
        self.username = username
        self.chat: list[Message] = []
        self.mediator = mediator
        self.mediator.register_user(self)

    def receive_message(self, message: Message):
        self.chat.append(message)

    def send_message_to_user(self, user: "User", text: str) -> None:
        self.mediator.translate_message_to_user(self, user, text)

    def send_message_to_everybody(self, text: str) -> None:
        self.mediator.translate_message_to_everybody(self, text)

    def print_chat(self):
        print(f'{self.username} chat:')
        for message in self.chat:
            print(f'{message.author}: {message.text}')
        print()

    def __repr__(self):
        return self.username

    def __del__(self):
        Mediator.unregister_user(self)
        del self


if __name__ == '__main__':
    cat = User('cat-user')
    dog = User('dog')
    fox = User('fox')
    cat.send_message_to_user(user=fox, text='Hi, fox!')
    cat.send_message_to_everybody(text='Hi, everyone!')
    fox.send_message_to_user(user=cat, text='Hi, cat!')
    fox.send_message_to_everybody(text='Hi, guys!')
    dog.send_message_to_everybody(text='Hi')

    cat.print_chat()
    fox.print_chat()
    dog.print_chat()
