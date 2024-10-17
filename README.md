## Application
<img width="1615" alt="REP_homepage" src="https://github.com/user-attachments/assets/87a2dd30-5667-48ef-bb69-6fbe0801d6a0">

<img width="1667" alt="REP_ollama" src="https://github.com/user-attachments/assets/be5e09f9-5200-42c4-9b2f-165888215628">

<img width="1624" alt="REP_Themes_News" src="https://github.com/user-attachments/assets/baaf82c5-dedd-4948-a4af-8839d90d0c22">


## Process to Run the Application

1. **Download the repository locally**  
   Clone or download the repository to your local machine.

2. **Create a virtual environment**  
   ```bash
   python -m venv <your-env-name>
   ```

3. **Install dependencies**  
   Activate the virtual environment and run the following command to install the required packages:  
   ```bash
   pip install -r reddit_analytics/requirements.txt
   ```

4. **Run the Streamlit app**  
   Use the command below to run the Streamlit app:  
   ```bash
   streamlit run frontend/streamlit_app/main.py
   ```

5. Make sure your ollama is running and the model is loaded. Change model name if you want.

6. Make sure your supabase is running and the database is created. Change the .env file if you want.

7. Run the app.




