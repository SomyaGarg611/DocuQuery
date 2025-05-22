from dbstore import vectorstore
from langchain.tools.retriever import create_retriever_tool
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import Tool
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
import os
from langchain_groq import ChatGroq
from langchain_community.utilities.sql_database import SQLDatabase
from core.config import Settings
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

GROQ_LLM = ChatGroq(
            model="llama3-70b-8192",
            temperature=0,
        )

os.environ["SERPAPI_API_KEY"] = Settings.SERP_API_KEY 

#retrieving from the vector store
retriever = vectorstore.as_retriever()
retriever_tool = create_retriever_tool(
    retriever,
    "document_search",
    "Search for information about document. For any questions about the user, you must use this tool!",
)

#making serpapi tool
search = SerpAPIWrapper()
serpapi_tool = Tool(
    name="serpapi",
    description="A search tool. Use this if you want to see the output from the internet",
    func=search.run,
)

connection=f"postgresql://{Settings.POSTGRES_USER}:{Settings.POSTGRES_PASSWORD}@{Settings.POSTGRES_SERVER}:{Settings.POSTGRES_PORT}/lego"

db = SQLDatabase.from_uri(connection)

toolkit = SQLDatabaseToolkit(db=db, llm=GROQ_LLM)
context = toolkit.get_context()
sqltools = toolkit.get_tools()

tools = [retriever_tool, serpapi_tool]
tools.extend(sqltools)

#Chat_history
memory=ConversationBufferWindowMemory(
    memory_key="chat_history",
    k=5,
    return_messages=True
)

from langchain import hub

#mMaking prompt
prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant. Make sure to use the answer tool for information, and only if no suitable answers are found, then refer to the present chat context to search for answer. Please pass the user specified format as a parameter into the tool, only when the tool is invoked. Please do not reveal the previous chats in this response. Please only answer the question given by the user using the tool, and nothing else.",
            ),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
 
        ]
    )

agent = create_tool_calling_agent(GROQ_LLM, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, memory=memory)

# input_user = input("Ask your query:")
# agent_executor.invoke({"input" : input_user})

