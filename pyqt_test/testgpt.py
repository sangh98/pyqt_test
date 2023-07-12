import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="##### Fix bugs in the below function\n"
           "\n"
           "### Buggy Python\n"
           "import Random\n"
           "a = random.randint(1,12)\n"
           "b = random.randint(1,12)\n"
           "for i in range(10):\n"
           "    question = \"What is \"+a+\" x \"+b+\"? \"\n"
           "    answer = input(question)\n"
           "    if answer = a*b\n"
           "        print (Well done!)\n"
           "    else:\n"
           "        print(\"No.\")\n"
           "    \n"
           "### Fixed Python",
    temperature=0,  #다양성
    max_tokens=3000, #문장 길이
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["###"]
)
print(response)