# Automate updating catalogue information

##  Introduction

The project code shows the python modules employed by an online fruit store to accomplish the following goals:

[========]

- **Convert the data supplied by the suppliers, in .TIF format for the image and .txt for the description of the product, to smaller .JPEG images and the text to HTML file that shows the image and the product description.**

- **Upload the contents of the HTML file to web service running the company's online website using Django server.**

- **Notify the suppliers with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email includes a PDF attachment with the name of the fruit and its total weight.**

- **Run health check of the system and send an email notification if something goes outside the acceptable metric range.**
