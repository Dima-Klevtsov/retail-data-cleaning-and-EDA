# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.2",
#     "pandas==3.0.1",
# ]
# ///

import marimo

__generated_with = "0.20.2"
app = marimo.App(
    width="medium",
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Retail dataset cleaning
    """)
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import re
    import matplotlib.pyplot as plt

    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Import dataset
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv('data\online_retail_raw.csv')
    df.head(2)
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Change columns name (single format)
    """)
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(df):
    df.columns = df.columns.str.replace(r'([a-z])([A-Z])', r'\1 \2', regex=True) \
                           .str.replace(' ', '_') \
                           .str.lower()
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Missing values
    """)
    return


@app.cell
def _(df):
    df.isna().sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Changing the missing values in the product and brand name to "Unknown"
    """)
    return


@app.cell
def _(df):
    df[['product_name', 'brand']] = df[['product_name', 'brand']].fillna('Unknown')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cleaning messy product and brand names
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Removing emojis from the "product_name" column
    """)
    return


@app.cell
def _(df):
    df['product_name'] = df['product_name'].apply(lambda x: x.encode('ascii', 'ignore').decode('ascii'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Removing duplicate, beginning, and ending spaces
    """)
    return


@app.cell
def _(df):
    columns_name_change = ['product_name', 'brand'] 

    df[columns_name_change] = df[columns_name_change].apply(
        lambda x: x.str.strip().replace(r'\s+',' ',regex=True)
                   .str.capitalize()) # single product and brand name
    return


@app.cell
def _(df):
    df.product_name.tolist()
    return


@app.cell
def _(df):
    df.product_name.value_counts()
    return


@app.cell
def _(df):
    df.brand.value_counts()
    return


@app.cell
def _(df):
    df.brand.tolist()
    return


@app.cell
def _(df):
    df.isna().sum()
    return


@app.cell
def _(df):
    df.dtypes
    return


@app.cell
def _(df, pd):
    df['order_date'] = pd.to_datetime(df['order_date'])
    return


@app.cell
def _(df):
    df.dtypes
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Parsing inconsistent quantity formats in raw_weight
    """)
    return


@app.cell
def _(df):
    df.raw_weight.tolist()
    return


@app.cell
def _(df):
    df["raw_weight"] = (df["raw_weight"].str.lower()
                                        .str.replace("grams", "g")
                                        .str.replace("gram", "g")
                                        .str.replace("klg", "kg")
                       )
    return


@app.cell
def _(df):
    df[["value", "unit"]] = df['raw_weight'].str.extract(r'(\d+\.?\d*)\s*(kg|g|ml)')
    return


@app.cell
def _(df):
    df.isna().sum()
    return


@app.cell
def _(df):
    df.unit.value_counts()
    return


@app.cell
def _(df):
    df['value'] = df['value'].astype(float)
    return


@app.cell
def _(df):
    df.dtypes
    return


@app.cell
def _():
    conversion_weight = {
        'kg': 1000,
        'g': 1,
        'ml': 1  # we don't know the density, so let's leave this assumption
    }
    return (conversion_weight,)


@app.cell
def _(conversion_weight, df):
    df['weight_grams'] = df['value'] * df['unit'].map(conversion_weight)
    return


@app.cell
def _(df):
    df['weight_grams'].hist()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Filling in the missing values in the unit_price column
    """)
    return


@app.cell
def _(df):
    df.unit_price.describe()
    return


@app.cell
def _(df):
    df.unit_price.isna().mean() 
    # Output np.float64(0.12833333333333333)
    return


@app.cell
def _(df):
    df.unit_price.hist()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Replacing missing values ​​in columns with group means
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### unit_price
    """)
    return


@app.cell
def _(df):
    df['unit_price'] = df['unit_price'].fillna(df.groupby('brand')['unit_price'].transform('mean'))
    return


@app.cell
def _(df):
    df.unit_price.hist()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### raw_weight
    """)
    return


@app.cell
def _(df):
    df.weight_grams.describe()
    return


@app.cell
def _(df):
    df.weight_grams.isna().mean() 
    # Output np.float64(0.19666666666666666)
    return


@app.cell
def _(df):
    df.weight_grams.hist()
    return


@app.cell
def _(df):
    df['weight_grams'] = df['weight_grams'].fillna(df.groupby('product_name')['weight_grams'].transform('mean'))
    return


@app.cell
def _(df):
    df.weight_grams.hist()
    return


@app.cell
def _(df):
    df.isna().mean()
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ####
    """)
    return


if __name__ == "__main__":
    app.run()
