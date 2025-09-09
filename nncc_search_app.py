
import streamlit as st
import fitz  # PyMuPDF

# Load and index the PDF document
def load_pdf(file_path):
    doc = fitz.open(file_path)
    pages = []
    for page_num in range(len(doc)):
        text = doc.load_page(page_num).get_text()
        pages.append((page_num + 1, text))
    return pages

# Search for keyword in the document
def search_keyword(pages, keyword):
    results = []
    for page_num, text in pages:
        if keyword.lower() in text.lower():
            snippet = text.strip().replace('\n', ' ')
            results.append((page_num, snippet))
    return results

# Load the PDF content
pdf_path = "NNCC serivice and training.pdf"
pages = load_pdf(pdf_path)

# Streamlit App UI
st.title("NNCC Document Search")
st.write("Enter a keyword to search the NNCC service and training document:")

# Text input for keyword
keyword = st.text_input("Keyword")

# Display search results
if keyword:
    results = search_keyword(pages, keyword)
    if results:
        st.subheader(f"Search Results for '{keyword}':")
        for page_num, snippet in results:
            st.markdown(f"**Page {page_num}:** {snippet[:500]}...")
    else:
        st.warning("No results found.")
