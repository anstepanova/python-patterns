from abc import (
    ABC,
    abstractmethod,
)


class Subject:
    def provide_data(self, user: str):
        pass


class RealSubject(Subject):
    def provide_data(self, user: str) -> None:
        print(f'Providing data for {user} user')


class ProxySubject(Subject):
    ALLOWED_USERS = ('admin', 'db-admin', 'aws-admin')

    def __init__(self):
        self.real_subject = RealSubject()

    def provide_data(self, user: str) -> None:
        if user.lower() in ProxySubject.ALLOWED_USERS:
            return self.real_subject.provide_data(user)
        print(f'Impossible to provide data for {user} user')


if __name__ == '__main__':
    proxy_subject = ProxySubject()
    proxy_subject.provide_data('admin')
    proxy_subject.provide_data('user')
    proxy_subject.provide_data('aws-admin')
    proxy_subject.provide_data('test-admin')