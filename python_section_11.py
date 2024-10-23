
# Assuming that result_df is the output Dataframe of python_section_10.py
# Set the tax rate for motorcycles
tax_rate_moto = 0.8
result_df['moto'] = result_df['distance'] * tax_rate_moto
print(result_df)

# Calculate the toll for cars

tax_rate_car = 1.2
result_df['car'] = result_df['distance'] * tax_rate_car
print(result_df)


# Calculate the toll for rv's
tax_rate_rv = 1.5
result_df['rv'] = result_df['distance'] * tax_rate_rv
print(result_df)


# Calculate the toll for buses
tax_rate_bus = 2.2
result_df['bus'] = result_df['distance'] * tax_rate_bus
print(result_df)


# Calculate the toll for trucks
tax_rate_truck = 3.6
result_df['truck'] = result_df['distance'] * tax_rate_truck
print(result_df)
