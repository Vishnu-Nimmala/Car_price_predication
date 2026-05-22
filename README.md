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

      background:
      linear-gradient(rgba(5,10,30,0.95),
      rgba(5,15,40,0.95)),
      url('https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?q=80&w=1600');

      background-size:cover;
      background-position:center;
      background-attachment:fixed;

      color:white;
      padding:40px;
    }

    .container{

      width:95%;
      max-width:1400px;
      margin:auto;

      background:rgba(255,255,255,0.08);
      backdrop-filter:blur(15px);

      border-radius:25px;
      padding:50px;

      box-shadow:0 20px 60px rgba(0,0,0,0.7);

    }

    h1{

      text-align:center;
      font-size:55px;
      color:#ffd369;
      margin-bottom:20px;
      text-shadow:2px 2px 10px black;

    }

    h2{

      color:#00ffcc;
      margin-top:45px;
      margin-bottom:20px;
      font-size:34px;

    }

    h3{

      color:#ffd369;
      margin-top:30px;
      margin-bottom:15px;
      font-size:26px;

    }

    p{

      font-size:19px;
      line-height:1.9;
      margin-bottom:20px;

    }

    ul{

      margin-left:30px;
      margin-bottom:25px;

    }

    ul li{

      margin-bottom:12px;
      font-size:18px;

    }

    table{

      width:100%;
      border-collapse:collapse;
      margin-top:20px;
      margin-bottom:35px;

    }

    table th,
    table td{

      border:1px solid rgba(255,255,255,0.2);
      padding:15px;
      text-align:left;
      font-size:17px;

    }

    table th{

      background:#ffd369;
      color:black;

    }

    table tr:nth-child(even){

      background:rgba(255,255,255,0.05);

    }

    .code{

      background:black;
      padding:20px;
      border-radius:15px;
      overflow-x:auto;
      margin-bottom:30px;
      color:#00ffcc;
      font-size:17px;
      line-height:1.8;

    }

    .badge{

      display:inline-block;
      background:#00ffcc;
      color:black;
      padding:10px 18px;
      border-radius:25px;
      margin:10px;
      font-weight:bold;
      font-size:16px;

    }

    .footer{

      text-align:center;
      margin-top:60px;
      font-size:22px;
      color:#ffd369;

    }

    a{

      color:#00ffcc;
      text-decoration:none;

    }

    a:hover{

      text-decoration:underline;

    }

    @media(max-width:768px){

      h1{
        font-size:38px;
      }

      h2{
        font-size:28px;
      }

      p,li{
        font-size:16px;
      }

    }

  </style>

</head>

