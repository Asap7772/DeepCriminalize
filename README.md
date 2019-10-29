# DeepCriminalize

#Inspiration

Due to the rise in the number of criminal cases, sketch artists are often unavailable and back-logged. Additionally, some sketches may be highly unrealistic due to a lack of information. To solve this pressing issue, we created an Android app that uses a pg-GAN to render realistic images based off of witness descriptions. This project is highly challenging to implement, but could revolutionize the process of criminal identification by providing realistic images which are more likely to have a match than a sketch when searched across the existing criminal database.

#Aim

We have a mobile interface that allows police officers to set up case files and record and transcribe witness testimony, a database to store witness information, case testimonies, and the generated images, and a server-based backend that is able to take the transcribed testimony, extract descriptions of facial features, and generate an image of the criminal from those descriptions. We are also working on a translation feature that takes in descriptions in any language. In the future we will including classification specific to features such as tattoos to link criminals to gangs/areas, etc.

#Citation

Tero Karras, 2017, Progressive Growing of GANs for Improved Quality, Stability, and Variation

