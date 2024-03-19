from src.database import Database
from src.helper.write_a_json import writeAJson
from src.product_analyzer import ProductAnalyzer

db = Database(database="mercado", collection="produtos")
#db.resetDatabase()

product_analyzer = ProductAnalyzer()

total_sales_per_day = product_analyzer.total_sales_per_day()
writeAJson(total_sales_per_day, "total_de_vendas_por_dia")

most_sold_product = product_analyzer.most_sold_product()
writeAJson(most_sold_product, "produto_mais_vendido")

customer_highest_spending = product_analyzer.customer_highest_spending()
writeAJson(customer_highest_spending, "cliente_com_mais_gastos_em_uma_unica_compra")

products_sold_above_quantity = product_analyzer.products_sold_above_quantity()
writeAJson(products_sold_above_quantity, "produtos_vendidos_acima_de_1_unidade")
