# the decision making tree will help you to make decision
# the ai will use some decision making model like random forest, adaboast
# area of use- carrier recommendation ,stock, investment,healthcare,
# where to use -huge amount of data

# create application for carrier recommendation system
# fet the dataset in terms of interest area
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = {
    "maths": [9, 2, 8, 3, 7, 4, 1, 5, 9, 2],
    "science": [8, 3, 9, 2, 8, 3, 2, 6, 8, 3],
    "Art": [2, 9, 1, 8, 2, 6, 9, 5, 2, 7],
    "communication": [4, 6, 3, 7, 5, 8, 8, 6, 6, 9],
    "Suggested_Career": [
        "Engineer",
        "Artist",
        "Engineer",
        "Artist",
        "Engineer",
        "Journalist",
        "Designer",
        "Teacher",
        "Doctor",
        "Writer",
    ],
}
# convert the given dataset into using pandas
df = pd.DataFrame(data)
# print maths column data
# print(df['math'])
# encode the targeted column into labels
le = LabelEncoder()
df["Career_Label"] = le.fit_transform(df["Suggested_Career"])

# convert the dataset into label and input feature
X = df[["maths", "science", "Art", "communication"]]
y = df["Career_Label"]

# to provide the testing and trainning using split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=41
)
# apply the random forest model on test train model

model = RandomForestClassifier(n_estimators=100, random_state=41)
# apply trainning for fit the data
model.fit(X_train, y_train)

# predict the future career for new user
# Example: A student strong in Art and Communication
maths = int(
    input("Enter the intrest in maths : 0 for not interested 1 for interested ")
)
science = int(
    input("Enter the science interest : 0 for not interested 1 for interested ")
)
Art = int(input("Enter the art interest : 0 for not interested 1 for interested "))
communication = int(
    input("Enter the communication interest : 0 for not interested 1 for interested ")
)

# to past the new user data into model
new_user = [[maths, science, Art, communication]]

# predict the label
predicted_label = model.predict(new_user)
# predict career
predicted_career = le.inverse_transform(predicted_label)
print("Suggested Career:", predicted_career[0])

# NOTE : when the dataset is very less , then the accuracy is very less
# NOTE :
