
# Design and development of a hybrid printer for polymer filament and low-melting-point metal filament manufacturing

The present project aims to develop a hybrid printing system capable of
printing both polymeric materials and low-melting-point metals using Fused Filament Fabrication (FFF) technology. 

FFF technology is widely used,
especially at the domestic level, due to its low cost. However, at the industrial level, this process has some disadvantages, mainly related to the types
of materials used. These materials are mostly thermoplastics, which, while
versatile, have low mechanical strength and low thermal and electrical conductivity, limiting their use. 

To address these limitations, this project seeks
to combine the advantages of FFF technology and thermoplastics with the
characteristics of low-melting-point metals.
To achieve this, a dual extrusion printing system was developed, consisting of
one extruder for metal filament and another for polymeric filament, enabling
hybrid printing. This means the printing of polymeric objects with metallic
components in their composition. 

In addition, a small optimization study of
the printing parameters was conducted to evaluate not only the capabilities
of the new system but also the feasibility of low-melting-point metal alloys
for 3D FFF printing, since these alloys have different properties compared to
polymers, such as flowability, wettability, and melting temperature.

Some images of the final prototype can be found in the [Pictures Section](#pictures).

## Description

This repository contains the firmware designed for the "Leapfro Creatr MK4" 3D printer, as well as a Python script for recording the temperatures of each hotend present in it.

The firmware used is based on Marlin version `2.0.7.2`, and it includes all the printer's settings. It's important to note that this firmware should not be used on another printer, as it has been highly customized for this specific project and may cause damage to other printers.

The Python script, on the other hand, was created to record the temperatures of each of the hotends, so that the data obtained can be used for validating the numerical models used during the development of the printing system. Additionally, various records made throughout the project's development can be found in this repository.

## Pictures

<p align="center">
<img src="https://github.com/JoaoF2025/Leapfrog_Creatr_Mk4/assets/101104869/6da4cedb-1e28-49b0-854b-557bec5868ab" width=35% height=35%>
<img src="https://github.com/JoaoF2025/Leapfrog_Creatr_Mk4/assets/101104869/b0a850cb-d490-4812-b202-cf3edf6f7d10" width=35% height=35%>
</p>

<p align="center">
<img align="center" src="https://github.com/JoaoF2025/Leapfrog_Creatr_Mk4/assets/101104869/5dfb409e-accf-4a8a-8c54-731232e46a92" width=35% height=35%>
</p>

## Authors

This project was developed at the Department of Mechanical Engineering of the "Universidade de Aveiro" in order to obtain a Master's degree in Mechanical Engineering.

- [@JoaoF2025](https://github.com/JoaoF2025)

