import torch
import esm

model, alphabet = esm.pretrained.esm2_t6_8M_UR50D()
batch_converter = alphabet.get_batch_converter()
model.eval()

def embed(sequence):

    data = [("pep", sequence)]

    _, _, tokens = batch_converter(data)

    with torch.no_grad():
        out = model(tokens, repr_layers=[6])

    emb = out["representations"][6].mean(1).squeeze()

    return emb