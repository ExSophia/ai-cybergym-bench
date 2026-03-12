from ai_cybergym_bench import CyberGymBench

bench = CyberGymBench()
result = bench.evaluate(model="gpt-4o", task_id=1)  # 改成你想测的模型
print(result)
