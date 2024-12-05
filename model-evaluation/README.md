# 模型评估工具 (LLM Evaluation Tool)

基于AWS Bedrock 和 promptfoo的模型评估工具，用于进行大规模语言模型的性能测试和评估。

## 功能特点

- 支持AWS Bedrock服务的模型评估
- 使用promptfoo进行自动化测试
- 提供详细的评估报告和分析
- 支持多种评估指标和测试场景

## 环境要求

- 实例配置：AWS c7g.large
- 操作系统：Ubuntu 22.04
- Node.js 环境

## 安装步骤

1. 安装 NVM (Node Version Manager)
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
```

2. 安装 Node.js
```bash
nvm install 22
```

3. 验证Node.js安装
```bash
node -v
npm -v
```

4. 安装 promptfoo
```bash
npm install -g promptfoo
```

5. 安装 AWS Bedrock Runtime SDK
```bash
npm install -g @aws-sdk/client-bedrock-runtime
```

## 使用说明

1. 确保已完成所有依赖项的安装
2. 验证promptfoo安装
```bash
promptfoo --version
```

3. 运行评估测试
```bash
promptfoo eval
```

## 项目结构

```
.
├── README.md                    # 项目说明文档
├── test_bedrock_deepeval.py    # Bedrock深度评估测试脚本
├── test_model_evalution.py     # 模型评估测试脚本
├── promptfoo.yaml              # promptfoo配置文件
└── docs/                       # 文档和示例
    ├── 1.png
    ├── 2.png
    └── 3.png
```

## 示例

项目包含多个测试示例和评估结果，详细信息请参考 `docs` 目录下的截图。

## 注意事项

- 请确保您有适当的AWS权限和配置
- 建议在评估前检查AWS配额限制
- 评估过程可能产生相应的AWS费用

## 许可证

MIT License

## 贡献指南

欢迎提交Issue和Pull Request来帮助改进项目。
