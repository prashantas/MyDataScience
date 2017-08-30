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

##########################################################################################################################
###########################################################################################################################
  ### DRAWING roc CURVE **********************
  #https://datamize.wordpress.com/2015/01/24/how-to-plot-a-roc-curve-in-scikit-learn/
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import random

#2) Generate actual and predicted values. First let use a good prediction probabilities array:

actual = [1,1,1,0,0,0]
predictions = [0.9,0.9,0.9,0.1,0.1,0.1]

false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
roc_auc = auc(false_positive_rate, true_positive_rate)
##4) Finally we plot the fpr vs tpr as well as our auc for our very good classifier.

plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate, true_positive_rate, 'b',
label='AUC = %0.2f'% roc_auc)
plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

###############################################################################################################
################################################################################################################
