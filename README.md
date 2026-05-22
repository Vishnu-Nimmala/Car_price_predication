<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Car Price Prediction README</title>

  <style>

    *{
      margin:0;
      padding:0;
      box-sizing:border-box;
      font-family:Arial, Helvetica, sans-serif;
    }

    body{

      background:linear-gradient(to right,#0f172a,#1e293b);
      color:white;
      padding:40px;

    }

    .container{

      max-width:1200px;
      margin:auto;
      background:rgba(255,255,255,0.06);
      padding:40px;
      border-radius:25px;
      backdrop-filter:blur(12px);
      box-shadow:0 10px 40px rgba(0,0,0,0.5);

    }

    h1{

      text-align:center;
      font-size:52px;
      color:#ffd369;
      margin-bottom:20px;
      text-shadow:2px 2px 10px black;

    }

    .subtitle{

      text-align:center;
      font-size:22px;
      margin-bottom:40px;
      color:#d1d5db;

    }

    h2{

      color:#00ffcc;
      margin-top:35px;
      margin-bottom:15px;
      font-size:32px;
      border-left:6px solid #ffd369;
      padding-left:12px;

    }

    p{

      font-size:19px;
      line-height:1.8;
      margin-bottom:15px;
      color:#e5e7eb;

    }

    ul{

      margin-left:30px;
      margin-bottom:20px;

    }

    ul li{

      margin-bottom:10px;
      font-size:18px;

    }

    .code-box{

      background:#111827;
      padding:20px;
      border-radius:15px;
      overflow-x:auto;
      margin-top:15px;
      margin-bottom:25px;
      border:1px solid rgba(255,255,255,0.1);

    }

    code{

      color:#00ffcc;
      font-size:16px;

    }

    .highlight{

      color:#ffd369;
      font-weight:bold;

    }

    .footer{

      text-align:center;
      margin-top:50px;
      padding-top:25px;
      border-top:1px solid rgba(255,255,255,0.1);
      font-size:20px;
      color:#d1d5db;

    }

    .tag{

      display:inline-block;
      background:#ffd369;
      color:black;
      padding:8px 16px;
      border-radius:30px;
      margin:8px;
      font-weight:bold;

    }

  </style>

</head>

<body>

  <div class="container">

    <h1>🚗 Car Price Prediction</h1>

    <div class="subtitle">

      Machine Learning Project using Python & Scikit-Learn

    </div>

    <h2>📌 Project Overview</h2>

    <p>

      This project predicts the price of cars using Machine Learning algorithms.
      The system performs complete data preprocessing, categorical encoding,
      model training, testing, logging, and model saving.

    </p>

    <h2>⚙ Technologies Used</h2>

    <div class="tag">Python</div>
    <div class="tag">Pandas</div>
    <div class="tag">NumPy</div>
    <div class="tag">Scikit-Learn</div>
    <div class="tag">Matplotlib</div>
    <div class="tag">Logging</div>

    <h2>📂 Project Structure</h2>

    <div class="code-box">

<code>
CAR_PRICE_PREDICTION/
│
├── car_price_prediction_.csv
├── main.py
├── main_logcode.py
├── train_logcode.py
├── testing_logcode.py
├── model_saving.py
├── logs/
├── models/
└── README.md
</code>

    </div>

    <h2>📊 Features Used</h2>

    <ul>

      <li>Brand</li>
      <li>Year</li>
      <li>Engine Size</li>
      <li>Fuel Type</li>
      <li>Transmission</li>
      <li>Mileage</li>
      <li>Condition</li>

    </ul>

    <h2>🧠 Machine Learning Workflow</h2>

    <ul>

      <li>Data Loading using Pandas</li>
      <li>Removing unnecessary columns</li>
      <li>Converting categorical values into numerical values</li>
      <li>Splitting dataset into training and testing sets</li>
      <li>Training regression model</li>
      <li>Testing model accuracy</li>
      <li>Saving trained model</li>

    </ul>

    <h2>📦 Required Libraries</h2>

    <div class="code-box">

<code>
pip install numpy pandas matplotlib scikit-learn
</code>

    </div>

    <h2>▶ How to Run the Project</h2>

    <p class="highlight">Step 1 : Clone Repository</p>

    <div class="code-box">

<code>
git clone https://github.com/yourusername/car-price-prediction.git
</code>

    </div>

    <p class="highlight">Step 2 : Install Dependencies</p>

    <div class="code-box">

<code>
pip install -r requirements.txt
</code>

    </div>

    <p class="highlight">Step 3 : Run Main File</p>

    <div class="code-box">

<code>
python main.py
</code>

    </div>

    <h2>📝 Logging System</h2>

    <p>

      The project uses a custom logging system to track:
      dataset shape, column types, preprocessing steps,
      training status, testing status, and runtime errors.

    </p>

    <h2>💾 Model Saving</h2>

    <p>

      The trained Machine Learning model is saved for future deployment
      using a custom model saving module.

    </p>

    <h2>🚀 Future Improvements</h2>

    <ul>

      <li>Flask Deployment</li>
      <li>Streamlit Web Application</li>
      <li>Hyperparameter Tuning</li>
      <li>Feature Scaling</li>
      <li>Multiple Regression Algorithms</li>
      <li>Real-Time Price Prediction UI</li>

    </ul>

    <h2>👨‍💻 Developer</h2>

    <p>

      <span class="highlight">Nimmala Vishnu</span><br>
      Data Analyst | Machine Learning Engineer

    </p>

    <div class="footer">

      ⭐ Car Price Prediction Project using Machine Learning ⭐

    </div>

  </div>

</body>
</html>
