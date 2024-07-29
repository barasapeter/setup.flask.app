# setup.flask.app
This repo holds script to automate setting up a flask multifile application.

# Flask App Structure Generator

This utility is a Python script that automatically generates a basic Flask application structure with predefined files and directories. It sets up a modular Flask application with blueprints, configurations, and essential files to kickstart your Flask project.

## Features

- Creates a complete Flask application structure
- Sets up blueprints for main application and API
- Includes configuration files for different environments (development, testing, production)
- Adds basic templates and static files
- Includes a sample database model and migration setup
- Provides a basic test structure

## Requirements

- Python 3.x
- pip (Python package installer)

## Usage

1. Save the script as `flask_app_generator.py` (or any preferred name).

2. Open a terminal and navigate to the directory containing the script.

3. Run the script with the desired project folder name as an argument:

   ```
   python flask_app_generator.py <project_folder_name>
   ```

   Replace `<project_folder_name>` with your desired project name.

4. If the folder already exists, you'll be prompted to overwrite it. Enter 'Y' or press Enter to overwrite, or 'N' to abort.

5. The script will create the Flask application structure in the specified folder.

## Generated Structure

The script generates the following structure:

```
<project_folder_name>/
├── app/
│   ├── __init__.py
│   ├── main/
│   │   ├── __init__.py
│   │   └── views.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   └── style.css
│   ├── models.py
│   └── extensions.py
├── migrations/
│   └── README
├── tests/
│   └── test_basics.py
├── config.py
├── requirements.txt
└── script.py
```

## Next Steps

After generating the structure:

1. Navigate to your project folder:
   ```
   cd <project_folder_name>
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python script.py
   ```

5. Start building your Flask application by adding routes, models, and templates as needed.

## Customization

You can modify the `flask_app_generator.py` script to add or remove files, change the content of generated files, or adjust the directory structure to better suit your needs.

## License

This project is open-source and available under the MIT License.