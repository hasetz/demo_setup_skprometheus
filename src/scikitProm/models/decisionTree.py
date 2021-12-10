from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier


model = make_pipeline(
    DecisionTreeClassifier()
)
