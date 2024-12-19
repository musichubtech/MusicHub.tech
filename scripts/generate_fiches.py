import pandas as pd
from jinja2 import Template
import os

# Charger le fichier CSV
df = pd.read_csv('data/Categorized_Music_AI_and_Blockchain_Tools_with_Sub-Categories.csv')

# Template HTML
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{{ description }}">
    <title>{{ app_name }} - AI & Blockchain Tool</title>
    <link rel="stylesheet" href="../blog-style.css">
</head>
<body>
    <header>
        <a href="../index.html" class="logo-link"><img src="../assets/logo.png" alt="MusicHub.tech Logo" width="150"></a>
        <nav>
            <a href="../index.html">Home</a>
            <a href="../about.html">About</a>
            <a href="../apps.html" class="active">AI & Blockchain Tools</a>
            <a href="../contact.html">Contact</a>
        </nav>
    </header>

    <main class="blog-post">
        <h1>{{ app_name }}</h1>
        <p><strong>Category:</strong> {{ category }}<br>
           <strong>Sub-category:</strong> {{ sub_category }}</p>
        <p>{{ description }}</p>

        <a href="{{ url }}" target="_blank" class="cta-button">Visit {{ app_name }}</a>
        
        {% if download_link %}
        <p><a href="{{ download_link }}" target="_blank" class="cta-button">Download {{ app_name }}</a></p>
        {% endif %}
    </main>

    <footer>
        <p>&copy; 2024 MusicHub.tech. All rights reserved.</p>
    </footer>
</body>
</html>
"""

# Créer le dossier blog s'il n'existe pas
output_folder = "blog"
os.makedirs(output_folder, exist_ok=True)

# Générer les fichiers HTML
for index, row in df.iterrows():
    template = Template(html_template)
    output = template.render(
        app_name=row['Application Name'],
        category=row['Category'],
        sub_category=row['Sub-category'],
        description=row['Description'],
        url=row['URL'],
        download_link=row['Download'] if pd.notnull(row['Download']) else None
    )

    filename = f"{row['Application Name'].lower().replace(' ', '_').replace('/', '_')}.html"
    with open(os.path.join(output_folder, filename), "w") as file:
        file.write(output)
