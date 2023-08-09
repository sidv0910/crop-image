import calendar
import os
import time
import shutil
import glob
import boto3
from zipfile import ZipFile
from PIL import Image, ImageOps


cropped = "cropped"
jpg_extension = '.jpg'
jpeg_extension = '.jpeg'
png_extension = '.png'
image_extensions = [jpg_extension, jpeg_extension, png_extension]
zipfile_extension = '.zip'
zipfile_format = 'zip'
macosx = '__MACOSX'
s3 = 's3'
region = 'us-east-1'
s3_bucket = 'contour-education-cropped-image'
separator = '.'
s3_url = 'https://' + s3_bucket + separator + s3 + separator + 'amazonaws.com/'


def cropImage(file):
    image = Image.open(file)
    image.load()

    invert_im = image.convert("RGB")
    invert_im = ImageOps.invert(invert_im)
    image_box = invert_im.getbbox()

    return image.crop(image_box)


def getDirectory():
    return cropped + str(calendar.timegm(time.gmtime()))


def createZipFile(directory, zip_file):
    shutil.make_archive(directory, zipfile_format, directory)
    shutil.move(zip_file, directory)


def uploadToS3Bucket(directory, zip_file):
    client = boto3.client(s3, region_name=region)
    client.upload_file(os.path.join(directory, zip_file), s3_bucket, zip_file)


def deleteSubDirectories(directory):
    files = glob.glob(os.path.join(directory, '*'))
    for file in files:
        if os.path.isdir(file):
            shutil.rmtree(file)


class ImageCrop:
    def __init__(self, files):
        self.files = files

    def cropImages(self):
        number_of_files = len(self.files)
        file_name, file_extension = os.path.splitext(self.files[0].name)
        if number_of_files == 1:
            if file_extension in image_extensions:
                return self.cropImagesForSingleImage()
            else:
                return self.cropImagesForSingleZipFile()
        else:
            if file_extension in image_extensions:
                return self.cropImagesForMultipleImages()
            else:
                return "Error: Multiple zip files is not allowed"

    def cropImagesForSingleImage(self):
        directory = getDirectory()
        zip_file = directory + zipfile_extension
        os.makedirs(directory)

        cropped_image = cropImage(self.files[0])
        cropped_image.save(os.path.join(directory, self.files[0].name))

        createZipFile(directory, zip_file)
        uploadToS3Bucket(directory, zip_file)

        shutil.rmtree(directory)
        return s3_url + zip_file

    def cropImagesForMultipleImages(self):
        directory = getDirectory()
        zip_file = directory + zipfile_extension
        os.makedirs(directory)
        
        for file in self.files:
            cropped_image = cropImage(file)
            cropped_image.save(os.path.join(directory, file.name))

        createZipFile(directory, zip_file)
        uploadToS3Bucket(directory, zip_file)

        shutil.rmtree(directory)
        return s3_url + zip_file

    def cropImagesForSingleZipFile(self):
        directory = getDirectory()
        zipfile_name = directory + zipfile_extension
        os.makedirs(directory)

        zip_file = self.files[0]
        with ZipFile(zip_file, 'r') as zipfile_object:
            zipfile_object.extractall(path=directory)

            for file in zipfile_object.namelist():
                if (not file.startswith(macosx)) and (file.endswith(jpg_extension) or file.endswith(jpeg_extension)
                                                          or file.endswith(png_extension)):
                    cropped_image = cropImage(os.path.join(directory, file))
                    cropped_image.save(os.path.join(directory, os.path.basename(file)))

        deleteSubDirectories(directory)
        createZipFile(directory, zipfile_name)
        uploadToS3Bucket(directory, zipfile_name)

        shutil.rmtree(directory)
        return s3_url + zipfile_name
