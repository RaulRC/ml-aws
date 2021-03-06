
# coding: utf-8

# In[30]:

# Load libraries
import pandas
from pandas.tools.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# In[31]:


# Create file object for outputs
outputFile = open("output.txt", "w")

# Load dataset
url = "data/terrorism.csv"
dataset = pandas.read_csv(url)
dataset = dataset[["eventid", "iyear", "imonth", "iday", "country"]][:10000]

# In[32]:

# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'



# In[33]:



# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
    outputFile.write(msg + "\n")


# In[34]:



# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
accScore = accuracy_score(Y_validation, predictions)
confMatrix = confusion_matrix(Y_validation, predictions)
classReport = classification_report(Y_validation, predictions)
print(accScore)
print(confMatrix)
print(classReport)
outputFile.write(str(accScore) + "\n")
outputFile.write(str(confMatrix) + "\n")
outputFile.write(str(classReport) + "\n")
outputFile.close()

# In[ ]:



