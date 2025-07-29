# 📦 Requirements

system requirements -
    ram-16GB (Recommended) ///or 8(dedicated)+8(swap) (only for linux users)
    cpu above i5-11th gen (no graphics card needed the integrated graphics is fine)

# 🐍 Python Libraries

Install the required Python libraries with:
pip install -r requirements.txt
requirements.txt includes:

    flask – for building the web interface
    numpy – for working with numerical data
    pandas – for handling datasets
    scikit-learn – for using K-Nearest Neighbors
    sentence-transformers – for vectorizing input text
    joblib – for loading the trained models

# 🗃️ Required Data Files

The model relies on a few essential data files. Due to size limits, these aren’t hosted directly on GitHub. Download them from the links below:

File Name	
convertedskills.npy	Precompiled sentence embeddings of the ESCO-based Karrierewege dataset (≈4 GB)	
Download link - https://drive.google.com/file/d/1s48kuUCi3usaXTMns8kdvFDouvnOiPC-/view?usp=sharing

career_data.csv	Cleaned and structured subset of the Karrierewege dataset	(also ≈4 GB)
Download link - https://drive.google.com/file/d/1CRKWgIMGKn_i6SX5pOBj0VNKpqsi20vd/view?usp=sharing

knn_model.joblib Serialized KNN model trained on the embeddings	
Download link -would be updated once the web part is finished


# 🧪 How to Use

    Download the above files and place them in the project directory.
    Update file paths in the Python script if needed.
    Run your main script:

python nes_career_ai.py


# 🧠 Background Note

The core dataset, called Karrierewege, is a German word that literally translates to career paths. It’s based on the official ESCO occupations dataset and has been processed into machine-friendly formats here.
