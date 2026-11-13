import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path

    import pandas as pd
    import marimo as mo

    return Path, mo, pd


@app.cell
def _(Path, pd):
    this_dir = Path(__file__).parent
    sales_csv = pd.read_csv(this_dir / "sales_data.csv")
    sales_csv.head()
    return sales_csv, this_dir


@app.cell
def _(pd, this_dir):
    customer_csv = pd.read_csv(this_dir / "customer_data.csv")
    customer_csv.head()
    return


@app.cell
def _(sales_csv):
    len(sales_csv)
    return


@app.cell
def _(sales_csv):
    sales_csv.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU7 まずはデータを眺めてみよう
    """)
    return


@app.cell
def _(sales_csv):
    sales_csv.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU8 データ構造と品質を確認しよう
    """)
    return


@app.cell
def _(pd, this_dir):
    sales_df = pd.read_csv(this_dir / "sales_data.csv")
    null_data = sales_df.isnull()
    null_count = null_data.sum()
    null_count
    return (sales_df,)


@app.cell
def _(pd, this_dir):
    customer_df = pd.read_csv(this_dir / "customer_data.csv")
    customer_null_data= customer_df.isnull()
    customer_null_count = customer_null_data.sum()
    customer_null_data
    return (customer_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU9 数字でデータの特徴をつかもう

    `describe()`メソッドは、DataFrameの数値列について、件数、平均値、標準偏差、最小値、四分位数、最大値などをまとめて表示する。統計量とは、データの特徴をようやくするために計算される値で、`describe()`メソッドで確認できるこれらの代表的な値を**基本統計量**と呼ぶ。デフォルトでは数値列が対象となる。
    """)
    return


@app.cell
def _(sales_df):
    describe_result = sales_df.describe()
    describe_result
    return


@app.cell
def _(customer_df):
    customer_describe_result = customer_df.describe()
    customer_describe_result
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU10 必要なデータだけを取り出そう
    """)
    return


@app.cell
def _(sales_df):
    quantity_col = sales_df["quantity"]
    quantity_col.head()
    return


@app.cell
def _(sales_df):
    selected_cols = sales_df[["purchase_date", "total_amount"]]
    selected_cols.head()
    return


@app.cell
def _(sales_df):
    iloc_result = sales_df.iloc[9:15]
    iloc_result
    return


@app.cell
def _(sales_df):
    iloc_columns_result = sales_df.iloc[:5, 2:5]
    iloc_columns_result
    return


@app.cell
def _(sales_df):
    sales_df_loc = sales_df.loc[:, ["product_name", "total_amount"]]
    sales_df_loc.head()
    return


@app.cell
def _():
    return


@app.cell
def _(sales_df):
    smartphone_sales = sales_df.loc[
        sales_df["product_category"] == "スマートフォン"
    ]
    smartphone_sales.head()
    return


@app.cell
def _(sales_df):
    mask = sales_df["product_category"] == "スマートフォン"
    mask.head()
    return


@app.cell
def _(sales_df):
    condition = (
        (sales_df["product_category"] == "タブレット") &
        (sales_df["quantity"] >= 3)
    )
    tablet_bulk = sales_df.loc[condition]
    tablet_bulk_head = tablet_bulk.head()
    tablet_bulk_head
    return


@app.cell
def _(sales_df):
    condition2 = (
        (sales_df["product_category"] == "スマートフォン") |
        (sales_df["product_category"] == "タブレット")
    )
    smartphone_or_tablet = sales_df.loc[condition2]
    smartphone_or_tablet.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU 11 データを見える形にしてみよう
    """)
    return


@app.cell
def _(sales_df):
    quantity_hist = sales_df["quantity"].plot(kind="hist", bins=20, edgecolor="black")
    quantity_hist
    return


@app.cell
def _(customer_df):
    age_hist = customer_df["age"].plot(kind="hist", bins=30, edgecolor="black")
    age_hist
    return


@app.cell
def _(sales_df):
    scatter_plot = sales_df.plot(kind="scatter", x="quantity", y="total_amount", alpha=.5)
    scatter_plot
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU12 データを並び替えて傾向をみよう
    """)
    return


@app.cell
def _(sales_df):
    top_sales = sales_df.sort_values("total_amount", ascending=False)
    top_sales_display = top_sales.head()
    top_sales_display
    return


@app.cell
def _(sales_df):
    bottom_sales = sales_df.sort_values("total_amount", ascending=True)
    bottom_sales_display = bottom_sales.head()
    bottom_sales_display
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU13 データ型を理解しよう
    """)
    return


@app.cell
def _(sales_df):
    dtypes_result = sales_df.dtypes
    dtypes_result
    return


@app.cell
def _(sales_df):
    dtype_counts = sales_df.dtypes.value_counts()
    dtype_counts
    return


@app.cell
def _(sales_df):
    object_columns = sales_df.select_dtypes(include=["object"])
    object_columns.head()
    return


if __name__ == "__main__":
    app.run()
