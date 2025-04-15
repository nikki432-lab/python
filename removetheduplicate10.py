customer_ids = [101,102,103,101,104,102]
unique_customer_ids = list(set(customer_ids))
print(unique_customer_ids)


'''
If you need to preserve the original order while removing
duplicates, you can use this approach
'''
customer_ids = [101, 102, 103, 101, 104, 102]
unique_customer_ids = []
for cid in customer_ids:
    if cid not in unique_customer_ids:
        unique_customer_ids.append(cid)
print(unique_customer_ids)
