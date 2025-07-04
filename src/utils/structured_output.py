from typing import Any, List, Union
import transformers
import outlines
from langchain_core.messages import AIMessage, HumanMessage
from pydantic import BaseModel


class ResponseSchema(BaseModel):
    country: str
    city: str


class LLM:
    def __init__(self, model_name: str, system_prompt: str):
        tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
        model = transformers.AutoModelForCausalLM.from_pretrained(model_name)

        self.model = outlines.from_transformers(model, tokenizer)

        self.system_prompt: str = system_prompt
        self.memory: List[Union[AIMessage, HumanMessage]] = []
        self.context: List[str] = []
        self.output_type = None

    def set_output_type(self, output_type: Any):
        self.output_type = output_type

    def set_system_prompt(self, system_prompt: str):
        self.system_prompt = system_prompt

    def update_memory(self, memory: List[Union[AIMessage, HumanMessage]]):
        self.memory = memory

    def set_context(self, context: List[str]):
        self.context = context

    def get_context(self) -> List[str]:
        return self.context

    def prompt_model(self, user_prompt: str) -> Any:
        prompt_parts = []

        if self.system_prompt:
            prompt_parts.append(self.system_prompt)

        for ctx in self.context:
            prompt_parts.append(ctx)

        for msg in self.memory:
            if isinstance(msg, HumanMessage):
                prompt_parts.append(f"User: {msg.content}")
            elif isinstance(msg, AIMessage):
                prompt_parts.append(f"Assistant: {msg.content}")

        prompt_parts.append(f"User: {user_prompt}")

        formatted_prompt = "\n".join(prompt_parts)

        result = self.model(
            formatted_prompt,
            output_type=self.output_type,
            max_new_tokens=100,
            repetition_penalty=1.1,
        )

        return result

    response = llm.prompt_model(user_prompt)


if __name__ == "__main__":
    main()
