from sklearn import tree

# In machine learning and pattern recognition, a feature is an individual measurable property or
# characteristic of a phenomenon being observed. Choosing informative, discriminating and independent
# features is a crucial step for effective algorithms in pattern recognition, classification and regression.
features = [[140, 130, 120, 140], [130, 14, 180, 100], [140, 130, 120, 5], [130, 14, 180, 10]]

# The label is the final choice, such as dog, fish, iguana, rock, etc. Once you've trained your model, you will
# give it sets of new input containing those features; it will return the predicted "label" (pet type) for that
# person. Feature: In Machine Learning feature means a property of your training data.
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()

# teaching the classifier based on the above features and labels. Each array of features corresponds to a single label.
clf = clf.fit(features, labels)

print(clf.predict([[160, 150, 120, 100]]))  # returns predicted label for the imputed feature set
print(clf.predict([[160, 15, 120, 10]]))  # returns predicted label for the imputed feature set
