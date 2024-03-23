
# Word Autocomplete

This repository contains code for a word autocomplete application. The application takes a PDF file as input and builds an AVL tree, a BST (Binary Search Tree), and a simple list to store the unique words found in the document. It then allows users to enter a prefix and find all words in the chosen data structure that start with that prefix.


## Features

- Processes PDF documents to extract text content
- Builds an AVL tree, a BST, and a list to store unique words
- Provides autocomplete functionality for words with a given prefix
- Measures and compares the insertion and search time complexities of each data structure


## Usage

Clone the repository:

```bash
git clone https://github.com/anuaristico/AutoComplete.git
```

Install dependencies (if not already installed):

```bash
pip install streamlit pandas
```

Run the application:

```bash
streamlit run app.py
```
    
## Explanation of files

- avltree.py: Contains the implementation of the AVL tree and BST data structures and related functions.
- NLPprocess.py: Contains functions for preprocessing PDF documents and interacting with the data structures for insertion and search operations.
- index.py: The main application script using Streamlit to create the user interface and interact with the different data structures.
## Data Structures

The application utilizes three data structures to store and search for words:

- AVL Tree: A self-balancing binary search tree that offers efficient insertion and search operations with a guaranteed logarithmic time complexity in most cases.
- BST (Binary Search Tree): A standard binary search tree that also provides logarithmic search complexity but may become unbalanced for certain data sets, impacting performance.
- List: A simple linear data structure suitable for basic search operations but with linear time complexity, making it less efficient for large datasets.
## Performance Comparison

The application measures and compares the time complexities of inserting words into each data structure and searching for words with a given prefix. The results are displayed in a table to help users understand the trade-offs between different data structures.
## Authors

- Josué Anuar Costa de Medeiros [@anuaristico](https://github.com/anuaristico)


## Running the application

Vídeo

