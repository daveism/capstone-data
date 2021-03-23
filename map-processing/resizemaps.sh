#!/bin/bash
# This script resizes all the images it finds in a folder (and its subfolders) and resizes them
# The resized image is placed in the /resized folder which will reside in the same directory as the image
#
# Usage: > ./resizemaps.sh

initial_folder='no-distractor-v2'
# initial_folder='target-distractor-random-v2'
# initial_folder='target-distractor-clustered-v2'
# initial_folder='target-not-gestalt-distractor-clustered-v2'
# initial_folder='target-not-gestalt-distractor-random-v2'

resized_folder_name='maps-resized-for-s3'

all_images=$(find -E $initial_folder -iregex ".*\.(jpg|gif|png|jpeg)")

while read -r image_full_path; do
    filename=$(basename "$image_full_path");
    source_folder=$(dirname "$image_full_path");
    destination_full_path=$resized_folder_name/$filename;

    if [ ! -z "$image_full_path" -a "$image_full_path" != " " ] &&
        # Do not resize images inside a folder that was already resized
        [ "$(basename "$source_folder")" != "$resized_folder_name" ]; then

        convert $image_full_path -resize 50% $destination_full_path;
        pngquant $destination_full_path -f --ext .png;
    fi

done <<< "$all_images"

