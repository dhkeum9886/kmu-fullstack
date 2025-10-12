from __future__ import annotations
import bentoml

with bentoml.importing():
    from transformers import pipeline

EXAMPLE_INPUT = 'This is a demonstration of BentoML with a summarization model.'

@bentoml.service
class Summarization:
    def __init__(self) -> None:
        self.pipeline = pipeline('summarization')

    @bentoml.api
    def summarize(self, text: str = EXAMPLE_INPUT) -> str:
        result = self.pipeline(text)
        return f"Here's your summary: {result[0]['summary_text']}"