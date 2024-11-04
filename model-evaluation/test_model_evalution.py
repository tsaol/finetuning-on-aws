from langchain_community.chat_models import BedrockChat
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from deepeval import assert_test

# 配置Bedrock模型
bedrock_model = BedrockChat(
    credentials_profile_name="default",  # AWS配置文件名
    region_name="us-west-2",            # AWS区域
    model_id="meta.llama3-1-8b-instruct-v1:0", # Llama模型ID
    model_kwargs={
        "temperature": 0.4,
        "max_tokens": 512
    }
)

# 创建测试用例
test_case = LLMTestCase(
    input="你好，请介绍下自己",
    actual_output="我是一个AI助手",
    context="AI助手的自我介绍"
)

# 创建评估指标
metric = AnswerRelevancyMetric(threshold=0.7)

# 执行测试
result = assert_test(test_case, [metric])