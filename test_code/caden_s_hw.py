def predict(w_current, b_current, x_tst): # predict the label of x_tst with the current perceptron (w_current, b_current)
    # compute the percentron activation
    # if it is > 0, predict +1 (Mine)
    # otherwise, predict -1 (Rock)
    if np.sum(w_current*x_tst) + b_current >0:
      return 1
    return -1

def evaluate(w_current, b_current, X_tst, Y_tst): # evaluate the predictive accuracy of (w, b) on (X_tst, Y_tst)
    acc = 0 # this variable records the no. of corrected predictions so far
    for i in range(X_tst.shape[0]): # for each test input
        if predict(w_current, b_current, X_tst[i]) == Y_tst[i]:
          acc+=1
    return acc/X_tst.shape[0]

def update(w_current, b_current, X_tr, Y_tr): # (w_current, b_current) is the current estimated perceptron while (X_tr, Y_tr) is an individual (input, output) data point
    # use (w_current, b_current) to predict the label Y_pred for X_tr
    prediction = predict(w_current, b_current, X_tr)
    if prediction != Y_tr:
        for i in range (w_current.shape[0]):
            w_current[i] = w_current[i] + alpha*(Y_tr - prediction)*X_tr[i]
        b_current = b_current + alpha*(Y_tr - prediction)
    return (w_current, b_current)

def perceptron_training(X_train, Y_train, alpha, n_epoch, checkpoint):
    d = X.shape[1] # feature dimension
    w, b = np.zeros(d), 0 # set everything to zero
    perceptrons = [] # use this list to store the perceptron models every "checkpoint" epochs
    for n in trange(n_epoch):  # for each epoch
        # perform a full scan over the training dataset & update the (w, b) whenever the prediction is incorrect
        for i in range(X_train.shape[0]):
          temp = update(w, b, X_train[i], Y_train[i])
          w, b = temp[0], temp[1]
        if (n + 1) % checkpoint == 0:  # at every "checkpoint" epoches
            perceptrons.append((w,b))
    return perceptrons  # return the list of saved perceptrons