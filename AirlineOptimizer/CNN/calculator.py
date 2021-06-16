#import libs
import math
import datetime
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
plt.style.use('fivethirtyeight')

def Calculator(training_data):
    # Get the scsv file created on batch
    df = pd.read_csv(training_data, sep=';', index_col=0)
    df

    # Get the number of rows and collumns in the data set
    df.shape

    plt.figure(figsize=(16, 8))
    plt.title('Sandwich coefficient')
    coefficient = df['Coefficient'].astype(float)
    plt.plot(df['Date'], coefficient)
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Coefficient', fontsize=18)

    # Create a new dataframe with only the 'Close' column
    data = df.filter(['Coefficient'])
    # Convert the dataframe to a numpy array
    dataset = data.values
    # Get the nuber of rows to train the model on
    training_data_len = math.ceil(len(dataset) * 0.8)

    training_data_len

    # Scale the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)

    scaled_data

    # Create the training data set
    # Create the scaled training data set
    train_data = scaled_data[0:training_data_len, :]
    # Split the data into x_train and y_train data set
    x_train = []
    y_train = []

    for i in range(60, len(train_data)):
        x_train.append(train_data[i - 60:i, ])
        y_train.append(train_data[i, 0])
        if i <= 60:
            print(x_train)
            print(y_train)
            print()

    # Convert the x_train and y_train to numpy arrays
    x_train, y_train = np.array(x_train), np.array(y_train)

    # Reshape the data
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    x_train.shape

    # Build the LSTM model
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    model.fit(x_train, y_train, batch_size=1, epochs=1)

    # Create the testing data set
    # Create a new array containing scaled values from index from 1543 to 2003
    test_data = scaled_data[training_data_len - 60:, :]
    # Create the data sets x_test and y_test
    x_test = []
    y_test = dataset[training_data_len:, :]
    for i in range(60, len(test_data)):
        x_test.append(test_data[i - 60:i, 0])

    # Convert the data to a numpy array
    x_test = np.array(x_test)

    # Reshape the data into 3D (LSTM expexcts 3D model)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1],
                                 1))  # number of samples, number of columns which is equal to the number of timesteps, number of features

    # Get the models predicted values for x_test dataset
    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)  # unscaling the values

    # Get the root mean squared error (RMSE) lowe the better
    rmse = np.sqrt(np.mean(predictions - y_test) ** 2)
    rmse

    # Plot the data
    train = data[:training_data_len]
    valid = data[training_data_len:]
    valid['Predictions'] = predictions
    # Visualize the data
    plt.figure(figsize=(16, 8))
    plt.title('Model')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Coefficient', fontsize=18)
    plt.plot(train['Coefficient'])
    plt.plot(valid[['Coefficient', 'Predictions']])
    plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')

    # Show the valid and the predicted values
    valid

    # Get the quote
    #df = pd.read_csv(test_data, sep=';', index_col=0)
    # Create a new data frame
    new_df = df.filter(['Coefficient'])
    # Get the last 60 days closing price values and convert the df to an array
    last_60_days = new_df[-60:].values
    # Scale the data to be values between 0 and 1
    last_60_days_scaled = scaler.transform(last_60_days)
    # Create an empty list
    X_test = []
    # Append the past 60 days
    X_test.append(last_60_days_scaled)
    # Convert the X_test data set to a numpy array
    X_test = np.array(X_test)
    # Reshape the data
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    # Get the predicted scaled price
    pred_coefficient = model.predict(X_test)
    # undo the scaling
    pred_coefficient = float(scaler.inverse_transform(pred_coefficient))
    print(pred_coefficient)
    return pred_coefficient

Calculator('sample_flight_beer.csv')
