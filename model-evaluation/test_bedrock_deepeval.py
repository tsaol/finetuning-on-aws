from langchain_community.chat_models import BedrockChat
from deepeval.models.base_model import DeepEvalBaseLLM
from deepeval.metrics import AnswerRelevancyMetric

class AWSBedrock(DeepEvalBaseLLM):
    def __init__(
        self,
        model
    ):
        self.model = model

    def load_model(self):
        return self.model

    def generate(self, prompt: str) -> str:
        chat_model = self.load_model()
        return chat_model.invoke(prompt).content

    async def a_generate(self, prompt: str) -> str:
        chat_model = self.load_model()
        res = await chat_model.ainvoke(prompt)
        return res.content

    def get_model_name(self):
        return "Bedrock Models"

# Replace these with real values
custom_model = BedrockChat(
    credentials_profile_name ="default", 
    region_name = "us-west-2", 
    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0",
    model_kwargs = {"temperature": 0.4}
)

aws_bedrock = AWSBedrock(model=custom_model)
print(aws_bedrock.generate("Write me a joke"))


metric = AnswerRelevancyMetric(model=aws_bedrock)
