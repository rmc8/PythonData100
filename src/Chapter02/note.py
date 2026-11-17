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
    return full_sales_df, sales_with_store_product


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
    return (store_sales,)


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU21 groupby()メソッドでさまざまな集計をしてみよう
    """)
    return


@app.cell
def _(sales_with_store_product):
    category_sales = sales_with_store_product.groupby("category")["amount"].sum()
    category_sales.head()
    return (category_sales,)


@app.cell
def _(pd, sales_with_store_product):
    sales_with_store_product["purchase_datetime"] = pd.to_datetime(sales_with_store_product["purchase_datetime"])
    sales_with_store_product["weekday"] = sales_with_store_product["purchase_datetime"].dt.dayofweek
    weekday_map = {
        i:k for i, k in enumerate("月火水木金土日")
    }
    sales_with_store_product["weekday_name"] = sales_with_store_product["weekday"].map(weekday_map)
    weekday_sales = sales_with_store_product.groupby("weekday_name")["amount"].sum()
    weekday_sales.sort_values()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU22 ピボットテーブルでクロス集計に挑戦しよう
    """)
    return


@app.cell
def _(pd, sales_with_store_product):
    pivot_sales = pd.pivot_table(
        sales_with_store_product,
        index="store_name",
        columns="category",
        values="amount",
        aggfunc="sum",
        fill_value=0
    )
    pivot_sales.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU23 データを縦方向に結合しよう
    """)
    return


@app.cell
def _(pd, this_dir):
    oct_df = pd.read_csv(this_dir / "sales_202610.csv")
    nov_df = pd.read_csv(this_dir / "sales_202611.csv")
    dec_df = pd.read_csv(this_dir / "sales_202612.csv")

    dfs = (oct_df, nov_df, dec_df)
    for d in dfs:
        print(d.shape)
    return (dfs,)


@app.cell
def _(dfs, pd):
    quarterly_df = pd.concat(dfs, ignore_index=True)
    quarterly_df.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU24 文字列を置換・分割しよう
    """)
    return


@app.cell
def _(store_master):
    store_name = store_master["store_name"].head()
    store_name
    return


@app.cell
def _(product_master):
    product_name = product_master["product_name"].head()
    product_name
    return


@app.cell
def _(store_master):
    store_master["store_name_simple"] = store_master["store_name"].str.replace("Daily Grind Coffee ", "")
    store_replace = store_master[["store_name", "store_name_simple"]].head(3)
    store_replace
    return


@app.cell
def _(product_master):
    split_result = product_master["product_name"].str.split("(", expand=True)
    split_result.head()
    return (split_result,)


@app.cell
def _(product_master, split_result):
    product_master["base_name"] = split_result[0]
    product_master["size_info"] = split_result[1]
    cols = ["product_name", "base_name", "size_info"]
    product_master[cols].head()
    return (cols,)


@app.cell
def _(cols, product_master):
    product_master["size_info"] = product_master["size_info"].str.replace(")", "")
    product_master[cols].head()
    return


@app.cell
def _(product_master):
    latte_products = product_master[
        product_master["product_name"].str.contains("ラテ")
    ]
    print(latte_products.shape)
    latte_products.head(7)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU26 可視化の準備をしよう
    """)
    return


@app.cell
def _(customer_master, pd, product_master, sales_df, store_master):
    sales_df["datetime"] = pd.to_datetime(sales_df["purchase_datetime"])
    sales_df["hour"] = sales_df["datetime"].dt.hour
    sales_df["month"] = sales_df["datetime"].dt.month
    sales_df["weekday"] = sales_df["datetime"].dt.dayofweek
    sales_df["customer_id"] = sales_df["customer_id"].astype(str)
    merge_df1 = pd.merge(sales_df, store_master, on="store_id", how="left")
    merge_df2 = pd.merge(merge_df1, product_master, on="product_id", how="left")
    full_sales_df2 = pd.merge(merge_df2, customer_master, on="customer_id", how="left")
    full_sales_df2.head()
    return (full_sales_df2,)


@app.cell
def _(full_sales_df2, pd):
    full_sales_df2.to_csv("analyzed_sales_data.csv", index=False)
    analyzed_sales_data = pd.read_csv("analyzed_sales_data.csv")
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import japanize_matplotlib

    return (plt,)


@app.cell
def _(full_sales_df2, plt):
    plt.hist(full_sales_df2["hour"])
    plt.show()
    return


@app.cell
def _(full_sales_df2, plt):
    plt.hist(full_sales_df2["hour"], bins=16)
    plt.xlabel("時間帯")
    plt.ylabel("来店数")
    plt.title("時間別の来店数分布")
    plt.show()
    return


@app.cell
def _(full_sales_df2, plt):
    plt.figure(figsize=(10,6))
    plt.hist(full_sales_df2["hour"], bins=15,
             edgecolor="black",
             alpha=.7
            )
    plt.xlabel("時間帯")
    plt.ylabel("来店数")
    plt.title("時間別の来店数分布")
    plt.xticks(range(6,22))
    plt.grid(True, alpha=.3)
    plt.show()
    return


@app.cell
def _(full_sales_df2, plt):
    _, axes = plt.subplots(1, 2, figsize=(12, 5))
    # 左側のグラフ
    axes[0].hist(full_sales_df2["hour"], bins=15, edgecolor="black", alpha=.7)
    axes[0].set_xlabel("時間帯")
    axes[0].set_ylabel("来店数")
    axes[0].set_title("時間帯別の来店数分布")
    axes[0].grid(True, alpha=.3)

    # 右側のグラフ
    axes[1].hist(full_sales_df2["amount"], bins=30, edgecolor="black", color="orange", alpha=.7)
    axes[1].set_xlabel("購入金額（円）")
    axes[1].set_ylabel("頻度")
    axes[1].set_title("購入金額の分布")
    axes[1].grid(True, alpha=.3)


    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU28 棒グラフでカテゴリを比較してみよう
    """)
    return


