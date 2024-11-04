import boto3
import json
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric


# 配置AWS客户端
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    # 选择适合的区域
    region_name='us-west-2'
)

def invoke_llama(prompt):
    # 设置模型参数
    model_id = "meta.llama2-13b-chat-v1"  # 或选择其他版本
    body = json.dumps({
        "prompt": f"<s>[INST] {prompt} [/INST]",
        "max_gen_length": 512,
        "temperature": 0.5
    })
    
    # 调用模型
    response = bedrock_runtime.invoke_model(
        body=body,
        modelId=model_id,
        contentType="application/json",
        accept="application/json"
    )
    return json.loads(response['body'].read())

def test_llama_response():
    # 创建测试用例
    test_case = LLMTestCase(
        input="测试问题",
        actual_output=invoke_llama("测试问题"),
        context="预期上下文"
    )
    
    # 设置评估指标
    metric = AnswerRelevancyMetric(threshold=0.5)
    return test_case, metric


# 执行测试
from deepeval import assert_test

test_case, metric = test_llama_response()
assert_test(test_case, [metric])