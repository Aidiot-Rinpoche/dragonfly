from skrfr import get_tr_dataset_size_from_z0, rfr_train_and_validate
from sklearn.datasets import load_diabetes
import numpy as np

# Load Data
X, Y = load_diabetes(return_X_y=True, as_frame=False)
Y = Y.reshape(-1,1)
DATA = np.hstack((X,Y))

MAX_TR_DATA_SIZE = 400
MAX_VA_DATA_SIZE = 42

def objective(z, x):
    """Objective."""
    num_tr_data_to_use = get_tr_dataset_size_from_z0(z[0])
    return rfr_train_and_validate(x, DATA,num_tr_data_to_use,
        MAX_TR_DATA_SIZE, MAX_VA_DATA_SIZE)

def cost(z):
    """ Compute cost"""
    num_tr_data_to_use = get_tr_dataset_size_from_z0(z[0])
    return num_tr_data_to_use /float(MAX_TR_DATA_SIZE)