import sys

# log_file = open("errors.txt", "w")
# sys.stderr = log_file


# LLMs
from swarms.models.anthropic import Anthropic
from swarms.models.petals import Petals
from swarms.models.mistral import Mistral
from swarms.models.openai_models import OpenAIChat, AzureOpenAI, OpenAI
from swarms.models.zephyr import Zephyr
from swarms.models.biogpt import BioGPT
from swarms.models.huggingface import HuggingfaceLLM
from swarms.models.wizard_storytelling import WizardLLMStoryTeller
from swarms.models.mpt import MPT7B

# MultiModal Models
from swarms.models.idefics import Idefics  # noqa: E402

# from swarms.models.kosmos_two import Kosmos  # noqa: E402
from swarms.models.vilt import Vilt  # noqa: E402
from swarms.models.nougat import Nougat  # noqa: E402
from swarms.models.layoutlm_document_qa import LayoutLMDocumentQA  # noqa: E402

# from swarms.models.gpt4v import GPT4Vision
# from swarms.models.dalle3 import Dalle3
# from swarms.models.distilled_whisperx import DistilWhisperModel # noqa: E402

__all__ = [
    "Anthropic",
    "Petals",
    "Mistral",
    "OpenAI",
    "AzureOpenAI",
    "OpenAIChat",
    "Zephyr",
    "Idefics",
    # "Kosmos",
    "Vilt",
    "Nougat",
    "LayoutLMDocumentQA",
    "BioGPT",
    "HuggingfaceLLM",
    "MPT7B",
    "WizardLLMStoryTeller",
    # "GPT4Vision",
    # "Dalle3",
]
