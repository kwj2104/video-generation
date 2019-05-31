#!/bin/bash
for ((i=1; i<=$1; i++))
do
    python pix2pix.py --mode gen --output_dir data/output --input_dir data/output --checkpoint model_param
    cp data/output/outputs.jpg data/gen/$i.jpg
done