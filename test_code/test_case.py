def predict(w_current, b_current, x_tst): # predict the label of x_tst with the current perceptron (w_current, b_current)
    theta = np.dot(x_tst, w_current) + b_current # compute the percentron activation
    if theta > 0:
        return 1 # if the activation > 0, predict positive (Mine)
    return -1 # else, predict negative (Rock)

def evaluate(w_current, b_current, X_tst, Y_tst): # evaluate the predictive accuracy of (w, b) on (X_tst, Y_tst)
    acc = 0
    for i in range(X_tst.shape[0]): # for each test input
        theta = predict(w_current, b_current, X_tst[i]) # predict
        if theta == Y_tst[i]: # check if the prediction is correct
            acc += 1 # update the no. of correct prediction
    return acc * 1.0 / X_tst.shape[0] # return correct percentage (accuracy)

def update(w_current, b_current, X_tr, Y_tr):
    Y_pred = predict(w_current, b_current, X_tr) # predict
    w_current = w_current + alpha * (Y_tr - Y_pred) * X_tr # update rule for w
    b_current = b_current + alpha * (Y_tr - Y_pred) # update rule for b
    return w_current, b_current  # if the prediction is correct, Y_tr - theta = 0 which cancels out the update

def perceptron_training(X_train, Y_train, alpha, n_epoch, checkpoint):
    d = X.shape[1] # feature dimension
    w, b = np.zeros(d), 0 # set everything to zero
    perceptrons = []
    for n in trange(n_epoch):  # for each epoch
        for i in range(X_train.shape[0]):  # each epoch requires a full scan over the training dataset
            w, b = update(w, b, X_train[i], Y_train[i])
        if (n + 1) % checkpoint == 0:  # save the model every "checkpoint" epoches
            perceptrons.append((np.copy(w), np.copy(b)))
    return perceptrons  # return the list of saved perceptrons