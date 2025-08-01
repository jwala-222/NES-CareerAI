# How NES-CareerAI Works (Explained Simply)

Hey there! If you're reading this, you've probably seen NES-CareerAI and are curious about how it works. 
In this file I will try to explain every major part of the project in plain terms—no jargon, no confusion.

## What does NES-CareerAI actually do?

It’s a project made to help students get career suggestions based on their strengths and interests.

You type something like:  
> “I enjoy solving math problems and understanding how machines work.”

And NES-CareerAI will suggest job roles like:
- Data Analyst  
- Mechanical Engineer  
- Research Scientist  

Now let’s break down how it works under the hood.

---

## Step-by-Step Breakdown

### 1. User Input

You fill out a form with a sentence that describes your interests or skills.

---

### 2. Converting Text into Vectors (NLP part)

This sentence is processed through a Sentence Transformer model.  
The model turns your sentence into a vector—think of it as a string of 384 numbers that represent the meaning of your sentence.

Why use this?  
Because comparing raw text is hard. Numbers are easier for machines to compare.

---

### 3. Preprocessed Job Data

I used a large dataset called Kareerwege, which has around 600,000 job entries.

Each job title and description was already converted into its own vector using the same Sentence Transformer model (I used Google Colab and GPU for this because it takes a lot of time and resources).

All these job vectors are stored in a file, which is loaded when you run the app.

---

### 4. Finding the Best Matches (ML part)

Once your sentence is converted into a vector, the model compares it with over 600,000 job vectors.

This is done using something called the K-Nearest Neighbors algorithm (KNN).  
It finds the 5 vectors that are closest to yours (the “K” = 5). These are the most relevant job matches.

---

### 5. Showing the Result

The closest matching job roles (based on meaning, not just words) are shown back to you on the website, so you can explore those careers further.

---

## But why does it need so much RAM?

Good question.

Since we’re comparing your vector to over 600,000 other vectors, we need to load all of them into RAM.  
This isn’t like opening a file and reading one line—you need all the vectors present in memory to compare their distances quickly.

Think of it like this:  
> Your SSD is a big warehouse, your RAM is a small room.   
> If you want to read all the labels on 600,000 boxes, it's better to bring them all into the room rather than keep going back and forth to the warehouse.

That’s why it uses a good amount of RAM (around 6 to 8 GB minimum). On my system, I use Linux with swap enabled, so I get extra memory by using SSD as virtual RAM.

---

## Tech Summary (For the Nerds)

- **Frontend**: HTML/CSS  
- **Backend**: Python + Flask  
- **NLP Model**: `all-MiniLM-L6-v2` via `SentenceTransformers`  
- **ML Algorithm**: KNN from `scikit-learn`  
- **Dataset**: Kareerwege (over 600,000 entries)  
- **Storage**: Pre-vectorized with `joblib`

---

## Final Notes

This is my first project where I combined NLP and ML in a real-world use case.  
It was a big learning experience, and I’m glad people like you are interested in it.

If you have more questions, feel free to reach out—or keep an eye on the GitHub repo, because a video walkthrough is coming soon.

---

Thanks for reading!  
~ Abhimanyu (aka the creator of Torque)
