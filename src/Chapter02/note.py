import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path

    import pandas as pd
    import marimo as mo

    this_dir = Path(__file__).parent
    return mo, pd, this_dir


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU14 データの全体像をつかもう
    """)
    return


@app.cell
def _(pd, this_dir):
    sales_df = pd.read_csv(this_dir / "sales_data.csv")
    sales_df.head()
    return (sales_df,)


@app.cell
def _(sales_df):
    sales_df.info()
    return


@app.cell
def _(sales_df):
    stats_summary = sales_df.describe()
    stats_summary
    return


@app.cell
def _(pd, this_dir):
    store_master = pd.read_csv(this_dir / "store_master.csv")
    product_master = pd.read_csv(this_dir / "product_master.csv")
    customer_master = pd.read_csv(this_dir / "customer_master.csv")

    def print_all(df: pd.DataFrame):
        print(df.head())
        print(df.info())
        print(df.describe())

    return customer_master, print_all, product_master, store_master


@app.cell
def _(print_all, store_master):
    print_all(store_master)
    return


@app.cell
def _(print_all, product_master):
    print_all(product_master)
    return


@app.cell
def _(customer_master, print_all):
    print_all(customer_master)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU15 データ型を確認・変換しよう
    """)
    return


@app.cell
def _(customer_master):
    customer_master_dtypes = customer_master.dtypes
    customer_master_dtypes
    return


@app.cell
def _(customer_master):
    customer_master["customer_id"] = customer_master["customer_id"].astype(str)
    customer_master.dtypes
    return


@app.cell
def _(customer_master):
    customer_master["age_group"].unique()
    return


@app.cell
def _(customer_master):
    customer_master["age_group"] = customer_master["age_group"].astype("category")
    customer_master.dtypes
    return


@app.cell
def _(customer_master):
    cat_cols = ["gender", "occupation", "member_rank"]
    customer_master[cat_cols] = customer_master[cat_cols].astype("category")
    customer_master.dtypes
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU16 列を追加・削除・名前変更しよう
    """)
    return


@app.cell
def _(product_master):
    product_master["profit_margin"] = product_master["price"] - product_master["cost"]
    product_master.head(3)
    return


@app.cell
def _(product_master):
    product_master["is_high_margin"] = product_master["profit_margin"] >= 300
    product_master.head()
    return


@app.cell
def _(product_master):
    _ = product_master.drop("profit_margin", axis=1)
    r = _.drop(["is_high_margin", "cost"], axis=1)
    r.columns
    return (r,)


@app.cell
def _(r):
    _ = r.rename(columns={
        "price": "価格",
        "category": "カテゴリー",
    })
    _.columns
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU17 日付データを使いこなそう
    """)
    return


@app.cell
def _(sales_df):
    datetime_dtype1 = sales_df["purchase_datetime"].dtype
    datetime_dtype1
    return


@app.cell
def _(pd, sales_df):
    sales_df["purchase_datetime"] = pd.to_datetime(sales_df["purchase_datetime"])
    datetime_dtype2 = sales_df["purchase_datetime"].dtype
    datetime_dtype2
    return


@app.cell
def _(sales_df):
    sales_df["purchase_datetime"].head()
    return


@app.cell
def _(sales_df):
    sales_df["year"] = sales_df["purchase_datetime"].dt.year
    sales_df["month"] = sales_df["purchase_datetime"].dt.month
    sales_df["day"] = sales_df["purchase_datetime"].dt.day
    sales_df["hour"] = sales_df["purchase_datetime"].dt.hour
    sales_df["day_of_week"] = sales_df["purchase_datetime"].dt.dayofweek
    return


@app.cell
def _(sales_df):
    sales_df[["purchase_datetime", "year", "month", "day", "hour", "day_of_week"]]
    return


@app.cell
def _(sales_df):
    weekday_names = {i: k for i, k in enumerate("月火水木金土日")}
    sales_df["weekday_name"] = sales_df["day_of_week"].map(weekday_names)
    sales_df[["day_of_week", "weekday_name"]].value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU18 データを結合しよう
    """)
    return


@app.cell
def _(customer_master, product_master, sales_df, store_master):
    for d in [sales_df, store_master, customer_master, product_master]:
        print(d.head(2))
    return


@app.cell
def _(pd, sales_df, store_master):
    sales_with_store = pd.merge(sales_df, store_master, on="store_id")
    sales_with_store.head(3)
    return (sales_with_store,)


@app.cell
def _(customer_master, pd, product_master, sales_with_store):
    sales_with_store_product = pd.merge(sales_with_store, product_master, on="product_id")
    sales_with_store_product["customer_id"] = sales_with_store_product["customer_id"].astype(str)
    customer_master["customer_id"] = customer_master["customer_id"].astype(str)
    full_sales_df = pd.merge(sales_with_store_product, customer_master, on="customer_id")
    return


@app.cell
def _(pd):
    df_left = pd.DataFrame(
        {
            "menu_id": [1,2],
            "menu_name": ["あんぱん", "塩パン"],
        }
    )
    df_right = pd.DataFrame(
        {
            "menu_id": [1, 201],
            "store": ["新宿店", "渋谷店"],
        }
    )
    print("内部結合：inner")
    print(pd.merge(df_left, df_right, on="menu_id", how="inner"))

    print("左外部結合：left")
    print(pd.merge(df_left, df_right, on="menu_id", how="left"))

    print("右外部結合：right")
    print(pd.merge(df_left, df_right, on="menu_id", how="right"))

    print("完全外部結合：outer")
    print(pd.merge(df_left, df_right, on="menu_id", how="outer"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU20 データをグループごとに集計しよう
    """)
    return


@app.cell
def _(sales_with_store):
    store_sales = sales_with_store.groupby("store_name")["amount"].sum()
    store_sales.head()
    return


@app.cell
def _(sales_with_store):
    store_mean = sales_with_store.groupby("store_name")["amount"].mean()
    store_mean.head(3)
    return


@app.cell
def _(sales_with_store):
    store_count = sales_with_store.groupby("store_name")["amount"].count()
    store_count.head(3)
    return


@app.cell
def _(sales_with_store):
    store_max = sales_with_store.groupby("store_name")["amount"].max()
    store_max.head(3)
    return


@app.cell
def _(sales_with_store):
    store_min = sales_with_store.groupby("store_name")["amount"].min()
    store_min.head(3)
    return


@app.cell
def _(sales_with_store):
    store_stats = sales_with_store.groupby("store_name")["amount"].agg(["sum", "mean", "count"])
    store_stats.head(3)
    return


if __name__ == "__main__":
    app.run()
