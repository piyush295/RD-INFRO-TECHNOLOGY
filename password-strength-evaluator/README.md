# Password Strength Evaluator

## Overview
The Password Strength Evaluator is a project designed to assess the strength of passwords using both rule-based and machine learning approaches. It provides a comprehensive framework for evaluating password security, helping users create stronger passwords.

## Project Structure
```
password-strength-evaluator
├── src
│   ├── rule_based_evaluator.py      # Implements rule-based password strength evaluation
│   ├── ml_based_evaluator.py         # Utilizes machine learning for password strength assessment
│   ├── data_preprocessing.py         # Contains functions for data cleaning and preparation
│   ├── model_training.py              # Handles training and saving of machine learning models
│   └── utils.py                      # Provides utility functions for the project
├── data
│   ├── raw                           # Directory for raw data files
│   └── processed                     # Directory for processed data files
├── notebooks
│   └── exploratory_analysis.ipynb    # Jupyter notebook for exploratory data analysis
├── models                            # Directory for storing trained machine learning models
├── requirements.txt                  # Lists project dependencies
└── README.md                         # Project documentation
```

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd password-strength-evaluator
pip install -r requirements.txt
```

## Usage
1. **Rule-Based Evaluation**: Use the `RuleBasedEvaluator` class from `src/rule_based_evaluator.py` to evaluate passwords based on predefined rules.
2. **Machine Learning Evaluation**: Utilize the `MLBasedEvaluator` class from `src/ml_based_evaluator.py` to assess password strength using a trained machine learning model.
3. **Data Preprocessing**: Use functions from `src/data_preprocessing.py` to clean and prepare your dataset.
4. **Model Training**: Train your models using the functions in `src/model_training.py`.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.