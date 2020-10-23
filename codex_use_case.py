import logging
import pandas as pd
from codex import CodexKg

logging.basicConfig(
    format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO
)


# good use case can be smart tvs...
# they have lots of different content
# we want to use nlq to find certain content


# example entity_map


# entity_map = {}
# entity_map["Company"] = ["company","companies"]
# entity_map["Product"] = ["product","products"]

# attr_list = ["name","budget"]


# codex_actions_map = {}
# codex_actions_map["Find"] = ["find","get","show","list"]

# codex_action_keys = list(codex_actions_map.keys())


# cols = ["name","budget","produces"]


def search_for_data(codexkg):

    codexkg.find(
        concept="Company",
        attrs=["name"],
        conds=["equals"],
        values=["Google"],
    )

    codexkg.find(
        concept="Company",
        attrs=["name", "budget"],
        conds=["==", ">="],
        values=["Google", 100],
    )

    company = codexkg.concept("Company")

    codexkg.find(
        concept="Company",
        rel_action=["produces"],
        concept_rels=["Product"],
        concept_rel_attrs=["name"],
        concept_rel_conds=["equals"],
        concept_rel_values=["Google"],
    )

    codexkg.find(
        concept="Company",
        concept_attrs=["name"],
        concept_conds=["equals"],
        concept_values=["Google"],
        rel_action=["produces"],
        concept_rels=["Product"],
        concept_rel_attrs=["name"],
        concept_rel_conds=["equals"],
        concept_rel_values=["Google"],
    )

    codexkg.find(
        concept="Company",
        concept_attrs=["name"],
        concept_conds=["equals"],
        concept_values=["Google"],
        rel_action=["produces"],
        concept_rels=["Product"],
        with_rel_attrs=["note"],
        with_rel_conds=["contains"],
        with_rel_values=["bis"],
    )

    codexkg.find(
        concept="Company",
        concept_attrs=["name"],
        concept_conds=["equals"],
        concept_values=["Google"],
        rel_action=["produces"],
        concept_rels=["Product"],
        concept_rel_attrs=["name"],
        concept_rel_conds=["equals"],
        concept_rel_values=["Pixel"],
        with_rel_attrs=["note"],
        with_rel_conds=["contains"],
        with_rel_values=["bis"],
    )

    # codexkg.find(
    #     concept="Company",
    #     attrs=["name", "budget"],
    #     conds=["equals", "greater than"],
    #     values=["Google", 100],
    # )

    query_obj = Attr("name").eq("Google") & Attr("budget").gt("100")

    company.find(query_obj)

    KeyConditionExpression = Key("artist").eq("Arturus Ardvarkian") & Key("song").lt(
        "C"
    )

    codexkg.find(concept="Company", attrs=["name"], conds=["equals"], values=["Google"])

    # df[df.iloc["name"] == "Google"]


def main():

    logging.info("This will highlight how we can use codex to create knowledge graphs")
    codexkg = CodexKg()

    codexkg.create_db("tech_example")

    # loading_data(codexkg)
    # gen_qs(codexkg)
    # search_data(codexkg)

    # print(codexkg.lookup_map["Find"]["Company"]["name"])

    # Find Companies that have a name that Equals CODEX_REPLACE.
    # Find Companies named Google.

    # Find Companies with a budget less than 500.
    # doc = nlp("Find companies that have a name equal to Google")

    # find coffee open - failed
    # find coffee shops that are open - worked

    # find companies that have a name equal to Google

    # look for Companies that have a budget equal to 100."
    # look for this in sentence

    # VERB - action we are doing
    # NOUN - entity we want
    # NOUN - attribute we want
    # ADJ/VERB  - Condition
    # NUM - Value of condtion


def gen_qs(codexkg):

    logging.info("Well here comes the pain")
    codexkg.generate_queries("Company", "Entity", True)
    # codexkg.generate_queries("Product","Entity",True)


def search_data(codexkg):

    # codexkg.gen_queries() - > create all queries
    # codexkg.show_queries() - > list of all queries
    # codexkg.nlquery("Find Companies that have a name that contains Google.")

    df = pd.read_csv("sample_data/tech_companies.csv")
    ans = df.loc[df["name"] == "Google"]

    logging.info(ans)


def loading_data(codexkg):

    # load data from csv
    tech_companies = pd.read_csv("sample_data/tech_companies.csv")
    tech_products = pd.read_csv("sample_data/tech_products.csv")

    # create entites
    codexkg.create_entity(tech_companies, "Company", "name")
    codexkg.create_entity(tech_products, "Product", "name")

    # codexkg.delete_db("tech_example") # Delete keyspace


if __name__ == "__main__":
    main()
