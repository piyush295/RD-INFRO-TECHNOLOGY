# Phishing URL Detection

This project aims to build a system for detecting phishing websites using Natural Language Processing (NLP) and classification models. The system leverages text analysis and feature extraction techniques to classify URLs as phishing or legitimate.

## Project Structure

- `src/`: Contains the source code for data preprocessing, feature extraction, model training, evaluation, and utility functions.
  - `data_preprocessing.py`: Functions for cleaning and preprocessing raw data.
  - `feature_extraction.py`: Implements feature extraction techniques like TF-IDF and word embeddings.
  - `model_training.py`: Responsible for training classification models.
  - `model_evaluation.py`: Contains functions to evaluate model performance.
  - `utils.py`: Utility functions for loading data, saving models, and visualizing results.

- `data/`: Directory for datasets.
  - `raw/`: Stores the raw dataset.
  - `processed/`: Stores the processed dataset after preprocessing and feature extraction.

- `models/`: Directory for saving trained models.

- `notebooks/`: Contains Jupyter notebooks for exploratory data analysis.
  - `exploratory_analysis.ipynb`: Used for visualizing data distributions and understanding the dataset.

- `requirements.txt`: Lists the dependencies required for the project.

- `.gitignore`: Specifies files and directories to be ignored by version control.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd phishing-url-detection
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Prepare the dataset by placing the raw data in the `data/raw/` directory.

4. Run the preprocessing script to clean and preprocess the data:
   ```
   python src/data_preprocessing.py
   ```

5. Extract features from the processed data:
   ```
   python src/feature_extraction.py
   ```

6. Train the classification models:
   ```
   python src/model_training.py
   ```

7. Evaluate the trained models:
   ```
   python src/model_evaluation.py
   ```

## Usage Examples

- To preprocess data, run the `data_preprocessing.py` script.
- Use the `feature_extraction.py` script to convert text data into numerical features.
- Train models using the `model_training.py` script and evaluate their performance with `model_evaluation.py`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.