from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
import pandas as pd

def load_data():
    train_dataset = pd.read_csv('test2.csv')
    test_dataset = pd.read_csv('test3.csv')
    train_columns = train_dataset.columns
    train_predictors = train_dataset[train_columns[train_columns != 'target']]
    train_target = train_dataset['target']

    test_columns = test_dataset.columns
    test_predictors = test_dataset[test_columns[test_columns != 'target']]
    test_target = test_dataset['target']

    X_train = train_predictors
    y_train = train_target

    X_test = test_predictors
    y_test = test_target

    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    return X_train, y_train, X_test, y_test


def build_model():
    model = Sequential()
    model.add(Dense(200, activation='relu', input_shape=(X_train.shape[3],)))
    model.add(Dense(200, activation='relu'))
    model.add(Dense(200, activation='relu'))
    model.add(Dense(200, activation='relu'))
    model.add(Dense(2, activation='softmax'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return model

X_train, y_train, X_test, y_test = load_data()

model = build_model()
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=200, verbose=2)

scores = model.evaluate(X_test, y_test)
print(f'Accuracy: {scores[1]} \n Error: {1 - scores[1]}')