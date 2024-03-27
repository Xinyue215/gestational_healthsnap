import pandas as pd
import matplotlib.pyplot as plt
import sys

df = pd.read_csv('../final_df.csv', index_col='Classes')
df.drop(columns=['Unnamed: 0'], inplace=True)

def makeplot(food):
    
    def plot_pie(food, nutrient, daily_need, title, ax=None):
        if ax is None:
            fig, ax = plt.subplots()

        if daily_need >= df.loc[food][nutrient]:
            source = pd.DataFrame({"category": ['Provided', ''], "value": [df.loc[food][nutrient], daily_need - df.loc[food][nutrient]]})

            # Plot pie chart
            wedges, _ = ax.pie(source['value'], labels=source['category'], colors=['purple', 'lavender'])

            # Calculate percentage
            category_percentage = source.loc[source['category'] == 'Provided', 'value'].iloc[0] / daily_need * 100

            ax.set_aspect('equal')

            ax.set_title(f'{title} Content \n {category_percentage:.2f}%')

        else:
            source = pd.DataFrame({"category": ['Provided', ''], "value": [df.loc[food][nutrient], 0]})

            # Plot pie chart
            wedges, _ = ax.pie(source['value'], labels=source['category'], colors=['indianred', 'lavender'])

            # Calculate percentage
            category_percentage = source.loc[source['category'] == 'Provided', 'value'].iloc[0] / daily_need * 100

            ax.set_aspect('equal')

            ax.set_title(f'{title} Content exceed \n {category_percentage:.2f}%')


    nutrients = ['vitamin_a_per_serving_mcg', 'vitamin_d_per_serving_mcg', 'vitamin_e_per_serving_mg',
                 'vitamin_c_per_serving_mg', 'thiamin_per_serving_mg', 'riboflavin_per_serving_mg',
                 'niacin_per_serving_mg', 'vitamin_b6_per_serving_mg', 'vitamin_b12_per_serving_mcg',
                 'folic_acid_per_serving_mcg', 'calcium_per_serving_mg', 'iron_per_serving_mg',
                 'protein_per_serving_g', 'zinc_per_serving_mg']
    daily_needs = [770, 5, 15, 85, 1.4, 1.4, 18, 1.9, 2.6, 800, 1300, 27, 71, 13]
    titles = ['Vitamin A', 'Vitamin D', 'Vitamin E', 'Vitamin C', 'Thiamin', 'Riboflavin', 'Niacin', 'Vitamin B6',
              'Vitamin B12', 'Folic Acid', 'Calcium', 'Iron', 'Protein', 'Zinc']

    fig, axes = plt.subplots(4, 4, figsize=(15, 15))

    axes = axes.flatten()

    for i, (nutrient, daily_need, title) in enumerate(zip(nutrients, daily_needs, titles)):
        final_plot = plot_pie(food, nutrient, daily_need, title, ax=axes[i])

    axes[-1].set_visible(False)
    axes[-2].set_visible(False)
    plt.suptitle(f'Nutrient Content of {food}', fontsize=24, y=1.05)
    plt.tight_layout()
    
    return final_plot
