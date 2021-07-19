train = pd.read_csv("../input/train.csv")
test = pd.read_csv("../input/test.csv")

# include only the rows having label = 0 or 1 (binary classification)
X = train[train['label'].isin([0, 1])]

# target variable
Y = train[train['label'].isin([0, 1])]['label']

# remove the label from X
X = X.drop(['label'], axis = 1)