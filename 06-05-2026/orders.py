import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="bronze_orders_new"
)
def bronze_orders():

    data = [
        (321,114,204,"2024-04-11",3,"Delivered"),
        (322,118,210,"2024-04-11",2,"Delivered"),
        (304,114,208,"2024-04-02",5,"Delivered"),
        (319,112,208,"2024-04-10",2,"Delivered"),
        (323,120,210,"2024-04-12",1,"Pending")
    ]

    columns = [
        "order_id",
        "product_id",
        "supplier_id",
        "order_date",
        "quantity",
        "order_status"
    ]

    return spark.createDataFrame(data, columns)


#
@dlt.table(
    name="silver_orders_new"
)
def silver_orders():

    df = dlt.read("bronze_orders_new")

    return df.withColumn(
        "order_date",
        to_date("order_date","yyyy-MM-dd")
    ).withColumn(
        "total_revenue",
        col("quantity") * 1000
    ).filter(
        col("quantity") > 0
    )

@dlt.table(
    name="gold_city_revenue_new"
)
def gold_city_revenue():

    df = dlt.read("silver_orders_new")

    return df.groupBy("supplier_id") \
        .agg(
            sum("total_revenue")
            .alias("city_revenue")
        )

@dlt.table(
    name="gold_category_revenue_new"
)
def gold_category_revenue():

    df = dlt.read("silver_orders_new")

    return df.groupBy("order_status") \
        .agg(
            sum("total_revenue")
            .alias("category_revenue")
        )