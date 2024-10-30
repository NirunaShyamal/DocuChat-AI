import streamlit as st
from document import make_temp_dir, remove_temp_dir, save_documents, load_documents

temp_dir="document/upload"



st.set_page_config(page_title="DocuChat AI: Your Intelligent Document Assistant", page_icon="📄", layout="wide")


uploaded_file=st.file_uploader("Upload your documents", type=["pdf", "docx", "txt"], accept_multiple_files=True)

if uploaded_file:
    with st.status(label="Uploading documents..", expanded=True):
        st.write("Make temporary directory..")
        temp_dir=make_temp_dir(temp_dir=temp_dir)
        
        st.write("Saving documents..")
        saved_paths=save_documents(documents=uploaded_file, temp_dir=temp_dir)
        
        st.write("Loading documents..")
        documents=load_documents(temp_dir=temp_dir)
        
        st.write("Removing temporary directory..")
        remove_temp_dir(temp_dir=temp_dir)
    
        st.write(len(documents), "documents uploaded")
    
        st.markdown(documents)