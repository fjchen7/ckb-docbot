from langchain.chat_models import ChatOpenAI

from llama_index import LLMPredictor, ServiceContext
# Use LLM gpt-3.5-turbo
llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, chunk_size_limit=3072)

from llama_index import GPTSimpleVectorIndex
index = GPTSimpleVectorIndex.load_from_disk("./index/everything.json", service_context=service_context)
