# Flight Ticket Price Prediction
* Flight ticket prices can be something hard to guess, today we might see a price, check out the price of the same flight tomorrow, it will be a different story. We might have often heard travellers saying that flight ticket prices are so unpredictable. 
* Here you will be provided with prices of flight tickets for various airlines between the months of March and June of 2019 and between various cities.


### Type of Machine Learning task : 
It is an regression problem where given a set of features we need to predict the price of ticket from one city to another.

### Importing Data
The first step in any data analysis project is to import the data. In this case, will working with a dataset containing (Airline, Date_of_Journey, Source, Destination,Route, Dep_Time,	Arrival_Time, Duration, Total_Stops, Additional_Info) and the target column **Price**

### EDA
Exploratory Data Analysis (EDA) helps us gain insights into the structure and characteristics of the data. 
To start, use the `info()` function to get an overview of the dataset, Second, cheaking NULLs and Duplications,
after that go to Analysis at some cases like **(Univariate, Bivariate, Graphs)**
Graphs that means creating a some plots to visualize the data and the shown the big diff between featuers.

### Data Preprocessing

Data preprocessing is an essential step in any machine learning project. It involves transforming the raw data into a format suitable for training the model, and chose the best processing for the test data.

1. Get all Numeric columns as group, and Categorical columns as another groups, beacuse each type will be at diff preprocessing
that will be done using 'ColumnTransformer'

2. Numeric columns will be Preprocessed using **KNNImputer** for Filling NUlls value
 **StandardScaler** for scaling

3. Categorical columns will be Preprocessed using **SimpleImputer(strategy='most_frequent')** for Filling NUlls value using tha most frequent
 **OrdinalEncoder** for encoding all categorical to numbers 

### Model Training and Prediction

1. With the preprocessed data, we can proceed to train **SGDRegressor, RandomForestRegressor** 
2. will use the cross validation to use all data as train and as test.

### Model Evaluation & Tuning

To assess the performance of Models, we can use MSE & RMSE:
To Tune the model and choose the best parameters for models, we used the **GridSearchCV** 

### Model Deployment 
I deployment the models by building GUI using "Streamlit" library

### Finaly
Thank You...
