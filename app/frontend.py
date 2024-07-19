import streamlit as st
import requests

API_URL = "http://localhost:5000"

def get_books():
    response = requests.get(f"{API_URL}/books/")
    return response.json()

def create_book(title, author, category):
    book = {
        "title": title,
        "author": author,
        "category": category
    }
    response = requests.post(f"{API_URL}/books/", json=book)
    return response.json()

st.title("Sistema de Gerenciamento de Biblioteca Interna")

menu = ["Listar Livros", "Adicionar Livro"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Listar Livros":
    st.subheader("Lista de Livros")
    books = get_books()
    for book in books:
        st.write(f"**Título:** {book['title']}")
        st.write(f"**Autor:** {book['author']}")
        st.write(f"**Categoria:** {book['category']}")
        st.write(f"**Disponível:** {'Sim' if book['is_available'] else 'Não'}")
        st.write("---")

elif choice == "Adicionar Livro":
    st.subheader("Adicionar Novo Livro")
    title = st.text_input("Título")
    author = st.text_input("Autor")
    category = st.text_input("Categoria")
    if st.button("Adicionar"):
        create_book(title, author, category)
        st.success("Livro adicionado com sucesso!")
