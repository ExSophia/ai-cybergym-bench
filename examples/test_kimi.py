from ai_cybergym_bench import CyberGymBench

bench = CyberGymBench()
result = bench.evaluate(model="moonshot-v1-8k", task_id=0)
print(result)
