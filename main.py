import numpy as np
orders = np.array([
    [101, 3, 1200, 4],
    [102, 5, 800, 3],
    [103, 2, 2500, 4],
    [104, 8, 450, 4],
    [105, 4, 1800, 3],
    [106, 6, 950, 4],
    [107, 3, 2200, 4],
    [108, 10, 600, 3],
    [109, 7, 1500, 4],
    [110, 2, 3000, 4],
    [111, 5, 750, 3],
    [112, 9, 1250, 4] ])
# orderID | Quantity | Price | Rating


print("Dimension : ",orders.ndim)
print("Shape : ",orders.shape)
print("Size : ",orders.size)

print("1st 5 orders : ",orders[:5,:])

print("Last 3 orders : ",orders[-3:,:])

print("Every second order : ",orders[1::2,:])

revenue=orders[:,1]*orders[:,2]
print("Revenue for every order : ",orders[:,1]*orders[:,2])

total_revenue=np.sum(orders[:,1]*orders[:,2])
print("Total Revenue : ",total_revenue)
average_revenue=np.mean(revenue)
print("Average Revenue : ",average_revenue)

order_highest_revenue_index=np.argmax(revenue)
order_highest_revenue=orders[order_highest_revenue_index]
print("Order with highest revenue : ",order_highest_revenue)

median_revenue=np.median(revenue)
print("Median revenue : ",median_revenue)

order_category=np.where(revenue>=15000,"High",np.where(revenue>=7500,"Medium","Low"))
print("Orders Categorize : ",order_category)

print("Orders where Quantity greater than or  equal to 5 and Rating greater than or equal to 3 : ",orders[((orders[:,1]>=5)&(orders[:,-1]>=3))])

print("Order having price above median or Rating is below 4 : ",orders[((orders[:,2]>np.median(orders[:,2]))|(orders[:,-1])>4)])
price=orders[:,2]
discount=np.where(orders[:,2]>1000,orders[:,2]*0.10,0)
print("Discount where order price greater than 1000 : ",discount)
new_price=price-discount
print("Price after discount : ",new_price)

print("Round discounted price up to 2 decimal points : ",np.around(new_price,2))

print("Standard deviation of prices : ",np.std(new_price))


p25=np.percentile(new_price,25)
p75=np.percentile(new_price,75)
print("25th percentile of prices : ",p25)
print("75th percentile of prices : ",p75)

print("price above 75th percentile : ",new_price[(new_price>p75)])

or4=orders[:,-1][(orders[:,-1])>=4]
percentage=len(or4)*100/len(orders[:,-1])
print("Percentage of orders having rating greater than or equal to 4 : ",percentage)

reshape_revenue=revenue.reshape((3,4))
print("Reshape revenue : ",reshape_revenue)

print("Average revenue of each row : ",np.mean(reshape_revenue,axis=1))

flatten_revenue=reshape_revenue.flatten()
print("Flatten revenue : ",flatten_revenue)

tr=revenue[((orders[:,-1]>=4)&(revenue>np.mean(revenue)))]
print("Total Revenue of orders having rating >=4 and revenue above average revenue : ",np.sum(tr))