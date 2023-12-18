### AirBnb Automation Project

1. **Project Description:**
   Automation of the AirBnb.com website using pytest and Selenium WebDriver in Chrome. The project includes both UI and API tests, along with utility methods found in the `helpers` directory for UI and `api_utils` for API.

2. **Installation:**
   - Clone the repository: `git clone https://github.com/<>.git`
   - Navigate to the project directory: `cd AirBnb_Automation`
   - Install dependencies: `pip install -r requirements.txt`

3. **Usage:**
   - UI Tests: Execute UI tests using pytest and Selenium WebDriver.
     ```bash
     pytest tests/ui
     ```
   - API Tests: Run API tests using pytest.
     ```bash
     pytest tests/api
     ```

4. **Project Structure:**
- AirBnb_Automation/
  - data/                  # Test data (credentials, etc.) 
  - elements               # Locators and endpoints
  - helpers/               # Directory for test helpers
  - pages/                 # Page factories
  - tests/
    - api/                 # Directory for API tests
	- ui/                  # Directory for UI tests
  - requirements.txt
  - README.md

5. **Contributing:**
Contributions are welcome! If you would like to contribute to the project, please follow these steps:
- Fork the repository
- Create a new branch: `git checkout -b feature_branch`
- Make your changes and commit them: `git commit -m 'Add new feature'`
- Push to the branch: `git push origin feature_branch`
- Submit a pull request

6. **Contact:**
For inquiries or further information, please contact Maryia Shumanskaya at maryjashum@gmail.com.