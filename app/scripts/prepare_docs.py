# # prepare_docs.py
# import pandas as pd
# from langchain_core.documents import Document
# import pickle

# csv_path = "C:/Users/Administrator/Downloads/code/data/raw/un-general-debates.csv"

# df = pd.read_csv(csv_path).head(5)
# documents = []
# for _, row in df.iterrows():
#     page_content = (
#         f"Session: {row['session']}\n"
#         f"Year: {row['year']}\n"
#         f"Country: {row['country']}\n"
#         f"Speech:\n{str(row['text']).strip()}"
#     )
#     metadata = {
#         "session": row["session"],
#         "year": row["year"],
#         "country": row["country"]
#     }
#     documents.append(Document(page_content=page_content, metadata=metadata))

# # ✅ Lưu documents ra file
# with open("./data/processed/documents.pkl", "wb") as f:
#     pickle.dump(documents, f)

# print("Documents saved.")
