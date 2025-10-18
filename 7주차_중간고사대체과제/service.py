from __future__ import annotations
import bentoml


@bentoml.service
class Hello:

    @bentoml.api
    def greet(self, name: str = 'Bento') -> str:
        return f'풀스택서비스구축, {name} !'
