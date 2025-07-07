import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrice = np.array(list).reshape(3, 3)
    print(matrice)

    calculations = {
        'mean' : [
            matrice.mean(axis=0).tolist(),
            matrice.mean(axis=1).tolist(),
            matrice.mean().item()
        ],

        'variance' : [
            matrice.var(axis=0).tolist(),
            matrice.var(axis=1).tolist(),
            matrice.var().item()
        ],

        'standard deviation' : [
            matrice.std(axis=0).tolist(),
            matrice.std(axis=1).tolist(),
            matrice.std().item()
        ],

        'max' : [
            matrice.max(axis=0).tolist(),
            matrice.max(axis=1).tolist(),
            matrice.max().item()
        ],

        'min' : [
            matrice.min(axis=0).tolist(),
            matrice.min(axis=1).tolist(),
            matrice.min().item()
        ],

        'sum' : [
            matrice.sum(axis=0).tolist(),
            matrice.sum(axis=1).tolist(),
            matrice.sum().item()
        ]
    }    

    return calculations