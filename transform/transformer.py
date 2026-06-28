import pandas as pd
from utils.logger import logger


class Transformer:
    def transform(self, data):
        logger.info("Transformation Started..")

        rows = []

        for cart in data["carts"]:
            for product in cart["products"]:
                rows.append(
                    {
                        "order_id": cart["id"],
                        "customer_name": f"Customer_{cart['userId']}",
                        "product_name": product["title"],
                        "quantity": product["quantity"],
                        "unit_price": product["price"],
                        "total_amount": product["quantity"] * product["price"],
                    }
                )
        df = pd.DataFrame(rows)

        logger.info(f"Transformation Completed: {len(df)} rows")
        return df
