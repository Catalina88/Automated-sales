import pandas as pd
import os
import matplotlib.pyplot as plt

# Rutas absolutas según tu proyecto
input_file = "C:/Users/User/Documents/data/sales_analyst/data/ventas.xlsx"
output_dir = "C:/Users/User/.n8n-files/output"
os.makedirs(output_dir, exist_ok=True)

# Leer Excel
df = pd.read_excel(input_file)

# Cálculos
total_sales = df["ventas"].sum()
df["ingresos"] = df["ventas"] * df["precio"]
total_revenue = df["ingresos"].sum()

sales_xproduct = df.groupby("producto")["ventas"].sum()
revenue_product = df.groupby("producto")["ingresos"].sum()

product_bsell = sales_xproduct.idxmax()
quantity_bsell = sales_xproduct.max()

product_genmoney = revenue_product.idxmax()
performer_top = revenue_product.max()

# Gráfico
plt.figure(figsize=(8,5))
sales_xproduct.plot(kind='bar')
plt.title("sales for product")
plt.xlabel("product")
plt.ylabel("Quantity sold")
plt.xticks(rotation=45)
plt.tight_layout()
grafico_path = os.path.join(output_dir, "grafico_ventas.png")
plt.savefig(grafico_path)
plt.close()

# Reporte Excel y JSON
reportfinancial = pd.DataFrame({
    "Total Ventas": [total_sales],
    "Total Ingresos": [total_revenue],
    "Producto Más Vendido": [product_bsell],
    "Producto Más Rentable": [product_genmoney]
})

reporte_excel = os.path.join(output_dir, "reporte.xlsx")
reporte_json = os.path.join(output_dir, "reporte.json")
reportfinancial.to_excel(reporte_excel, index=False)
reportfinancial.to_json(reporte_json, orient="records")

# Devuelve resultados a n8n
print("Total Sales:", total_sales)
print("Total Revenue:", total_revenue)
print("Best Selling Product:", product_bsell)
print("Most Profitable Product:", product_genmoney)
print("Excel saved at:", reporte_excel)
print("JSON saved at:", reporte_json)
print("Chart saved at:", grafico_path)