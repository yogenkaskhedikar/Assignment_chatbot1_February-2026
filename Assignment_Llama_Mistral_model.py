{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOpLhawzpyWUu48m1LAul8Z",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/yogenkaskhedikar/Assignment_chatbot1_February-2026/blob/main/Assignment_Llama_Mistral_model.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Create an interactive chat loop, where we can converse with the Llama model."
      ],
      "metadata": {
        "id": "Xj8HbHJE2G4w"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install transformers torch accelerate\n",
        "!huggingface-cli login\n",
        "!huggingface-cli whoami\n",
        "from transformers import AutoTokenizer\n",
        "import transformers\n",
        "import torch\n",
        "\n",
        "model = \"meta-llama/Llama-2-7b-chat-hf\" # meta-llama/Llama-2-7b-hf\n",
        "\n",
        "tokenizer = AutoTokenizer.from_pretrained(model, use_auth_token=True)\n",
        "\n",
        "from transformers import pipeline\n",
        "\n",
        "llama_pipeline = pipeline(\n",
        "    \"text-generation\",  # LLM task\n",
        "    model=model,\n",
        "    torch_dtype=torch.float16,\n",
        "    device_map=\"auto\",\n",
        ")\n",
        "\n",
        "def get_llama_response(prompt: str) -> None:\n",
        "    \"\"\"\n",
        "    Generate a response from the Llama model.\n",
        "\n",
        "    Parameters:\n",
        "        prompt (str): The user's input/question for the model.\n",
        "\n",
        "    Returns:\n",
        "        None: Prints the model's response.\n",
        "    \"\"\"\n",
        "    sequences = llama_pipeline(\n",
        "        prompt,\n",
        "        do_sample=True,\n",
        "        top_k=10,\n",
        "        num_return_sequences=1,\n",
        "        eos_token_id=tokenizer.eos_token_id,\n",
        "        max_length=256,\n",
        "    )\n",
        "    print(\"Chatbot:\", sequences[0]['generated_text'])\n",
        "\n",
        "while True:\n",
        "    user_input = input(\"You: \")\n",
        "    if user_input.lower() in [\"bye\", \"quit\", \"exit\"]:\n",
        "        print(\"Chatbot: Goodbye!\")\n",
        "        break\n",
        "    get_llama_response(user_input)"
      ],
      "metadata": {
        "id": "QOKq-7e-2Yre"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}