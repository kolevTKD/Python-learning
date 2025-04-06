gpu_price = 250.0

budget = float(input())
gpus_count = int(input())
cpus_count = int(input())
rams_count = int(input())

gpus_total = gpus_count * gpu_price
cpus_total = cpus_count * (gpus_total * 0.35)
rams_total = rams_count * (gpus_total * 0.1)

total = gpus_total + cpus_total + rams_total

if gpus_count > cpus_count:
    total -= total * 0.15

if budget >= total:
    print(f"You have {budget - total:.2f} leva left!")

else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")