# Predictive basket service

## Install

    pip install -r requirements.txt


## Run

    python app.py

    curl --location --request POST 'http://localhost:5000/api/1.0/predict' \
        --header 'Content-Type: application/json' \
        --data-raw '[
            [
                "Milk",
                "Onion",
                "Nutmeg",
                "Kidney Beans",
                "Eggs",
                "Yogurt"
            ],
            [
                "Dill",
                "Onion",
                "Nutmeg",
                "Kidney Beans",
                "Eggs",
                "Yogurt"
            ],
            [
                "Milk",
                "Apple",
                "Kidney Beans",
                "Eggs"
            ],
            [
                "Milk",
                "Unicorn",
                "Corn",
                "Kidney Beans",
                "Yogurt"
            ],
            [
                "Corn",
                "Onion",
                "Onion",
                "Kidney Beans",
                "Ice cream",
                "Eggs"
            ]
        ]'