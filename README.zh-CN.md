# Data Science Toolkit
这是一个面向科研任务开发的数据科学常用工具集，旨在通过代码的模块化封装，提升数据处理、统计分析及可视化工作的效率与可复现性。

本仓库提炼了科研分析中高频使用的核心方法论，将复杂的任务拆解为即插即用的逻辑模块，从而使研究能够从繁琐的工程配置中解脱出来，专注于核心数据的洞察与解释。


## 🛠️ 核心架构和设计理念: 可复用性与可靠性
我基于在大量数据实践中总结出的高效流程，遵循以下两大核心原则，确保工具的可靠性与可扩展性:
### 统一高效的数据文件格式标准 (Legacy)
为实现数据处理的灵活性、便捷性与性能的稳定，我优先支持并提供了与其他格式(如 CSV/Excel)的默认转换方法:
- JSONLines(.jsonl): 数据基础。灵活支持各种复杂嵌套数据类型，方便流式处理和日志存储。
- SQLite(.db): 嵌入式数据库。统一处理方法。小型、零配置数据库，方便各种编程语言统一使用 SQL 进行数据处理。
- DUCKDB(.duckdb): 嵌入式分析数据库。高性能分析，我逐步支持的方向之一。

### 函数式编程与可靠的数据流水线 (Pipeline)
借鉴函数式编程范式，构建可组合且状态可追踪的处理流程:
- **可缓存性 (Caching)**：支持自动保存中间计算结果，既能避免重复计算开销，也便于对实验每一步的输出进行核查与审计。
- **可组合性 (Composability)**：处理模块采用解耦设计，支持像积木般灵活组合，提高核心算法在不同课题间的复用率。
- **可扩展性 (Extensibility)**：在保持轻量化的前提下，为特定科研需求留出接口，避免过度工程化。


## 🚀 性能演进：从 Pandas 转向现代架构
> **重要更新:** 随着数据规模的扩大，本项目正逐步从传统的 `Pandas/JSONL` 堆栈向高性能计算架构迁移。

### 迁移方向与动机:
- **计算引擎: 从 Pandas 转向 Polars** 针对大规模实验数据，Pandas 易受单核性能与内存溢出的限制。通过引入 **Polars**，利用其多线程并行引擎与惰性求值（Lazy Evaluation）特性，在百万级数据处理中显著降低内存消耗并提升运行效率。
- **内存标准: 基于 Apache Arrow** 采用 **Arrow** 作为内存中数据的统一标准，消除不同处理工具间数据传递的序列化/反序列化成本，实现与 DuckDB 等高性能后端间的“零拷贝”集成。
- **存储优化: Parquet & Avro**
  - **Parquet**: 针对分析型任务（OLAP），利用其列式存储与高压缩比，大幅减少科学计算过程中的磁盘 I/O。
  - **Avro**: 针对流式数据或结构变动频繁的场景，确保数据 Schema 的鲁棒性。


## 📂 核心模块概览
为了方便快速定位所需功能，下表概括了本工具集的主要能力范围:

| 任务 | 核心模块 | 主要解决问题 | 核心技术栈 |
|-----------| --- | --- | --- |
| **数据处理**  | Data Processing | I/O 加速、异步清洗、特征工程 | Polars / Arrow |
| **统计分析**  | Statistical Analysis | 描述统计、假设检验、基础回归分析 | statsmodels / scipy |
| **机器学习**  | Machine Learning | 无监督学习、模型评估、预处理 Pipeline | scikit-learn |
| **文本分析**  | Text Analysis | 高可解释性 NLP、文本向量化、语义聚类 | NLTK / Scikit-learn |
| **快捷可视化** | Quick Visualization | 交互式探索、**学术论文规范配图** | Plotly |


### 🔍 模块说明
#### 🛠️ Data Processing
专注于数据的 I/O 优化、质量保障和结构化转换。
- **Data Acceleration**: 通过异步编程和多线程，加速 I/O 密集型和计算密集型任务。
- **Data Cleaning**: 包含缺失值处理、异常值检测及数据类型严格校验。
- **Feature Engineering**: 标准化、独热编码等即插即用的特征转换方法。

#### 📊 Statistical Analysis
基于统计学原理，快速进行数据形态验证，指导建模方向。
- **Descriptive Stats**: 快速查看分布和关联性。
- **Hypothesis Testing**: 提供参数与非参数检验工具。
- **Regression Models**: 基础通用回归工具，用于快速基准测试。

#### 🤖 Machine Learning
侧重于通用预处理和模型观测。
- **Unsupervised Learning**: 用于数据的聚类、降维和异常检测。
- **Model Evaluation**: 提供多维度的模型指标评估和交叉验证工具。

#### 📝 Text Analysis
面向高可解释性的非深度学习任务。
- **Text Computing**: 基于规则与统计的计算方法。
- **Text Visualization**: 词云生成、主题模型展示及语义聚类可视化。

*注：高性能 NLP 任务建议参考我的 [Deep-Learning-Toolkit](https://github.com/yuliu625/Yu-Deep-Learning-Toolkit)。*

#### 📈 Quick Visualization
基于 `Plotly` 等库构建，平衡“交互性”与“出版质量”。
- **Data Explore**: 预置多种查看数据分布和相互关系的方法。
- **Data Report**: **学术论文配置**。总结了顶级期刊常用的配色、字体和布局规范，实现一键出图。


## 🔗 系列工具箱
该仓库是我个人科研工具链的一部分，你可以配合以下仓库使用:
- **[RAG-Toolkit](https://github.com/yuliu625/Yu-RAG-Toolkit)**: 核心检索增强工具集。
- **[Agent-Development-Toolkit](https://github.com/yuliu625/Yu-Agent-Development-Toolkit)**: 专注于智能体(Agents)逻辑构建。
- **[Deep-Learning-Toolkit](https://github.com/yuliu625/Yu-Deep-Learning-Toolkit)**: 深度学习通用任务底座。
- **[Data-Science-Toolkit](https://github.com/yuliu625/Yu-Data-Science-Toolkit)**: 数据科学与预处理工具。

