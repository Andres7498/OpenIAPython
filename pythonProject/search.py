import os
import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone



def buscar():
    pinecone.init(api_key="e5364597-8f21-4855-a69f-13068ff2d8c2", environment="gcp-starter")
    embeddings = OpenAIEmbeddings(openai_api_key = "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")
    docsearch = Pinecone.from_existing_index("matrix1", embeddings)
    query = "Cuantos años de acreditación tiene ingeniería de industrial?"
    docs = docsearch.similarity_search(query)
    print(docs)

buscar()



[[]]

[]