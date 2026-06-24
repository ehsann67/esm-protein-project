import torch
from transformers import EsmForProteinFolding, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("facebook/esmfold_v1")
model = EsmForProteinFolding.from_pretrained("facebook/esmfold_v1")

def predict_structure(sequence):

    inputs = tokenizer(sequence, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    return outputs