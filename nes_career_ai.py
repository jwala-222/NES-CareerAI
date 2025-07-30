import os
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors
from collections import Counter

maindata="karrierewege.csv"

if os.path.exists(maindata):
    print("Found main database , loading from file...") 
    data = pd.read_csv(maindata)
    data = data[["skills", "preferredLabel_en"]].dropna()

    model_name = 'paraphrase-MiniLM-L6-v2'
    converter = SentenceTransformer(model_name)

    embedding_file = "convertedskills.npy"

    if os.path.exists(embedding_file):
        print("Found cached embeddings, loading from file...") 
        convertedskills = np.load(embedding_file)
        nn_model = NearestNeighbors(n_neighbors=10, metric='cosine')
        nn_model.fit(convertedskills)


        def top3(skillinput):
        input_vector = converter.encode([skillinput])
        distance, indices = nn_model.kneighbors(input_vector)
    
        raw_predictions = data.iloc[indices[0]]["preferredLabel_en"].values
        counter = Counter(raw_predictions)

        top_unique = [out for out, _ in counter.most_common(3)]
        print(f"\nSkills: {skillinput}")
        
        for i, rec in enumerate(top_unique, 1):
            print(f"Prediction {i}: {rec}")

        while True:
            usrinput = input("Enter your skill (type end to exit ): ")

            if usrinput.lower()=='end':
                break
            else:
                top3(usrinput)
    
    else:
        print(" No cache found, please visit https://drive.google.com/file/d/1s48kuUCi3usaXTMns8kdvFDouvnOiPC-/view?usp=sharing and download the file.")
        print("/place the file in the same folder as the current project is saved in")
    
else:
    print(" No cache found, please visit https://drive.google.com/file/d/1s48kuUCi3usaXTMns8kdvFDouvnOiPC-/view?usp=sharing and download the file.")
    print("/place the file in the same folder as the current project is saved in")


