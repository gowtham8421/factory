from faker import Faker
import random

fake = Faker()

class ProductFactory:
    @staticmethod
    def create_fake_product():
        product_name = fake.word()
        product_price = random.uniform(1, 1000)
        product_category = fake.word()
        product_description = fake.text()

        return {
            "name": product_name,
            "price": product_price,
            "category": product_category,
            "description": product_description
        }

    @staticmethod
    def create_fake_products_batch(num_products):
        products = []
        for _ in range(num_products):
            product = ProductFactory.create_fake_product()
            products.append(product)
        return products

# Example usage
if __name__ == "__main__":
    num_fake_products = 10
    fake_products = ProductFactory.create_fake_products_batch(num_fake_products)
    for product in fake_products:
        print(product)
