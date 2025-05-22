from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain_community.document_loaders import UnstructuredPowerPointLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_postgres.vectorstores import PGVector
from core.config import Settings
# from dbstore import vectorstore
from langchain_text_splitters import CharacterTextSplitter

def upload_user_file(file):
    extension = file.split('.')[-1]
   
    # Classifying files
    if extension == 'pdf':
        loader = PyPDFLoader(file)
    elif extension in ['doc', 'docx']:
        loader = Docx2txtLoader(file)
    elif extension in ['xls', 'xlsx']:
        loader = UnstructuredExcelLoader(file)
    elif extension == 'csv':
        loader = CSVLoader(file)
    elif extension in ['ppt','pptx']:
        loader = UnstructuredPowerPointLoader(file)
    else:
        return 'Unknown type'
   
    # Loading and Dividing into chunks
    document = loader.load()
    data= CharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200).split_documents(document)
    
    connection=f"postgresql+psycopg2://{Settings.POSTGRES_USER}:{Settings.POSTGRES_PASSWORD}@{Settings.POSTGRES_SERVER}:{Settings.POSTGRES_PORT}/{Settings.POSTGRES_DB}"
    collection_name = "all_docs"
    
    embeddings = HuggingFaceEmbeddings()

    vectorstore = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
    )
 
    vectorstore.add_documents(data)