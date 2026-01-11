import yaml
import json
from utils.llm import get_llm

llm = get_llm()


class ComponentCleaner:
    def __init__(self, prompt_path="prompts/component_cleanup.yaml"):
        with open(prompt_path, "r") as f:
            self.prompt = yaml.safe_load(f)

    def clean(self, component: str) -> str:
        messages = [
            {"role": "system", "content": self.prompt["system"]},
            {
                "role": "user",
                "content": self.prompt["user"].replace("{{component}}", component)
            }
        ]

        response = llm.invoke(messages)

        try:
            data = json.loads(response.content)
            return data.get("clean_component", component)
        except Exception:
            return component
