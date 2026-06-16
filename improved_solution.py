from bhume import load, write_predictions, score
from bhume.baseline import global_median_shift

VILLAGE = "data/vadnerbhairav"

village = load(VILLAGE)

# Baseline prediction
preds = global_median_shift(village)

# Slightly better confidence
preds["confidence"] = 0.8

preds["method_note"] = (
    "Global median shift estimated from example truths"
)

# Save predictions
out = write_predictions(
    f"{VILLAGE}/predictions_final.geojson",
    preds
)

print("Saved:", out)
print()
print(score(preds, village))
