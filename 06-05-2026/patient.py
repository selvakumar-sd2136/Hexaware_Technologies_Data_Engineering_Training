import dlt
from pyspark.sql.functions import *

@dlt.table
def bronze_patient_visit():
    data = [
        (1001,"Aarav Khan","Hyderabad","Cardiology",5000,2),
        (1002,"Priya Reddy","Bengaluru","Dermatology",3000,1),
        (1003,"Rahul Mehta","Mumbai","Orthopedics",7500,3),
        (1004,"Sneha Kapoor","Delhi","Pediatrics",2900,1),
        (1005,"Kiran Patel","Ahmedabad","Cardiology",5300,2),
        (1006,"Ananya Das","Kolkata","Neurology",10000,4),
        (1007,"Vikram Singh","Chennai","Dermatology",2850,1),
        (1008,"Meera Nair","Kochi","Orthopedics",5400,2),
        (1009,"Farhan Ali","Hyderabad","Cardiology",3200,1),
        (1010,"Divya Menon","Bengaluru","Dermatology",4800,2)
        ]

    columns = [
        "patient_id",
        "patient_name",
        "city",
        "specialization",
        "bill_amount",
        "tests_count"
        ]

    return spark.createDataFrame(data, columns)

@dlt.table
def silver_patient_visit():
    df=dlt.read("bronze_patient_visit")

    return df.withColumn(
        "test_cost",
        col("tests_count") * 500
    ).withColumn(
        "total_bill",
        col("bill_amount") + col("test_cost")
    ).filter(
        col("bill_amount").isNotNull()
    )

@dlt.table
def gold_city_revenue():
    df=dlt.read("silver_patient_visit")

    return  df.groupBy("city") \
        .agg(
            sum("total_bill").alias("city_revenue")
        )
@dlt.table
def gold_speciallization_revenue():
    df=dlt.read("silver_patient_visit")

    return  df.groupBy("specialization") \
        .agg(
            sum("total_bill").alias("specialization_revenue")
        )