<body>

  <div class="container">

    <h1>🚗 Car Price Prediction System</h1>

    <center>

      <span class="badge">Python 3.10</span>
      <span class="badge">Flask Web App</span>
      <span class="badge">Machine Learning</span>
      <span class="badge">Linear Regression</span>
      <span class="badge">Completed Project</span>

    </center>

    <h2>📌 What is This Project?</h2>

    <p>
      This project is a professional Car Price Prediction System developed using
      Machine Learning and Flask. Users can enter car details such as brand,
      year, engine size, fuel type, transmission, mileage, condition, and model.
      The system predicts the estimated car price using a trained Machine Learning model.
    </p>

    <ul>

      <li>Predicts estimated car price instantly</li>
      <li>Useful for buyers, sellers, and dealers</li>
      <li>Built using Machine Learning and Flask</li>
      <li>Frontend developed using HTML and CSS</li>

    </ul>

    <h2>🎯 Why Did I Build This Project?</h2>

    <ul>

      <li>To learn real-world Machine Learning implementation</li>
      <li>To connect ML models with Flask websites</li>
      <li>To understand how vehicle features affect car prices</li>
      <li>To improve my Data Analytics and ML Engineering skills</li>

    </ul>

    <h2>🛠️ Tools and Technologies Used</h2>

    <table>

      <tr>
        <th>Technology</th>
        <th>Purpose</th>
      </tr>

      <tr>
        <td>Python</td>
        <td>Main programming language</td>
      </tr>

      <tr>
        <td>Pandas</td>
        <td>Data preprocessing and analysis</td>
      </tr>

      <tr>
        <td>NumPy</td>
        <td>Numerical operations</td>
      </tr>

      <tr>
        <td>Scikit-learn</td>
        <td>Machine Learning model building</td>
      </tr>

      <tr>
        <td>Matplotlib</td>
        <td>Data visualization</td>
      </tr>

      <tr>
        <td>Seaborn</td>
        <td>Advanced graph styling</td>
      </tr>

      <tr>
        <td>Flask</td>
        <td>Web application framework</td>
      </tr>

      <tr>
        <td>HTML & CSS</td>
        <td>Frontend design</td>
      </tr>

      <tr>
        <td>Joblib</td>
        <td>Model saving/loading</td>
      </tr>

      <tr>
        <td>GitHub</td>
        <td>Version control</td>
      </tr>

      <tr>
        <td>Render</td>
        <td>Project deployment</td>
      </tr>

    </table>

    <h2>📊 Dataset Features</h2>

    <table>

      <tr>
        <th>Feature</th>
        <th>Description</th>
      </tr>

      <tr>
        <td>Brand</td>
        <td>Car company name</td>
      </tr>

      <tr>
        <td>Year</td>
        <td>Manufacturing year</td>
      </tr>

      <tr>
        <td>Engine Size</td>
        <td>Engine capacity</td>
      </tr>

      <tr>
        <td>Fuel Type</td>
        <td>Petrol/Diesel</td>
      </tr>

      <tr>
        <td>Transmission</td>
        <td>Manual/Automatic</td>
      </tr>

      <tr>
        <td>Mileage</td>
        <td>Total kilometers driven</td>
      </tr>

      <tr>
        <td>Condition</td>
        <td>New/Used/Like New</td>
      </tr>

      <tr>
        <td>Model</td>
        <td>Specific model name</td>
      </tr>

      <tr>
        <td>Price</td>
        <td>Target variable</td>
      </tr>

    </table>

    <h2>🧮 Machine Learning Workflow</h2>

    <h3>📍 Step 1 — Data Preprocessing</h3>

    <p>
      Text data like car brands and fuel types are converted into numerical values
      using Label Encoding because Machine Learning models cannot understand text directly.
    </p>

    <h3>📍 Step 2 — Multiple Linear Regression</h3>

    <p>
      The model learns relationships between car features and price using
      the Multiple Linear Regression formula.
    </p>

    <div class="code">

      Price = b0 + b1×Brand + b2×Year + b3×Engine Size + b4×Fuel Type
      + b5×Transmission + b6×Mileage + b7×Condition + b8×Model

    </div>

    <h3>📍 Step 3 — Model Training</h3>

    <p>
      The Machine Learning model is trained using historical car data.
      The algorithm continuously adjusts coefficients to minimize prediction error.
    </p>

    <h3>📍 Step 4 — Train Test Split</h3>

    <div class="code">

      Training Data → 80%  
      Testing Data  → 20%

    </div>

    <p>
      This ensures the model performs well on unseen real-world data.
    </p>

    <h2>📈 Evaluation Metrics</h2>

    <table>

      <tr>
        <th>Metric</th>
        <th>Purpose</th>
      </tr>

      <tr>
        <td>R² Score</td>
        <td>Measures model accuracy</td>
      </tr>

      <tr>
        <td>MAE</td>
        <td>Average prediction error</td>
      </tr>

      <tr>
        <td>MSE</td>
        <td>Squared prediction error</td>
      </tr>

      <tr>
        <td>RMSE</td>
        <td>Root Mean Squared Error</td>
      </tr>

    </table>

    <h2>📈 Visualizations</h2>

    <ul>

      <li>Brand vs Average Price</li>
      <li>Mileage vs Price</li>
      <li>Year vs Price</li>
      <li>Fuel Type Distribution</li>
      <li>Correlation Heatmap</li>
      <li>Actual vs Predicted Price</li>

    </ul>

    <h2>🚀 How to Run This Project</h2>

    <h3>Step 1 — Clone Repository</h3>

    <div class="code">

      git clone https://github.com/yourusername/car-price-prediction.git

    </div>

    <h3>Step 2 — Install Libraries</h3>

    <div class="code">

      pip install -r requirements.txt

    </div>

    <h3>Step 3 — Train Model</h3>

    <div class="code">

      python model.py

    </div>

    <h3>Step 4 — Run Flask App</h3>

    <div class="code">

      python app.py

    </div>

    <h3>Step 5 — Open Browser</h3>

    <div class="code">

      http://127.0.0.1:5000

    </div>

    <h2>📁 Project Folder Structure</h2>

    <div class="code">

car-price-prediction/

│

├── static/
├── templates/
├── app.py
├── model.py
├── car_model.pkl
├── requirements.txt
├── Procfile
└── README.md

    </div>

    <h2>📦 Required Libraries</h2>

    <div class="code">

flask
scikit-learn
pandas
numpy
matplotlib
seaborn
joblib
gunicorn

    </div>

    <h2>🌐 Deployment</h2>

    <p>
      This project is deployed using Render cloud platform.
      The application is connected directly with GitHub for automatic deployment.
    </p>

    <div class="code">

Procfile:

web: gunicorn app:app

    </div>

    <h2>🤝 Developed By</h2>

    <p>

      <strong>Nimmala Vishnu</strong><br><br>

      💼 Data Analyst & Machine Learning Engineer<br><br>

      🏢 Training — Vihara Tech Private Limited<br><br>

      📧 Email — nimmalavishnu602@gmail.com<br><br>

      🌐 Live Demo —
      <a href="https://car-price-prediction-eyp4.onrender.com" target="_blank">

        Click Here to View Application

      </a>

    </p>

    <div class="footer">

      ⭐ Thank You for Visiting My Project ⭐

    </div>

  </div>

</body>
</html>
