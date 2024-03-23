import avltree
import NLPprocess as nlp
import streamlit as st
import time
import pandas as pd

st.title("Autocompletador de palavras")

arquivo_pdf = st.file_uploader("Selecione um arquivo PDF para ser o corpus:")

if arquivo_pdf:
    texto_processado = nlp.preprocess_pdf_corpus(arquivo_pdf)
    arvore = avltree.AVLTree()
    bst = avltree.BST()
    lista = []
    inicio_avl = time.time()
    nlp.insert_unique_words(arvore, texto_processado)
    fim_avl = time.time()
    tempo_execucao_avl = fim_avl - inicio_avl
    inicio_bst = time.time()
    nlp.insert_unique_words_bst(bst, texto_processado)
    fim_bst = time.time()
    tempo_execucao_bst = fim_bst - inicio_bst
    inicio_list = time.time()
    nlp.insert_unique_words_list(lista, texto_processado)
    fim_list = time.time()
    tempo_execucao_list = fim_list - inicio_list
    prefixo = st.text_input("Digite um prefixo:")
    prefixo = prefixo.lower()
    if prefixo:
        inicio_avl2 = time.time()
        palavras_com_prefixo = nlp.find_words_with_prefix(
            arvore.root, prefixo)
        fim_avl2 = time.time()
        tempo_execucao_avl2 = fim_avl2 - inicio_avl2
        inicio_bst2 = time.time()
        palavras_com_prefixo_bst = nlp.find_words_with_prefix_bst(
            bst.root, prefixo)
        fim_bst2 = time.time()
        tempo_execucao_bst2 = fim_bst2 - inicio_bst2
        inicio_list2 = time.time()
        palavras_com_prefixo_list = nlp.find_words_with_prefix_list(
            lista, prefixo)
        fim_list2 = time.time()
        tempo_execucao_list2 = fim_list2 - inicio_list2
        st.write("Palavras encontradas (AVL):")
        st.text(palavras_com_prefixo)
        st.write("Palavras encontradas (BST):")
        st.text(palavras_com_prefixo_bst)
        st.write("Palavras encontradas (LIST):")
        st.text(palavras_com_prefixo_list)
        df = pd.DataFrame({"Estrutura": ["AVL", "BST", "LISTA"], "Tempo de inserção": [tempo_execucao_avl, tempo_execucao_bst,
                          tempo_execucao_list], "Tempo de busca": [tempo_execucao_avl2, tempo_execucao_bst2, tempo_execucao_list2]})
        st.dataframe(df, column_config={
                     "Tempo de inserção": {"format": "{:.4f}"}, "Tempo de busca": {"format": "{:.4f}"}}, hide_index=True)
