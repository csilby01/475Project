# import all necessary libraries

import numpy as np
from scipy.io import arff
import pandas as pd
from sklearn.model_selection import train_test_split
from tqdm import tqdm, trange
import matplotlib.pyplot as plt

# load the downloaded data to data frame and then convert it to numpy matrices

data = arff.loadarff("dataset_40_sonar.arff")
df = pd.DataFrame(data[0])
df = df.replace({b'Rock': -1, b'Mine': 1})

A = df.to_numpy()
X, Y = A[:, :-1], A[:, -1] # X is a 208 by 60 matrix and Y is a 208-dim vector -- that is, the input feature is 60-dim and the output is 1-dim (+1 or -1)

# perceptron predict and evaluation code -- it is now your turn to complete the code below

def predict(w_current, b_current, x_tst): # predict the label of x_tst with the current perceptron (w_current, b_current)
    # compute the percentron activation
    Theta = (w_current @ x_tst) + b_current
    if Theta > 0:
      prediction = 1
    else:
      prediction = -1
    # if it is > 0, predict +1 (Mine)
    # otherwise, predict -1 (Rock)
    return prediction

def evaluate(w_current, b_current, X_tst, Y_tst): # evaluate the predictive accuracy of (w, b) on (X_tst, Y_tst)
    acc = 0 # this variable records the no. of corrected predictions so far
    for i in range(X_tst.shape[0]): # for each test input
      prediction = predict(w_current, b_current, X_tst[i])
      if prediction == Y_tst[i]:
        acc += 1
    pred_acc = acc / X_tst.shape[0]
        # predict the label of X_tst[i], update the count of correct prediction
    return pred_acc # replace this with the return of the accuracy, which is the percentage of corrected predictions

# next, you are to fill in the training code

def update(w_current, b_current, X_tr, Y_tr): # (w_current, b_current) is the current estimated perceptron while (X_tr, Y_tr) is an individual (input, output) data point
    # use (w_current, b_current) to predict the label Y_pred for X_tr
    Y_pred = predict(w_current, b_current, X_tr)
    # compare Y_pred to (ground-truth) Y_tr and make adjustment to (w_current, b_current) as discussed in the lecture
    if Y_pred != Y_tr:
      for i in range(len(w_current)):
        w_current[i] = w_current[i] + alpha * (Y_tr - Y_pred) * X_tr[i]
      b_current += alpha * (Y_tr - Y_pred)
    return w_current, b_current # replace this with the return of the updated version of (w_current, b_current)

def perceptron_training(X_train, Y_train, alpha, n_epoch, checkpoint):
    d = X.shape[1] # feature dimension
    w, b = np.zeros(d), 0 # set everything to zero
    perceptrons = [] # use this list to store the perceptron models every "checkpoint" epochs

    for n in trange(n_epoch):  # for each epoch
        # perform a full scan over the training dataset & update the (w, b) whenever the prediction is incorrect
        for i in range(X_train.shape[0]):
          w,b = update(w,b,X_train[i], Y_train[i])

        if (n + 1) % checkpoint == 0:  # at every "checkpoint" epoches
            # save the current perceptron
            perceptrons.append((w, b))
    return perceptrons  # return the list of saved perceptrons

# set up evaluation configuration
n_evaluation, checkpoint, n_epoch, alpha = 5, 1000, 40000, 0.005
# n_evaluation: how many independent evaluation runs
# checkpoint: how frequent should we save the perceptron model while training
# n_epoch: how many training epochs per evaluation runs
# alpha: learning rate
train_acc, test_acc = [0.0] * (n_epoch // checkpoint), [0.0] * (n_epoch // checkpoint)
# if we save the model every "checkpoint" iterations, the no. of saved model is (n_epoch // checkpoint) -- note: // is integer division, e.g. 5 // 2 = 2 while 5/2 = 2.5
for i in range(n_evaluation):  # for each evaluation
    print("Evaluation Run {}".format(i + 1))
    # split the dataset into train, test (80/20 ratio) -- note how we set the random_state = i * 1000 so that we get a different partition for each eval run
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = i * 1000)
    # write code to call the above training routine & evaluate the predictive accuracy of the perceptron model at each checkpoint
    training = perceptron_training(X_train, Y_train, alpha, n_epoch, checkpoint)


# write code to compute the averaged train & test accuracies of the perceptron model across all eval runs
    y = 0
    for perceptron in training:
      train_acc[y] += evaluate(perceptron[0], perceptron[1], X_train, Y_train)
      test_acc[y] += evaluate(perceptron[0], perceptron[1], X_test, Y_test)
      y += 1



# store the results appropriately to the above train_acc, test_acc lists
for i in range(len(train_acc)):
  train_acc[i] /= n_evaluation

for i in range(len(test_acc)):
  test_acc[i] /= n_evaluation

# generate the code to plot the averaged train & test accuracy against the no. of epoches

plt.figure(figsize=(10, 5))
plt.plot (train_acc, label='Train Accuracy')
plt.plot (test_acc, label='Test Accuracy')
plt.xlabel('Epochs(in thousands)')
plt.ylabel('Accuracy')
plt.legend()
plt.show()