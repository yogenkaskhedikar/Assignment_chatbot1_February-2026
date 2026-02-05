{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "authorship_tag": "ABX9TyPFZM+1kg92Z0U3HEFxxFV8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/yogenkaskhedikar/Assignment_chatbot1_February-2026/blob/main/Interactive_chat.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "81d21d26"
      },
      "source": [
        "from openai import OpenAI\n",
        "\n",
        "\n",
        "# Initialize OpenAI client\n",
        "client = OpenAI(api_key=\"\")\n",
        "\n",
        "\n",
        "def chatbot():\n",
        "    system_prompt = \"You are a helpful assistant.\"\n",
        "\n",
        "\n",
        "    while True:\n",
        "        user_input = input(\"User: \")\n",
        "\n",
        "\n",
        "        if user_input.lower() == \"quit\":\n",
        "            break\n",
        "\n",
        "\n",
        "        response = client.responses.create(\n",
        "            model=\"gpt-5.2\",\n",
        "            input=[\n",
        "                {\"role\": \"system\", \"content\": system_prompt},\n",
        "                {\"role\": \"user\", \"content\": user_input}\n",
        "            ]\n",
        "        )\n",
        "\n",
        "\n",
        "        # Simplest & safest way to get text output\n",
        "        print(f\"Bot: {response.output_text}\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    print(\"Start chatting with the bot (type 'quit' to stop)!\")\n",
        "    chatbot()\n"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
