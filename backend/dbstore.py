from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_postgres.vectorstores import PGVector
from core.config import Settings
# from upload import data

connection=f"postgresql+psycopg2://{Settings.POSTGRES_USER}:{Settings.POSTGRES_PASSWORD}@{Settings.POSTGRES_SERVER}:{Settings.POSTGRES_PORT}/{Settings.POSTGRES_DB}"
collection_name = "all_docs"
embeddings = HuggingFaceEmbeddings()

#creating a vector store
vectorstore = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
    )
 