@app.cell
def _(category_sales):
    category_sales.head()
    return


@app.cell
def _(category_sales, plt):
    plt.figure(figsize=(10,6))
    plt.bar(category_sales.index, category_sales.values)
    plt.title("カテゴリ別売上ランキング")
    plt.xlabel("カテゴリ")
    plt.ylabel("売上合計(円)")
    plt.show()
    return


@app.cell
def _(full_sales_df, plt):
    products = full_sales_df.groupby("product_name")["amount"].sum()
    plt.figure(figsize=(10,8))
    plt.barh(products.index, products.values)

    plt.title("商品別売上")
    plt.xlabel("売上合計(円)")
    plt.grid(axis="x", alpha=.5)

    plt.show()
    return (products,)


@app.cell
def _(plt, products):
    products_top10 = products.sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 8))
    plt.barh(products_top10.index, products_top10.values)
    plt.title("商品別売上")
    plt.xlabel("売上合計(円)")
    plt.grid(axis="x", alpha=.5)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU29 折れ線グラフで推移を追ってみよう
    """)
    return


@app.cell
def _(full_sales_df2, plt):
    hourly_customers = full_sales_df2.groupby("hour")["transaction_id"].count()
    plt.figure(figsize=(10, 6))
    plt.plot(hourly_customers.index, hourly_customers.values, marker="o", linewidth=2, markersize=8)
    plt.xlabel("時間帯")
    plt.ylabel("来客数")
    plt.title("1日の来客数推移")
    plt.grid(True, alpha=.5)
    plt.xticks(range(6,23))
    plt.show()
    return


@app.cell
def _(full_sales_df2, pd, plt):
    category_hourly = pd.pivot_table(
        full_sales_df2,
        index="hour",
        columns="category",
        values="amount",
        aggfunc="sum",
    )
    plt.figure(figsize=(12,6))
    for category in category_hourly.columns:
        plt.plot(category_hourly.index, category_hourly[category], marker="o", label=category)

    plt.xlabel("時間帯")
    plt.ylabel("売上(円)")
    plt.title("カテゴリ別時間帯売上推移")
    plt.legend() # 凡例を表示
    plt.grid(True, alpha=.5)
    plt.xticks(range(6,23))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU30 散布図で変数の関係を発見しよう
    """)
    return


@app.cell
def _(full_sales_df2, plt, store_sales):
    store_counts = full_sales_df2.groupby("store_name")["transaction_id"].count()
    # store_sales = full_sales_df2.groupby("store_name")["amount"].sum()
    plt.figure(figsize=(10, 6))
    plt.scatter(store_counts, store_sales, s=100, alpha=.7, color="blue")
    plt.xlabel("取引数")
    plt.ylabel("総売上(円)")
    plt.title("店舗別:取引数と売上の関係")
    plt.grid(True, alpha=.3)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MENU31 箱ひげ図で分布の特徴をつかもう
    """)
    return


@app.cell
def _(plt, sales_df):
    plt.figure(figsize=(8,6))
    plt.boxplot(sales_df["amount"])
    plt.title("購入金額の分布")
    plt.ylabel("購入金額(円)")
    plt.grid(axis="y", alpha=.5)
    plt.show()
    return


@app.cell
def _(sales_df):
    sales_amount = sales_df["amount"]
    print(sales_amount.quantile(.25))
    print(sales_amount.median())
    print(sales_amount.quantile(.75))
    return


@app.cell
def _():
    import seaborn as sns

    return (sns,)


@app.cell
def _(full_sales_df2, plt, sns):
    plt.figure(figsize=(12,6))
    sns.boxplot(data=full_sales_df2, x="store_type", y="amount", hue="category", palette="Set2")
    plt.title("店舗タイプ*カテゴリ別購入金額分布")
    plt.xlabel("店舗タイプ")
    plt.ylabel("購入金額(円)")
    plt.grid(axis="y", alpha=.5)
    plt.legend(title="カテゴリ")
    plt.show()
    return


if __name__ == "__main__":
    app.run()
