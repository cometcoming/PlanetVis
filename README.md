# PlanetVis

Here, I take the sun-mars-earth system that has been tracked and monitored by NASA, using NAIF's kernel APIs tracking each celestial body. We make sure to denote in our code that the sun is the illuminator, Mars the body being observed, and Earth as the observing body. This is all barycenter-focused.

This utilizes NASA's Spiceypy Python wrapper, a library filled with Python tools that can be used for astronomical data analysis. We use this to model the geometry in our sun-mars-earth system and based on distance, sun illumination, and angle of observation find the single best day in the year of 2026 to observe Mars from Earth. 

NOTE: One of the kernels was over 100 MB, so I had to load it in under the "Releases" tab. Be sure to manually download it from there.
