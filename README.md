# Gentational HealthSnap

This project serves as a nutrition analyzer for foods, employing image recognition to identify the contents of a given image and subsequently display their corresponding nutritional information. Specifically tailored for women during pregnancy, it facilitates the monitoring of their nutritional intake by comparing the nutritional values of foods against the recommended pregnancy vitamin and nutrient guidelines provided by the American Pregnancy Association:  https://americanpregnancy.org/healthy-pregnancy/pregnancy-health-wellness/pregnancy-vitamins-nutrients/. 

The project includes 3 parts: 
1. Food image recognizer: a trained deep learning model
2. Food nutritional content calculator
3. Final deliverable on streamlit

## Requirements
- numpy 1.22.1
- fuzzywuzzy 0.18.0
- pandas 2.0.3
- matplotlib 3.7.3
- openai 1.14.2
- scikit-learn 1.3.2
- tensorflow 2.13.1
- keras 2.13.1
- streamlit 1.32.2

## Food image recognizer

The model is trained on the Food-101 dataset: https://www.kaggle.com/datasets/kmader/food41/data, which comprises 101 distinct food classes, with each image representing a single food category. First, the model utilizes the Inception model architecture (https://cloud.google.com/tpu/docs/inception-v3-advanced#introduction). Subsequently, the output latent vectors are employed as input for an additional, straightforward deep learning model. The achieved accuracy of the model on the test set reaches 60%. The training details can be found in notebook `Image_CNN.ipynb`.

## Nutritional content calculator

The 101 food categories are cross-referenced with a recipe table available at https://www.kaggle.com/datasets/shuyangli94/foodcom-recipes-with-search-terms-and-tags/data. This table provides details such as serving size, ingredients, and their corresponding amounts. All ingredient quantities are standardized into grams. For ingredients measured by volume, conversion to grams is conducted using the density of water. Natural language processing of ingredient amounts within the recipes is facilitated through OpenAI's capabilities in language processing.

The nutritional contents per 100 grams of each ingredient are sourced from Nutritional Values for Common Foods (https://www.kaggle.com/datasets/trolukovich/nutritional-values-for-common-foods-and-products) and Products. Each recipe's ingredients are cross-referenced with this table to aggregate their respective nutritional values. This process enables the compilation of comprehensive nutrition profiles for the recipes, facilitating informed dietary analysis and tracking. The final tabel includes the following nutritions: 

- Vitamin A
- Vitamin D
- Vitamin E
- Vitamin C
- Thiamin
- Riboflavin
- Niacin
- Vitamin B6
- Vitamin B12
- Folic Acid
- Calcium
- Iron
- Protein
- Zinc

The processing details can be found in notebook `Food_nutrition.ipynb`.

## Streamlit 

The culmination of this project is accessible through the following link: https://gestational-healthsnap-11.onrender.com/. Users are empowered to upload an image featuring a singular food item, upon which the system generates a graph illustrating the associated nutritional information. This graph includes the percentage representation of each nutrient compared to the daily dietary requirements for pregnant women, ensuring a comprehensive overview of nutritional intake. The files of this streamlit project are located at `streamlit_proj`.
