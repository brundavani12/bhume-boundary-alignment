from bhume import load, score, write_predictions
from bhume.baseline import global_median_shift

village = load("data/malatavadi")

preds = global_median_shift(village)

write_predictions(
    "data/malatavadi/predictions.geojson",
    preds
)

print(score(preds, village))