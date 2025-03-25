import pandas as pd
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
import time

data = {
    "id": [1, 2, 3, 4, 5],
    "text": [
        "testing text",
        "This is the testing text.",
        "testing text is being tested.",
        "blabblablablbalblabla.",
        "blabolalba."
    ]
}

df =pd.DataFrame(data)
model = SentenceTransformer("all-MiniLM-L6-v2")  
df["embeddings"] = df["text"].apply(lambda x: model.encode(x).tolist())

PINCONE_API_KEY ="pcsk_2hvndA_9ZE3h1TaUU7zabsEQ6yZZqEjWrp5Qdwp3Nwt49mzKD19B2wNVxcppYqcFK84qQ6"
pc = Pinecone(api_key=PINCONE_API_KEY)

index_name = "text-embeddings"

if index_name not in [index.name for index in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=len(df["embeddings"][0]),  # Embedding dimensions
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)

batch_size = 100
vectors = []

for i, row in df.iterrows():
    vectors.append((str(row["id"]), row["embeddings"]))

    if len(vectors) >= batch_size or i == len(df) - 1:
        index.upsert(vectors)
        vectors = [] 
        time.sleep(1) 

sample_vectors = index.fetch(ids=[str(i) for i in range(1, 6)])  

print("Sample Embeddings from:")
for vector_id, values in sample_vectors['vectors'].items():
    print(f"ID: {vector_id}")
    print(f"Embedding Vector: {values['values'][:5]}") 
