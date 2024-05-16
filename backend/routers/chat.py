from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores.faiss import FAISS
embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base")
new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
docs = new_db.similarity_search("frontend requirements")
print(docs)