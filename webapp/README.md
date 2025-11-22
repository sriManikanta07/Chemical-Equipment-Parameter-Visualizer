# 🧪 Chemical Equipment Parameter Visualizer

This is a React-based front-end application designed to visualize and analyze data related to chemical equipment parameters, such as **Flowrate**, **Pressure**, and **Temperature**, sourced from uploaded CSV files. The application features user authentication (Login/Register) and utilizes **Chart.js** for interactive data representation.

## ✨ Features

* **User Authentication:** Secure **Login** and **Registration** functionality.
* **CSV Upload:** Users can upload CSV files containing equipment data.
* **Data Visualization:** Displays key statistics and charts, including:
    * Overall average statistics (Flowrate, Pressure, Temperature).
    * **Pie Chart** showing equipment type distribution.
    * **Bar Chart** comparing average parameters (Flowrate, Pressure, Temperature) per equipment type.
    * Detailed statistics presented in a **table** format.
* **Sidebar Navigation:** Easily switch between recently uploaded files for review.
* **Persistent State:** Uses `localStorage` to maintain user session (token) and store recent uploads/selected file data for a better user experience.
* **Responsive Design:** Styled using **Tailwind CSS** (implied by class names like `bg-white`, `p-8`, `shadow-xl`, `grid-cols-4`, etc.).

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your system:

* **Node.js** (v14 or higher)
* **npm** or **Yarn**
* A running backend API at the specified.
const API_BASE_URL = '[https://equipmentanalyzer.pythonanywhere.com/api](https://equipmentanalyzer.pythonanywhere.com/api)';

### 1. Installation

Clone the repository and install the dependencies:

```bash
git clone <repository-url>
cd <project-directory>
npm install

2. Configure API Endpoint

const API_BASE_URL = '[https://equipmentanalyzer.pythonanywhere.com/api](https://equipmentanalyzer.pythonanywhere.com/api)';

#########
3. Running the Application
Start the development server:

npm run dev


#######
Backend API Integration:

Endpoint	Method	Description

/api/login/	   POST	Authenticates a user and returns a token.

/api/register/	POST	Registers a new user and returns a token.

/api/upload_csv/	POST	Uploads a CSV file, processes it, and returns the analysis data. Requires an Authorization: Token <token> header.

######
Expected Upload CSV Data Format:
# {
#   "overall_stats": {
#     "total_records": 1000,
#     "avg_flowrate": 55.23,
#     "avg_pressure": 10.51,
#     "avg_temperature": 80.99,
#     "type_distribution": {
#       "Type A": 500,
#       "Type B": 300,
#       "Type C": 200
#     }
#   },
#   "per_type_stats": {
#     "Type A": {
#       "count": 500,
#       "avg_flowrate": 60.0,
#       // ... other averages
#     },
#     // ... other types
#   }
# }




Authentication Flow

    User enters credentials on the Login or Register screen.

    On successful authentication, the backend returns an authentication token.

    The token is stored in the browser's localStorage.

    The application transitions to the Dashboard.

    All subsequent protected API calls (like /api/upload_csv/) include this token in the Authorization header (Authorization: Token <token>).

    Clicking Logout clears the token from localStorage and returns the user to the Login screen.