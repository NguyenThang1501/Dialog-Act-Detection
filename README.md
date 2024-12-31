---

# Dialog Act Detection

This project focuses on the task of dialog act detection using the MultiWOZ 2.2 dataset. The dataset has been split into three directories: dev, test, and train, and these are used directly for training, validation, and testing without further splitting.

## Dataset Preparation

The original MultiWOZ 2.2 dataset is extracted into two smaller datasets:

1. **Dataset for Dialog Act Detection**:
    - Extracted from the JSON files in the train, test, and dev directories and the `dialog_act.json` file.
    - Contains the following fields:
        - `Dialog_id`
        - `Turn_id`
        - `Speaker`
        - `Utterance`
        - `Dialog_act`
        - `span_info`

2. **Dataset for Slot and Value Detection**:
    - Based on `span_info` and `Utterance` extracted above, labels are assigned to the words in the sentence using BIO tagging.
    - Initially, BIO tags are assigned to each character using the `start` and `exclusive_end` values. Then, based on spaces, the tags are converted from characters to words.

## Methodology

### Dialog Act Detection

The study implements two approaches:

1. **Model with Input as the Current Utterance Only**:
    - The model uses only the current utterance for prediction.

2. **Model with Input as the Current Utterance and Context**:
    - The model uses the current utterance along with the preceding utterances in the conversation as context.

The output labels are transformed into a one-hot vector. For utterances with multiple labels, the corresponding positions in the vector are set to 1, while the remaining positions are 0.

Both approaches follow the same training procedure and model structure.

### Slot and Value Detection

The task of slot and value detection is framed as a BIO tagging problem. Once the BIO tags are assigned to each word in the sentence, the slots and their corresponding values can be easily identified.

- **Label Processing**:
    - The labels are converted from strings to numbers.
    - Padding is used to ensure all sequences are of equal length, meeting the input requirements of the model.

- **BIO Tag Identification**:
    - Using the positions of B and I tags, the slots and values in the sentence are identified.

## Directory Structure

- **DataProcessed**: Contains processed data files used for training and evaluation.
- **PreprocessData**: Contains scripts for data preprocessing.
- **Model**: Contains code for building and training the models.
- **FinalResult.ipynb**: Notebook combining the results of the two models discussed above.

## Training

The model training process was conducted on Kaggle to leverage their computational resources.

## Evaluation Metrics

The performance of the models is evaluated using accuracy, precision, recall, and F1-score metrics.

## Conclusion

The models perform well overall, particularly for labels with a large number of samples. However, improvements can be made for labels with fewer samples by collecting more data and applying data balancing techniques.

---

This README file provides a comprehensive overview of the project, including dataset preparation, methodology, directory structure, training, and evaluation metrics.
