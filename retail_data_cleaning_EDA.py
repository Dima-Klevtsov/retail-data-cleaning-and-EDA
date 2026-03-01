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
    # Retail dataset cleaning and EDA
    """)
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import re

    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Import dataset
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv('data\online_retail_real_world.csv')
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


@app.cell
def _(df):
    df[['product_name', 'brand']] = df[['product_name', 'brand']].fillna('Unknown')
    return


@app.cell
def _(df):
    df.raw_weight.nunique()
    return


@app.cell
def _(df):
    df.shape
    return


if __name__ == "__main__":
    app.run()
