n=20

for i in range(2,21):
    with open(f"/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/multiplication_table/multiplication_table_of_{i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}\n")
           

