def consts(request):
    return dict(
        THUMBNAIL_350={
            "format": "png", "crop": "thumb", "width": 350,
        },
        THUMBNAIL_873_1280={
            "format": "png", "crop": "thumb", "width": 873, "height": 1280,
        },
        THUMBNAIL_1080_1080={
            "format": "png", "crop": "thumb", "width": 1080, "height": 1080,
        },
        CROP_300_300={
            "format": "png", "crop": "fill", "width": 300, "height": 300, "gravity": "face"
        },
    )
