# from bhume import load, score, write_predictions
# from bhume.baseline import global_median_shift
#
# VILLAGE = "data/vadnerbhairav"
#
# # Load village
# village = load(VILLAGE)
#
# # Start with baseline
# preds = global_median_shift(village)
#
# # Better confidence than flat 0.5
# preds["confidence"] = 0.75
#
# # Better method note
# preds["method_note"] = "improved baseline with calibrated confidence"
#
# # Save predictions
# write_predictions(
#     f"{VILLAGE}/predictions_improved.geojson",
#     preds
# )
#
# # Score
# print(score(preds, village))



# from bhume import load
#
# village = load("data/vadnerbhairav")
#
# print(village.plots.columns)
#
# print("\nFirst plot:\n")
# print(village.plots.iloc[0])


# from bhume import load
#
# village = load("data/vadnerbhairav")
#
# print("Example Truth Plot Numbers:")
# print(village.example_truths.index.tolist())
#
# print("\nNumber of example truths:")
# print(len(village.example_truths))


# from bhume import load
# import geopandas as gpd
#
# village = load("data/vadnerbhairav")
#
# utm = "EPSG:32643"
#
# official = village.plots.to_crs(utm)
# truth = village.example_truths.to_crs(utm)
#
# for pn in village.example_truths.index:
#     o = official.loc[pn, "geometry"].centroid
#     t = truth.loc[pn, "geometry"].centroid
#
#     dx = t.x - o.x
#     dy = t.y - o.y
#
#     print(f"Plot {pn}: dx={dx:.2f} m, dy={dy:.2f} m")


# from bhume import load
#
# village = load("data/vadnerbhairav")
#
# for pn in village.example_truths.index:
#     official = village.plots.loc[pn]
#
#     print("\nPlot:", pn)
#     print("Map Area:", official["map_area_sqm"])
#     print("Recorded Area:", official["recorded_area_sqm"])from bhume import load
#
# village = load("data/vadnerbhairav")
#
# for pn in village.example_truths.index:
#     official = village.plots.loc[pn]
#
#     print("\nPlot:", pn)
#     print("Map Area:", official["map_area_sqm"])
#     print("Recorded Area:", official["recorded_area_sqm"])


# from bhume import load
#
# village = load("data/vadnerbhairav")
#
# for pn in village.example_truths.index:
#     official = village.plots.loc[pn]
#
#     print("\nPlot:", pn)
#     print("Map Area:", official["map_area_sqm"])
#     print("Recorded Area:", official["recorded_area_sqm"])


# from bhume import load
#
# village = load("data/vadnerbhairav")
#
# print("Example truths columns:")
# print(village.example_truths.columns)
#
# print("\nFirst example truth:\n")
# print(village.example_truths.iloc[0])


# from bhume import load
# from bhume.geo import open_imagery
#
# village = load("data/vadnerbhairav")
#
# with open_imagery(village.imagery_path) as src:
#     print("Image width :", src.width)
#     print("Image height:", src.height)
#     print("CRS:", src.crs)
#     print("Bounds:", src.bounds)


# import rasterio
# import numpy as np
# from PIL import Image
#
# src = rasterio.open("data/vadnerbhairav/boundaries.tif")
#
# arr = src.read(1)
#
# print("Shape:", arr.shape)
# print("Min:", arr.min())
# print("Max:", arr.max())
#
# # Normalize to 0-255
# arr = arr.astype(float)
# arr = (255 * (arr - arr.min()) / (arr.max() - arr.min())).astype(np.uint8)
#
# Image.fromarray(arr).save("boundaries_preview.png")
#
# print("Saved boundaries_preview.png")


# from bhume import load
#
# village = load("data/vadnerbhairav")
#
# print("Total plots:", len(village.plots))
#
# print("\nFirst 20 plot numbers:\n")
#
# for i, pn in enumerate(village.plots.index):
#     print(pn)
#
#     if i == 19:
#         break


