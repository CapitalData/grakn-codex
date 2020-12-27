import logging
import pandas as pd
from codex import CodexKg 


#Load csv data
df = pd.read_csv("sample_data/tech_companies.csv")

#Make new codex object
codexkg = CodexKg()

#Create new keyspace
codexkg.create_db("tech_example")

#Load data into Grakn
codexkg.create_entity(df, "Company", entity_key="name")

# Find Company that has a name equal to Google
ans = codexkg.find(
        concept="Company",
        concept_attrs=["name"],
        concept_conds=["equals"],
        concept_values=["Google"],
)

#Display data as a DataFrame
logging.info(ans)

# {'Company':      name  budget
#				0  Google  999.99}