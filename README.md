# bhume-boundary-alignment
Bhume Take Home Assignment - Boundary Alignment
# Bhume Boundary Alignment Assignment

## Overview

This repository contains my solution for the Bhume boundary alignment take-home assignment.

The objective is to improve the alignment of official cadastral plot boundaries using satellite imagery and boundary hints.

## Approach

1. Loaded village bundles using the provided starter kit.
2. Analyzed example truth plots.
3. Computed centroid shifts between official plots and aligned examples.
4. Estimated a village-level median translation.
5. Applied the translation to all plots.
6. Exported corrected boundaries as GeoJSON predictions.
7. Evaluated results using IoU and centroid error metrics.

## Results

### Vadnerbhairav

* Median IoU: 0.713
* Official IoU: 0.612
* Improvement: +0.112
* Accurate @ IoU ≥ 0.5: 100%

### Malatavadi

* Median IoU: 0.588
* Official IoU: 0.510
* Improvement: +0.090
* Accurate @ IoU ≥ 0.5: 67%

## Repository Structure

* `quickstart.py` – starter workflow
* `improved_solution.py` – Vadnerbhairav workflow
* `malatavadi_solution.py` – Malatavadi workflow
* `predictions/` – generated prediction files
* `transcripts/` – AI interaction references

## Future Improvements

Given more time, I would:

* Implement local boundary snapping using `boundaries.tif`
* Use boundary confidence estimation
* Apply adaptive confidence calibration
* Explore image-based alignment techniques
