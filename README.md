# Chemical Equipment Parameter Visualizer

## Project Components

| Directory | Description | Technology |
| :--- | :--- | :--- |
| `Desktop_frontend` | The **Desktop Application Frontend**. | Python |
| `equipment_project` | The **Common Server** (Backend API) for both desktop and web versions. | Django |
| `webapp` | The **Web Application Frontend**. | React.js |

## Getting Started

After cloning the repository:

1.  Install dependencies and requirements individually as guided in upcomming steps.(using a **virtual environment** is strongly recommended).
2.  Run the components separately using the commands provided below.
3.  Create a new user (use the register option) once the server is running.

## Setup and Run Commands

### I. Common Server (`equipment_project`)

1.  **Clone Repository:**
    ```bash
    git clone [https://github.com/sriManikanta07/Chemical-Equipment-Parameter-Visualizer](https://github.com/sriManikanta07/Chemical-Equipment-Parameter-Visualizer)
    cd Chemical-Equipment-Parameter-Visualizer
    ```

2.  **Virtual Environment Setup:**
    ```bash
    python -m venv venv
    source venv/Scripts/activate  # Windows
    # or source venv/bin/activate # Linux/macOS
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Server:**
    * **Migrations:**
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```
    * **Start Server:**
        ```bash
        python manage.py runserver 8080
        ```

### II. Desktop Frontend (`Desktop_frontend`)

1.  **Environment:** Use the same virtual environment as the common server, or install requirements separately.
2.  **Navigate to Directory:**
    ```bash
    cd Desktop_frontend
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Application:**
    ```bash
    python Desktop_frontend.py
    ```
    This command will open the desktop application window.

### III. Web App (`webapp`)

1.  **Navigate to Directory:**
    ```bash
    cd webapp
    ```

2.  **Install Dependencies:**
    ```bash
    npm install
    ```

3.  **Run Application:**
    ```bash
    npm run dev
    ```
    This will open the application in a browser window. If the application does not open, check that port **5174** is free.
