# tsp-gcn

To run the code:

## Generate train-test-val data
```
python data/TSP/generate_TSP.py --filename="data/TSP/tsp_train.txt" --split="train" --num_samples=1000
python data/TSP/generate_TSP.py --filename="data/TSP/tsp_val.txt" --split="val" --num_samples=500
python data/TSP/generate_TSP.py --filename="data/TSP/tsp_test.txt" --split="test" --num_samples=500
```

## Run the classification

python main_TSP_edge_classification.py --config="config/TSP_edge_classification_GatedGCN_100k.json"