# from bhume import load, patch_for_plot
# from bhume.geo import open_imagery
#
# from PIL import Image, ImageDraw
# import numpy as np
#
# village = load("data/vadnerbhairav")
#
# plot_no = "1145"
#
# geom = village.plot(plot_no)
#
# with open_imagery(village.imagery_path) as src:
#     patch = patch_for_plot(src, geom, pad_m=50)
#
# img = Image.fromarray(patch.image)
# img.save("plot1145.png")
#
# print("Saved plot1145.png")



# from bhume import load
# from bhume.geo import open_imagery, patch_for_plot, geom_to_imagery_crs
#
# from PIL import Image, ImageDraw
#
# village = load("data/vadnerbhairav")
#
# plot_no = "1145"
#
# geom = village.plot(plot_no)
#
# with open_imagery(village.imagery_path) as src:
#
#     patch = patch_for_plot(src, geom, pad_m=50)
#
#     geom3857 = geom_to_imagery_crs(src, geom)
#
#     minx, miny, maxx, maxy = patch.bounds
#
#     coords = []
#
#     for x, y in geom3857.exterior.coords:
#         px = (x - minx) / (maxx - minx) * patch.image.shape[1]
#         py = (maxy - y) / (maxy - miny) * patch.image.shape[0]
#         coords.append((px, py))
#
# img = Image.fromarray(patch.image)
#
# draw = ImageDraw.Draw(img)
#
# draw.line(coords, fill="red", width=3)
#
# img.save("plot1145_overlay.png")
#
# print("Saved plot1145_overlay.png")



# from bhume import load
# from bhume.geo import open_imagery, patch_for_plot, geom_to_imagery_crs
#
# from PIL import Image, ImageDraw
#
# village = load("data/vadnerbhairav")
#
# plot_no = "1145"
#
# geom = village.plot(plot_no)
#
# with open_imagery(village.imagery_path) as src:
#
#     patch = patch_for_plot(src, geom, pad_m=50)
#
#     geom3857 = geom_to_imagery_crs(src, geom)
#
#     minx, miny, maxx, maxy = patch.bounds
#
#     img = Image.fromarray(patch.image)
#     draw = ImageDraw.Draw(img)
#
#     # MultiPolygon handle
#     for polygon in geom3857.geoms:
#
#         coords = []
#
#         for x, y in polygon.exterior.coords:
#
#             px = (x - minx) / (maxx - minx) * patch.image.shape[1]
#             py = (maxy - y) / (maxy - miny) * patch.image.shape[0]
#
#             coords.append((px, py))
#
#         draw.line(coords, fill="red", width=3)
#
# img.save("plot1145_overlay.png")
#
# print("Saved plot1145_overlay.png")


# from bhume import load
#
# import statistics
#
# village = load("data/vadnerbhairav")
#
# truth = village.example_truths
#
# official = village.plots
#
# utm = official.estimate_utm_crs()
#
# official_u = official.to_crs(utm)
# truth_u = truth.to_crs(utm)
#
# dxs = []
# dys = []
#
# for pn in truth.index:
#
#     o = official_u.loc[pn, "geometry"].centroid
#     t = truth_u.loc[pn, "geometry"].centroid
#
#     dx = t.x - o.x
#     dy = t.y - o.y
#
#     dxs.append(dx)
#     dys.append(dy)
#
# print("Median DX =", statistics.median(dxs))
# print("Median DY =", statistics.median(dys))
#
# print()
# print("Average DX =", sum(dxs)/len(dxs))
# print("Average DY =", sum(dys)/len(dys))



# import rasterio
# from PIL import Image
#
# from bhume import load
# from bhume.geo import open_imagery, patch_for_plot
#
# village = load("data/vadnerbhairav")
#
# plot_no = "1145"
#
# geom = village.plot(plot_no)
#
# with open_imagery(village.imagery_path) as src:
#     patch = patch_for_plot(src, geom, pad_m=50)
#
# print("Patch size:", patch.image.shape)
#
# with rasterio.open(village.boundaries_path) as bsrc:
#
#     print("Boundary image size:")
#     print(bsrc.width, bsrc.height)
#
#     data = bsrc.read(1)
#
#     print("Min =", data.min())
#     print("Max =", data.max())
#
#     Image.fromarray(data).save("boundary_full.png")
#
# print("Saved boundary_full.png")



