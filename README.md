# Data Science Toolkit

## Overview
This is a lean **Data Science Toolkit** specifically designed for developers and data scientists who prioritize efficiency, code reusability, and high-quality data insights.

I have integrated core methodologies and **plug-and-play code modules** for essential data science tasks, ranging from data preprocessing and statistical analysis to foundational machine learning and visualization.

My core goal is to build a **lightweight, flexible, and highly reusable toolbox** that can tackle complex data tasks quickly and efficiently, allowing you to focus on insights rather than repetitive configuration.


## Core Design Philosophy: Reusability and Reliability
Based on efficient workflows summarized from extensive data practice, I adhere to the following two core principles to ensure the toolkit's reliability and scalability:

### Standardized and Efficient Data File Formats
To achieve flexibility, convenience, and stable performance in data processing, I prioritize and provide default conversion methods to and from other formats (like CSV/Excel):
- **JSONLines (.jsonl):** The data foundation. Flexibly supports various complex nested data types, convenient for stream processing and log storage.
- **SQLite (.db):** Embedded database. Provides a unified handling method. It's a small, zero-configuration database, making it easy to process data using SQL across different programming languages.
- **DUCKDB (.duckdb):** Embedded analytical database. A direction I am progressively supporting for high-performance analysis.

### Functional Programming and Reliable Data Pipeline
Our data processing flow is inspired by functional programming to build data processing pipelines that are **composable, cacheable, and easily extendable**:
- **Cacheable:** Allows saving intermediate results, which not only speeds up repeated computations but also facilitates debugging and inspecting the output of each step.
- **Composable:** Different processing modules can be freely combined like building blocks, achieving high code reuse and flexible workflow construction.
- **Easily Extendable:** While avoiding over-engineering, necessary space is reserved for future expansion based on specific needs.


## Key Content Modules
This toolkit includes the following core modules. All functions are designed as single files or concise classes, allowing for quick insertion into specific projects. Functionality is continuously being updated. Please refer to the detailed documentation and source code for specific methods.

### Data Processing
Focuses on optimizing data I/O, quality assurance, and structural transformation.
- **Data Acceleration:** General data processing acceleration methods. Speeds up I/O-intensive and compute-intensive tasks through asynchronous programming and multithreading.
- **Data Cleaning:** Data cleaning and quality management. Includes handling missing values, outlier detection and treatment, and data type validation and conversion.
- **Feature Engineering:** Feature engineering processing methods. Includes data imputation, standardization, one-hot encoding, etc.

### Statistical Analysis
Based on libraries like `statsmodel`, this module enables quick execution of common statistical and econometric analyses and preliminary tests to guide subsequent modeling directions.
- **Descriptive Stats:** Descriptive statistical methods. Quickly view data shape, distribution, and correlation.
- **Hypothesis Testing:** Common hypothesis testing methods. Provides tools for parametric and non-parametric tests.
- **Regression Models:** Tools for basic, general regression analysis methods.

*Note: This module provides basic, general-purpose tools. Comprehensive regression analysis often requires specific data handling and model construction.*

### Machine Learning
Primarily based on `sklearn`, this module focuses on general data preprocessing, observation of data shape, and model evaluation.
- **Unsupervised Learning:** Unsupervised learning methods. Used for data clustering, dimensionality reduction, and anomaly detection.
- **Model Evaluation:** Model evaluation metrics and cross-validation tools.

*Note: This module emphasizes general data preprocessing and analysis. For complex supervised learning tasks, a better approach may be to build a specialized data pipeline or use deep learning models.*

### Text Analysis
Supports non-deep-learning NLP tasks, primarily used for high-interpretability text analysis and visualization of text data results.
- **Text Preprocessing:** Text preprocessing. Includes tokenization, sentence splitting, standardization, and text vectorization.
- **Text Computing:** Text computation. Includes rule-based, statistical-learning-based, and foundational machine-learning-based computation methods.
- **Text Visualization:** Text result visualization. Includes word cloud generation, topic model result display, text semantic clustering display, etc.

*Note: For high-performance and high-accuracy text tasks, the current mainstream approach is based on deep learning, especially LLMs. You may check my other related repositories.*

### Quick Visualization
Built upon libraries like Plotly, this module is used to stably and efficiently generate high-quality, interactive visualizations.
- **Data Explore:** Quick exploratory visualization. Presets various methods to view data shape, distribution, and interrelationships.
- **Data Report:** Academic paper configuration. Summarizes common visualization color schemes, fonts, and layout configurations used in high-quality academic papers.


## More of My Projects
If you are interested in similar tasks, you are welcome to check out my other repositories focused on specific domains:
- [**Deep-Learning-Toolkit**](https://github.com/yuliu625/Yu-Deep-Learning-Toolkit): A general toolkit for deep learning tasks.
- [**Agent-Development-Toolkit**](https://github.com/yuliu625/Yu-Agent-Development-Toolkit): A toolkit focused on building LLMs and Agents.

