import yaml

with open("./data1.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)  # 返回字典
    print(data)
    print(type(data))