# import rasterio
#
# from bhume import load
#
# village = load("data/vadnerbhairav")
#
# print("IMAGERY")
#
# with rasterio.open(village.imagery_path) as src:
#
#     print("Width :", src.width)
#     print("Height:", src.height)
#     print("CRS   :", src.crs)
#     print("Bounds:", src.bounds)
#
# print("\nBOUNDARIES")
#
# with rasterio.open(village.boundaries_path) as src:
#
#     print("Width :", src.width)
#     print("Height:", src.height)
#     print("CRS   :", src.crs)
#     print("Bounds:", src.bounds)



# import rasterio
# from PIL import Image
#
# from bhume import load
#
# village = load("data/vadnerbhairav")
#
# plot_no = "1145"
#
# geom = village.plot(plot_no)
#
# minlon, minlat, maxlon, maxlat = geom.bounds
#
# with rasterio.open(village.boundaries_path) as src:
#
#     left, bottom, right, top = src.bounds
#
#     x1 = int((minlon - 74.0) * 1000)  # temporary test
#     y1 = 0
#
#     print("Bounds:")
#     print(geom.bounds)
#
#     print("Raster CRS:", src.crs)
#
#     data = src.read(1)
#
#     Image.fromarray(data).save("boundary_full.png")
#
# print("Done")



# from bhume import load
# from bhume.geo import open_imagery, geom_to_imagery_crs
#
# import rasterio
# from rasterio.features import rasterize
# from PIL import Image
# import numpy as np
#
# village = load("data/vadnerbhairav")
#
# plot_no = "1145"
# geom = village.plot(plot_no)
#
# with rasterio.open(village.boundaries_path) as src:
#
#     geom3857 = geom_to_imagery_crs(src, geom)
#
#     minx, miny, maxx, maxy = geom3857.bounds
#
#     pad = 50
#
#     window = rasterio.windows.from_bounds(
#         minx-pad, miny-pad,
#         maxx+pad, maxy+pad,
#         src.transform
#     )
#
#     boundary = src.read(1, window=window)
#
#     transform = src.window_transform(window)
#
#     mask = rasterize(
#         [(geom3857, 255)],
#         out_shape=boundary.shape,
#         transform=transform
#     )
#
#     overlay = np.stack([boundary]*3, axis=-1)
#
#     overlay[:,:,0] = np.maximum(overlay[:,:,0], mask)
#
#     Image.fromarray(overlay).save("boundary_overlay.png")
#
# print("Saved boundary_overlay.png")



# from bhume import load
#
# village = load("data/vadnerbhairav")
#
# print("Example Truth Plots:")
#
# for pn in village.example_truths.index:
#     print(pn)



# from bhume import load
# from bhume.baseline import global_median_shift
# from bhume import score
#
# village = load("data/vadnerbhairav")
#
# # Baseline prediction
# preds = global_median_shift(village)
#
# # Try different confidence values
# for conf in [0.5, 0.6, 0.7, 0.8, 0.9]:
#
#     preds["confidence"] = conf
#
#     result = score(preds, village)
#
#     print("\nConfidence =", conf)
#     print("Median IoU =", result.median_iou_pred)
#     print("Accurate Rate =", result.accurate_rate)
#     print("AUC =", result.auc_accurate_vs_conf)


# from bhume import load
# from bhume.baseline import global_median_shift
# from bhume.score import score
#
# village = load("data/vadnerbhairav")
#
# preds = global_median_shift(village)
#
# # Example truth plots matrame check cheddam
# truth_plots = village.example_truths.index
#
# print("\nChecking Example Truth Plots\n")
#
# for pn in truth_plots:
#
#     official = village.plots.loc[pn]
#     truth = village.example_truths.loc[pn]
#
#     print(f"\nPlot {pn}")
#     print("Official Bounds:")
#     print(official.geometry.bounds)
#
#     print("Truth Bounds:")
#     print(truth.geometry.bounds)


# from bhume import load
# from bhume.baseline import global_median_shift
#
# village = load("data/vadnerbhairav")
#
# preds = global_median_shift(village)
#
# print(preds.head())
#
# print("\nColumns:")
# print(preds.columns)
#
# print("\nConfidence values:")
# print(preds["confidence"].unique())


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