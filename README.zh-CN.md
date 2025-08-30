# Data Science Toolkit

## 概述
这个仓库是我对于常见数据科学任务构建的工具集。主要分为数据处理方法和数据分析方法。

这个仓库中大部分文件多设计为仅一个文件就可以运行，目的是能够在多种项目中快速引入和使用。

## 约定
通过大量的具体任务，我总结出以下最佳实践:
### 数据文件格式
我倾向于使用的数据格式:
- jsonlines: 可处理流式数据，可灵活处理各种情况。
- sqlite: 小型嵌入式数据库，方便各种编程语言统一用sql进行数据处理。
### 数据处理流程
遵循函数式编程思想，并基于构造可靠pipeline的为目的:
- 可缓存: 可保留中间结果，以实现加速或检验中间过程。
- 可组合: 以不同的方式组合，可复用组件。
- 易于扩展: 避免过度设计，但留有必要情况下的扩展方法。


## 内容
### mapreduce_methods
通过mapreduce算法获得的启发，我构建了一些加速数据处理的方法。通过对数据集的初始状态的划分，避免因竞争导致的各种问题。方法包括:
- jsonline_accelerator: 专门针对jsonline数据的处理方法。同时内部使用高效的 `orjson` 或 `ujson` 实现IO加速。我非常推荐使用。
- df_accelerator: 对于通用df的加速方法，使用pandas进行数据处理。但我并不推荐使用，原因在于pandas的interface设计得并不够好，同时运行效率低下。对于大型数据，pandas有时无法避免的将全部数据都加载到内存中，这对分析有利，但对数据处理不好。这些方法仅为了在一些情况下提供兼容性。
- torch_accelerator: 利用torch的dataset和dataloader设计，使用torch的多线程方法。可能有些舍近求远，尤其是不在进行深度学习任务。

对于sqlite，如果你会异步编程，可直接使用aiosqlite，从而避免各种构建和具体的处理任务。

### text_analysis
非深度学习任务的NLP方法，常见的文本计算方法。多用于文本数据的结果分析和可视化。方法包括:
- pre_processing_tools: 文本预处理方法。
- rule_based_methods: 基于规则的方法。主要基于的工具是正则表达式。
- statistical_based_methods: 基于统计学的方法。适用于基础的文本分析。
- machine_learning_based_methods: 基于机器学习的方法。这里指的不是去训练机器学习模型，而是使用预训练的机器学习模型进行文本数据处理。
- embedding_based_methods: 文本向量方法。对向量的计算和处理方法。可能无法避免的需要使用到深度学习模型。


## 更多
如果你关注类似的任务，可以查看我其他的仓库:
- [Deep-Learning-Toolkit](https://github.com/yuliu625/Yu-Deep-Learning-Toolkit): 一个用于深度学习任务的通用工具集。
- [Agent-Development-Toolkit](https://github.com/yuliu625/Yu-Agent-Development-Toolkit): 专注于LLM和Agent构建的工具集。

