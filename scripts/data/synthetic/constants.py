# Copyright (c) 2024, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

"""
Add a new task (required arguments):

TASK_NAME: {
    'tokens_to_generate': how many tokens we want to generate.
    'template': the template with at least {context} and {query}.
}
"""

TYPE_NEEDLE_EN_KO = {
    'numbers': '숫자',
    'words': '단어',
    'uuids': 'UUID',
}



TASKS = {
    'niah': {
        'tokens_to_generate': 128,
        # 'template': """Some special magic {type_needle_v} are hidden within the following text. Make sure to memorize it. I will quiz you about the {type_needle_v} afterwards.\n{context}\nWhat are all the special magic {type_needle_v} for {query} mentioned in the provided text?""",
        'template': """다음 텍스트에는 특별한 마법 {type_needle_v}가 숨겨져 있습니다. 반드시 기억해두세요. 나중에 {type_needle_v}에 대해 퀴즈를 내겠습니다.\n{context}\n제공된 텍스트에서 {query}에 대한 모든 특별한 마법 {type_needle_v}는 무엇입니까?""",
        # 'answer_prefix': """ T        11111111                    1he special magic {type_needle_v} for {query} mentioned in the provided text are""",
        'answer_prefix': """제공된 텍스트에서 언급된 {query}에 대한 특별한 마법 {type_needle_v}는"""
    },
    
    'variable_tracking': {
        'tokens_to_generate': 30,
        # 'template': """Memorize and track the chain(s) of variable assignment hidden in the following text.\n\n{context}\nQuestion: Find all variables that are assigned the value {query} in the text above.""",
        'template': """다음 텍스트에 숨겨진 변수 할당 체인(들)을 기억하고 추적하세요.\n\n{context}\n질문: 위의 텍스트에서 값 {query}이(가) 할당된 모든 변수를 찾으십시오.""",
        # 'answer_prefix': """ Answer: According to the chain(s) of variable assignment in the text above, {num_v} variables are assgined the value {query}, they are: """,
        'answer_prefix': """ 답변: 위의 텍스트에서 변수 할당 체인에 따르면, 값 {query}이(가) 할당된 변수는 {num_v}개이며, 다음과 같습니다: """
    },
    
    'common_words_extraction': {
        'tokens_to_generate': 120,
        # 'template': """Below is a numbered list of words. In these words, some appear more often than others. Memorize the ones that appear most often.\n{context}\nQuestion: What are the 10 most common words in the above list?""",
        'template': """아래에는 단어 목록이 번호가 매겨져 있습니다. 이 단어들 중 일부는 다른 단어보다 더 자주 나타납니다. 가장 자주 나타나는 단어들을 기억하세요.\n{context}\n질문: 위 목록에서 가장 일반적인 10개의 단어는 무엇입니까?""",
        # 'answer_prefix': """ Answer: The top 10 words that appear most often in the list are:""",
        'answer_prefix': """ 답변: 목록에서 가장 자주 나타나는 상위 10개 단어는 다음과 같습니다:"""
    },
    
    'freq_words_extraction' : {
        'tokens_to_generate': 50,
        # 'template': """Read the following coded text and track the frequency of each coded word. Find the three most frequently appeared coded words. {context}\nQuestion: Do not provide any explanation. Please ignore the dots '....'. What are the three most frequently appeared words in the above coded text?""",
        'template': """다음의 코드화된 텍스트를 읽고 각 코드화된 단어의 빈도를 추적하십시오. 가장 자주 나타나는 코드화된 단어 3개를 찾으십시오. {context}\n질문: 설명을 제공하지 마십시오. 점 '....'을 무시하십시오. 위의 코드화된 텍스트에서 가장 자주 나타나는 단어 3개는 무엇입니까?""",
        # 'answer_prefix': """ Answer: According to the coded text above, the three most frequently appeared words are:""",
        'answer_prefix': """ 답변: 위의 코드화된 텍스트에 따르면, 가장 자주 나타나는 단어 3개는 다음과 같습니다:"""
    },

    'qa': {
        'tokens_to_generate': 32, 
        # 'template': """Answer the question based on the given documents. Only give me the answer and do not output any other words.\n\nThe following are given documents.\n\n{context}\n\nAnswer the question based on the given documents. Only give me the answer and do not output any other words.\n\nQuestion: {query}""",
        'template': """주어진 문서를 기반으로 질문에 답하십시오. 답변만 제공하고 다른 단어는 출력하지 마십시오.\n\n다음은 주어진 문서입니다.\n\n{context}\n\n주어진 문서를 기반으로 질문에 답하십시오. 답변만 제공하고 다른 단어는 출력하지 마십시오.\n\n질문: {query}""",
        # 'answer_prefix': """ Answer:""",
        'answer_prefix': """ 답변:"""
    },
}