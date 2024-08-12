# Finetuning on AWS

## Overview

This repository provides a streamlined approach to fine-tuning Large Language Models (LLMs) on AWS SageMaker using the LLaMA Factory framework. It aims to simplify the process of adapting powerful language models to specific tasks or domains using AWS cloud infrastructure.

## Features

- Leverage AWS SageMaker for scalable and managed machine learning workflows
- Utilize LLaMA Factory for efficient fine-tuning of various LLM architectures
- Implement distributed training across multiple nodes and GPUs
- Deploy fine-tuned models on SageMaker endpoints
- Support for advanced fine-tuning techniques like QLora SFT (Quantized Low-Rank Adaptation Supervised Fine-Tuning)

## Getting Started

1. Clone this repository:
```
   git clone https://github.com/tsaol/finetuning-on-aws.git
```

2. Set up your AWS environment and configure your credentials

3. Follow the Jupyter notebooks in the `finetuning-llamafactory/` directory for step-by-step guidance

## Prerequisites

- An AWS account with appropriate permissions
- Basic understanding of AWS SageMaker and machine learning concepts
- Familiarity with Python programming

## Repository Structure

- `finetuning-llamafactory/`: Main directory containing the finetuning scripts and notebooks
- `LLaMA-Factory @ f6ac23e`: Submodule containing the LLaMA Factory framework (linked to a specific commit)
- `awsome-distributed-training @ 26130c0`: Submodule with resources for distributed training (linked to a specific commit)

## Usage

Detailed usage instructions are provided in the Jupyter notebooks. These cover:

1. Data preparation
2. Model selection and configuration
3. Fine-tuning process
4. Evaluation and iteration
5. Model deployment on SageMaker endpoints

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LLaMA Factory](https://github.com/hiyouga/LLaMA-Factory)
- [AWS SageMaker](https://aws.amazon.com/sagemaker/)

## Contact

For questions or feedback, please open an issue in this repository.

