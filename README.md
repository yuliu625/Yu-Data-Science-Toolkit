# Data Science Toolkit
A comprehensive suite of common data science tools developed for scientific research tasks. It aims to enhance the efficiency and reproducibility of data processing, statistical analysis, and visualization through modular code encapsulation.

This repository distills core methodologies frequently used in research analysis, breaking down complex tasks into plug-and-play logical modules. This allows researchers to break free from tedious engineering configurations and focus on core data insights and interpretation.


## 🛠️ Core Architecture & Design Philosophy: Reusability & Reliability
Based on high-efficiency workflows summarized from extensive data practice, I follow two core principles to ensure tool reliability and scalability:

### Standardized & Efficient Data File Formats (Legacy)
To achieve flexibility, convenience, and performance stability in data handling, I provide default conversion methods for various formats (e.g., CSV/Excel) with a preference for:
- **JSONLines (.jsonl)**: The data foundation. Flexibly supports complex nested data types; ideal for stream processing and logging.
- **SQLite (.db)**: Embedded database with unified processing methods. A small, zero-configuration database that allows for consistent SQL-based data manipulation across different programming languages.
- **DuckDB (.duckdb)**: Embedded analytical database. High-performance analytics, representing one of the strategic directions I am progressively supporting.

### Functional Programming & Reliable Data Pipelines
Drawing from functional programming paradigms, I build composable processing workflows with traceable states:
- **Caching**: Supports automatic saving of intermediate results to avoid redundant computation and facilitate auditing of every experimental step.
- **Composability**: Modules are designed with decoupling in mind, allowing them to be assembled like building blocks to increase the reuse rate of core algorithms across different projects.
- **Extensibility**: While remaining lightweight, interfaces are reserved for specific research needs to avoid over-engineering.


## 🚀 Performance Evolution: From Pandas to Modern Architectures
> **Important Update:** As data scales grow, this project is progressively migrating from the traditional `Pandas/JSONL` stack to a high-performance computing architecture.

### Migration Motivations & Direction:
- **Compute Engine: From Pandas to Polars**
For large-scale experimental data, Pandas is often limited by single-core performance and memory overflows. By introducing **Polars**, we leverage its multi-threaded parallel engine and Lazy Evaluation to significantly reduce memory consumption and boost efficiency in million-row processing scenarios.
- **Memory Standard: Based on Apache Arrow**
Adopting **Arrow** as the unified standard for in-memory data eliminates serialization/deserialization overhead between different tools, enabling "zero-copy" integration with high-performance backends like DuckDB.
- **Storage Optimization: Parquet & Avro**
  - **Parquet**: For analytical tasks (OLAP), utilizing columnar storage and high compression ratios to drastically reduce disk I/O during scientific computing.
  - **Avro**: For streaming data or scenarios with frequent schema changes, ensuring robust data structure integrity.


## 📂 Core Modules Overview
To help you quickly locate the required functionality, the table below summarizes the main capabilities of this toolkit:

| Task | Core Module | Key Problem Solved | Core Tech Stack |
| --- | --- | --- | --- |
| **Data Processing** | Data Processing | I/O acceleration, async cleaning, feature engineering | Polars / Arrow |
| **Statistical Analysis** | Statistical Analysis | Descriptive stats, hypothesis testing, basic regression | statsmodels / scipy |
| **Machine Learning** | Machine Learning | Unsupervised learning, model evaluation, preprocessing pipelines | scikit-learn |
| **Text Analysis** | Text Analysis | Interpretable NLP, text vectorization, semantic clustering | NLTK / Scikit-learn |
| **Quick Viz** | Quick Visualization | Interactive exploration, **academic-standard plotting** | Plotly |


### 🔍 Module Details
#### 🛠️ Data Processing
Focuses on I/O optimization, quality assurance, and structural transformation.
- **Data Acceleration**: Accelerates I/O-intensive and compute-intensive tasks via asynchronous programming and multi-threading.
- **Data Cleaning**: Includes missing value handling, outlier detection, and strict data type validation.
- **Feature Engineering**: Plug-and-play transformation methods such as normalization and One-Hot encoding.

#### 📊 Statistical Analysis
Based on statistical principles to quickly verify data patterns and guide modeling directions.
- **Descriptive Stats**: Rapidly inspect distributions and correlations.
- **Hypothesis Testing**: Provides both parametric and non-parametric testing tools.
- **Regression Models**: General-purpose regression tools for quick benchmarking.

#### 🤖 Machine Learning
Focuses on general preprocessing and model observation.
- **Unsupervised Learning**: Used for data clustering, dimensionality reduction, and anomaly detection.
- **Model Evaluation**: Provides multi-dimensional metric evaluation and cross-validation tools.

#### 📝 Text Analysis
Aimed at highly interpretable, non-deep learning tasks.
- **Text Computing**: Calculation methods based on rules and statistics.
- **Text Visualization**: Word cloud generation, topic model display, and semantic clustering visualization.

*Note: For high-performance NLP tasks, please refer to my [Deep-Learning-Toolkit](https://github.com/yuliu625/Yu-Deep-Learning-Toolkit).*

#### 📈 Quick Visualization
Built on libraries like `Plotly` to balance "interactivity" with "publication quality."
- **Data Explore**: Pre-set methods for viewing data distributions and relationships.
- **Data Report**: **Academic Paper Configurations**. Summarizes color schemes, fonts, and layout standards commonly used in top-tier journals for one-click plotting.

## 🔗 Related Toolkits
This repository is part of my personal research toolchain. You can use it alongside the following:
- **[RAG-Toolkit](https://github.com/yuliu625/Yu-RAG-Toolkit)**: Core retrieval-augmented generation tools.
- **[Agent-Development-Toolkit](https://github.com/yuliu625/Yu-Agent-Development-Toolkit)**: Focused on LLM Agent logic construction.
- **[Deep-Learning-Toolkit](https://github.com/yuliu625/Yu-Deep-Learning-Toolkit)**: A foundation for general deep learning tasks.
- **[Data-Science-Toolkit](https://github.com/yuliu625/Yu-Data-Science-Toolkit)**: Data science and preprocessing utilities.

