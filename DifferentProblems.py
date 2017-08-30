# https://stackoverflow.com/questions/41864083/how-to-set-a-threshold-for-a-sklearn-classifier-based-on-roc-results
model = SomeSklearnModel()
model.fit(X_train, y_train)
predict = model.predict(X_test)
predict_probabilities = model.predict_proba(X_test)
fpr, tpr, _ = roc_curve(y_test, predict_probabilities)

#However, I am annoyed that predict chooses a threshold corresponding to 0.4% of true positives (false positives are zero).
#The ROC curve shows a threshold I like better for my problem where the true positives are approximately 20% (false positive around 4%).
#I then scan the predict_probabilities to find what probability value corresponds to my favourite ROC point. In my case this probability 
#is 0.21.
#Then I create my own predict array:

predict_mine = np.where(rf_predict_probabilities > 0.21, 1, 0)
#and there you go:

confusion_matrix(y_test, predict_mine)
#returns what I wanted:

#array([[6927,  309],
#       [ 621,  121]])
