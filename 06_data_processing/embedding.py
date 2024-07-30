# !pip install torch==2.3.1+cu121 -f https://download.pytorch.org/whl/torch_stable.html

import torch.nn.functional as F
from sentence_transformers import SentenceTransformer
import numpy as np

with open("reviews.txt", "r", encoding="utf-8") as file:
    reviews = file.readlines()

# Define the model and target dimension
matryoshka_dim = 512
model = SentenceTransformer("nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True)

# Function to generate embeddings in batches
def generate_embeddings_in_batches(model, texts, batch_size=32):
    embeddings = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        batch_embeddings = model.encode(batch, convert_to_tensor=True)
        batch_embeddings = F.layer_norm(batch_embeddings, normalized_shape=(batch_embeddings.shape[1],))
        batch_embeddings = F.normalize(batch_embeddings, p=2, dim=1)
        embeddings.append(batch_embeddings.cpu().numpy())
        print(i, len(texts), f"{round(100*i/len(texts))}%")
    return np.vstack(embeddings)

# Generate embeddings
embeddings = generate_embeddings_in_batches(model, reviews, batch_size=32)

print(embeddings.shape)
np.save(f"review_embeddings_original.npy", embeddings)

# Dimensions to slice
dimensions = [512, 256, 128, 64]

# Save the embeddings for each required dimension
for dim in dimensions:
    sliced_embeddings = embeddings[:, :dim]
    np.save(f"review_embeddings_{dim}.npy", sliced_embeddings)
