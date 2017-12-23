from sklearn import datasets
iris = datasets.load_iris()

x = iris.data 
y = iris.target

from sklearn.cross_validation import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = .5)

from sklearn import tree
# create classifier
my_classifier = tree.DecisionTreeClassifier()
#train with training data
my_classifier.fit(X_train, y_train)

#classify testing data
predictions = my_classifier.predict(X_test)
print predictions
 
from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)

