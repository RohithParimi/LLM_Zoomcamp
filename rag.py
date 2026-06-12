INSTRUCTIONS='''
Role: You're a teaching assistant need to answer the questions of the students from the given context
And please don't enterntain or provide response for the questions which are out of context.

Expected_Outcome: A clear and consice answer which needs to self explonatory. And ask the user if there other areas
that need to be explored. And tell the user you can find the answer that you are searching for in the lesson
please mention the associated filename also
'''

PROMPT_TEMPLATE='''
QUESTION: {question}

CONTEXT:
{context}
'''.strip()

class RAGBase:
    def __init__(self,
                 index,
                 llm_client,
                 instructions=INSTRUCTIONS,
                 prompt_template=PROMPT_TEMPLATE,
                 model='gpt-5.4-mini'):
        
        self.index=index
        self.llm_client=llm_client
        self.instructions=instructions
        self.prompt_template=prompt_template
        self.model=model
        self.response=None
    
    def search(self,query,num_results=5):
        return self.index.search(
            query,
            num_results=num_results
            )
    
    def build_context(self,serach_results):
        lines=[]

        for doc in serach_results:
            lines.append(f"filename:{doc["filename"]}")
            lines.append(f"content:{doc["content"]}")
            lines.append('')
        
        return '\n'.join(lines).strip()
    
    def build_prompt(self,query,search_results):
        context=self.build_context(search_results)
        return self.prompt_template.format(
            question=query,
            context=context
        )
    
    def llm(self,prompt):
        input_messgaes=[
            {'role':'developer','content':self.instructions},
            {'role':'user','content':prompt}
        ]

        self.response=self.llm_client.responses.create(
            model=self.model,
            input=input_messgaes
        )

        return self.response.output_text.strip()
    
    def rag(self,query):
        search_results=self.search(query)
        prompt=self.build_prompt(query,search_results)
        answer=self.llm(prompt)
        input_tokens=self.response.usage.input_tokens
        output_tokens=self.response.usage.output_tokens
        result=(answer,input_tokens,output_tokens)
        
        return (
            f"Answer: {answer}\n"
            f"Input_Tokens: {input_tokens}\n"
            f"Output_Tokens: {output_tokens}"
        )
