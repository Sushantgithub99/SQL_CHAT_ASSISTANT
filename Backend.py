## Packages
import pandas as pd
from openai import OpenAI
import sqlite3 as sql

## Database Schema.
schema = ''' 
Employees(ID INT PRIMARY KEY, Name TEXT, Department TEXT, Salary INT, Hire_Date TEXT)  
Departments (ID INT PRIMARY KEY, Name TEXT, Manager TEXT)
'''

def model_setup(api_key, system_query, human_query):
    client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key=api_key,
    )
    completion = client.chat.completions.create(
      model="deepseek/deepseek-r1:free",
      messages=[
        {"role": "system", "content": system_query},
        {"role": "user","content": human_query}
      ]
    )
    print(completion)

    choices = completion.choices
    if choices == None:
        response = "Error : Rate Limited Exceeded."
    else: 
        response = (choices[0].message.content)
    return response


## Retrieval of Data for the generated query
def execute_sql(sql_query):
    if not sql:
        return None, "No SQL generated."
    conn = sql.connect('"sql_chat_assistant//Database"')
    c = conn.cursor()
    try:
        c.execute(sql_query)
        results = c.fetchall()
        columns = [desc[0] for desc in c.description] if c.description else []
        return columns, results
    except sql.Error as e:
        return None, str(e)
    finally:
        conn.close()


# Method to retrieve llm query response.
def llm_query_response(api_key,model,prompt):

    ## Queries
    system_query = '''  
    You are an SQL expert. Convert the user query into an optimized SQLite query to retrieve the required data.  
    '''
    human_query = f''' 
    Table schema : {schema}
    Query: {prompt}  
    Respond in one line in the format: <<< your sql query >>>
    '''

    if model == 'deepseek/deepseek-r1:free':
        res = model_setup(api_key, system_query,human_query)
        if res == "Error : Rate Limited Exceeded.":
            generated_query = res
            print(generated_query)
            return generated_query
        print('deepseek/deepseek-r1:free:',res)


    # Code that retrieves the SQL query from the truncated response of the LLM output.
    indicator_1 = res.find('<')
    indicator_2 = res.find('>',indicator_1)
    truncated_response = res[indicator_1:indicator_2]
    print("############ TR ###############")
    print(truncated_response)
    print("############ TR ###############")

    start = truncated_response.find("SELECT")
    end = truncated_response.find(';',start)

    if start == -1:
        print('No query returned by LLM')
        return None

    # Final generated_query.
    generated_query = truncated_response[start:end]

    return generated_query


