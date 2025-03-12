# des = 'Bulgari is one tia conmpar with the best brands in the world. It is a brand that is loved by many people and is known for its quality and style. Bulgari is a brand that is loved by many people and is known for its quality and style.'
# des ='Gucci is one tia conmpar with the best brands in the world. '
# des = 'BVLGARI is one tia conmpar with the best brands in the world. '
brands = ['BVLGARI', 'Bulgari', 'Gucci', 'Burberry', 'Cartier', 'Hermès']
matched_brand = next((name for name in brands if name in des), None)
if matched_brand:
    if matched_brand == 'Bulgari' or matched_brand == 'BVLGARI':
        print('Bulgari')
    else:
        print(matched_brand)