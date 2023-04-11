
# This script builds LLM index from GitHub repository.
# You need to install nest_asyncio, httpx and llama by pip before running this script.
import nest_asyncio
nest_asyncio.apply()

import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index import GPTSimpleVectorIndex, GithubRepositoryReader
import os

# Set GITHUB_TOKEN environment variable to your GitHub token.
github_token = os.environ.get("GITHUB_TOKEN")
owner = "fjchen7"
repo = "ckb-llama-index-source"
branch = "main"

documents = GithubRepositoryReader(
    github_token=github_token,
    owner=owner,
    repo=repo,
    use_parser=False,
    verbose=False,
).load_data(branch=branch)

index = GPTSimpleVectorIndex.from_documents(documents)
