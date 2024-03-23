import PyPDF2
import re
import nltk
import nltk.corpus
nltk.download('stopwords')


def convert_pdf_to_txt(pdf_file):
    """
    Converts a PDF file to TXT using the PyPDF2 module.

    Args:
      pdf_file: A file object containing the PDF file contents.

    Returns:
      The extracted text from the PDF file.
    """

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Extract text from all pages
    full_text = ''
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        full_text += page_text

    # Return the complete text from the PDF file
    return full_text


# Load Portuguese stop words
stop_words = set(nltk.corpus.stopwords.words('portuguese'))

# Text preprocessing function


def preprocess(text):
    # Convert text to lowercase
    lowercase_text = text.lower()

    # Remove punctuation and special characters
    punctuation_free_text = re.sub('[^\w\s]', '', lowercase_text)

    # Split text into words
    words = punctuation_free_text.split()

    # Remove stop words
    stopword_free_words = [word for word in words if word not in stop_words]

    # Return the list of preprocessed words
    return stopword_free_words


def preprocess_pdf_corpus(pdf_file):
    """
    Preprocesses a PDF corpus.

    Args:
      pdf_file: Path to the PDF file.

    Returns:
      A list of preprocessed words from the corpus.
    """

    converted_text = convert_pdf_to_txt(pdf_file)
    preprocessed_words = preprocess(converted_text)

    return preprocessed_words


def insert_unique_words(avl_tree, words):
    """Inserts unique words from a list of preprocessed words into the AVLTree."""
    unique_words = set(words)  # Remove duplicates
    for word in unique_words:
        avl_tree.add(word)


def insert_unique_words_bst(bst_tree, words):
    """Inserts unique words from a list of preprocessed words into the BST."""
    unique_words = set(words)  # Remove duplicates
    for word in unique_words:
        bst_tree.add(word)


def insert_unique_words_list(list, words):
    """Inserts unique words from a list of preprocessed words into the LIST."""
    unique_words = set(words)  # Remove duplicates
    for word in unique_words:
        list.append(word)


def find_words_with_prefix(avl_root, prefix):
    """Finds words in the AVLTree that start with the given prefix, stopping after finding the prefix.

    Args:
      avl_tree: The AVLTree to search.
      prefix: The prefix to search for.

    Returns:
      list: A list of words in the tree that start with the prefix.
    """

    words = []
    node = avl_root
    found_prefix = False
    while node:
        if found_prefix:
            # Stop searching if prefix is found and value of node and childs doesn't start with prefix
            if node.value.startswith(prefix):
                words.append(node.value)
                if node.left_child and node.left_child.value.startswith(prefix):
                    words.extend(find_words_with_prefix(
                        node.left_child, prefix))
                if node.right_child and node.right_child.value.startswith(prefix):
                    words.extend(find_words_with_prefix(
                        node.right_child, prefix))
                break
        else:
            # Start searching for prefix once found
            if node.value.startswith(prefix):
                found_prefix = True
            elif prefix < node.value:
                node = node.left_child
            else:
                node = node.right_child
    return words


def find_words_with_prefix_bst(bst_root, prefix):
    """Finds words in the unbalanced BST that start with the given prefix.

    Args:
        bst: The unbalanced BST to search.
        prefix: The prefix to search for.

    Returns:
        list: A list of words in the tree that start with the prefix.
    """

    words = []
    node = bst_root

    while node:
        if node.value.startswith(prefix):
            words.append(node.value)
        if node.left_child:
            words.extend(find_words_with_prefix_bst(node.left_child, prefix))
        if node.right_child:
            words.extend(find_words_with_prefix_bst(node.right_child, prefix))
        break

    return words


def find_words_with_prefix_list(list, prefix):
    """
    Encontra palavras em uma lista que começam com o prefixo dado.

    Args:
      words: A lista de palavras a serem pesquisadas. (The list of words to search.)
      prefix: O prefixo a ser pesquisado. (The prefix to search for.)

    Returns:
      list: Uma lista de palavras na lista que começam com o prefixo. (A list of words in the list that start with the prefix.)
    """

    matching_words = []
    for word in list:
        # Verifica se a palavra começa com o prefixo. (Checks if the word starts with the prefix.)
        if word.startswith(prefix):
            # Adiciona a palavra à lista de resultados. (Adds the word to the list of results.)
            matching_words.append(word)

    return matching_words
