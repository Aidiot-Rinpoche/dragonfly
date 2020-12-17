import numpy as np
from sklearn.ensemble import RandomForestRegressor

def get_tr_dataset_size_from_z0(z0):
    """Returns the training dataset size"""
    return int(np.round(np.exp(z0)))

def _get_avg_regression_error(Y1, Y2):
  """ Returns the negative prediction error. """
  if len(Y1) != len(Y2):
    raise ValueError('Lenghts of Y1 (%d), and Y2 (%d) should be the same.'%(
                      len(Y1), len(Y2)))
  num_data = float(len(Y1))
  differences = np.array(Y1) - np.array(Y2)
  finite_diffs = differences[np.isfinite(differences)]
  if len(finite_diffs) > 0:
    max_finite_diff = finite_diffs.max()
  else:
    max_finite_diff = 10.0
  differences[np.logical_not(np.isfinite(differences))] = \
    np.clip(10*max_finite_diff, 10.0, 100.0)
  diff_sq = np.linalg.norm(differences)**2
  ret = diff_sq / num_data
  ret = min(ret, 100.0)
  return ret

def rfr_train_and_validate(hyperparam_vect, data, num_tr_data_to_use,
                           max_tr_data_size, max_va_data_size, *args, **kwargs):
    # get relevant subsets
    np.random.shuffle(data)
    colNum = data.shape[1]
    x_tr = data[0:max_tr_data_size,0:colNum-1]
    y_tr = data[0:max_tr_data_size,-1]
    x_va = data[-max_va_data_size:,0:colNum-1]
    y_va = data[-max_va_data_size:,-1]

    # train method
    hyperparam_dict = {'n_estimators':hyperparam_vect[0],
                       'criterion':hyperparam_vect[1],
                       'max_depth':hyperparam_vect[2],
                       'min_samples_split':hyperparam_vect[3],
                       'min_samples_leaf':hyperparam_vect[4],
                       'max_features':hyperparam_vect[5],
                       }
    model = ensemble.RandomForestRegressor(**hyperparam_dict)
    model.fit(x_tr, y_tr)
    
    # compute validation error
    predictions = model.predict(x_va)
    ret = _get_avg_regression_error(predictions, y_va)