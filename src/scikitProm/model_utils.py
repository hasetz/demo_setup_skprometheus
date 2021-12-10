from sklearn.metrics import f1_score, make_scorer
from sklearn.model_selection import cross_validate, KFold


def train(model, X, y):
    cv = KFold(n_splits=5)
    scoring = {
        "f1_accuracy": make_scorer(f1_score, average="macro")
    }
    return cross_validate(
        model,
        X,
        y,
        return_train_score=True,
        cv=cv,
        scoring=scoring
    )
