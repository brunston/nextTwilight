    /// Below, we read in the file, breaking the data into individual arrays///
    
filename = 'SMART_data.txt'
numberOfColumns = 7
data = read(filename,-1,numberOfColumns); // the negative one makes sure all of the rows are read.

   /// Below, we define the columns locations for each data set, then get an array for each data set /// 
    //DONE
colDist = 1               // Distance column, in kiloparsecs (kpc)
colNeutralGas = 2         // Neutral Gas column, in solar masses (m_sun)
colLumB = 3               // Luminosity in the B band, solar luminosities (l_sun)
colLumR = 4               // Luminosity in R band, l_sun
colModelVel = 5           // Velocity column in kilometers/second (kms) 
colCounterRotating = 6    // This velocity array includes counter-rotating elements. 
colVel = 7                // Velocity, modeled to "smooth" the data (kms)
//DONE
radii = data(:,colDist);
velocity = data(:,colVel);
velocityModel = data(:,colModelVel);
neutralGasMass = data(:,colNeutralGas);
luminosityR = data(:,colLumR);
luminosityB = data(:,colLumB);

    /// Below, we use scf(number) and clf(number) to create each of our graphs. Note that after we make one graph, we add 1 to number; this moves us to the next window.
   //DONE
number = 1 
scf(number); // these two commands do "housekeeping" by clearing the plot window.
clf(number);    // these two commands do "housekeeping" by clearing the plot window.
number = number + 1

// plot velocity (km/s) versus distance (kpc) DONE
plot(radii,velocity,'+b','MARKERSIZE', 3)
plot(radii,velocityModel,'m<','MARKERSIZE',3) // two plot commands in the same subplot will display both plots in the same window
xtitle("Plot of Velocity Data and Velocity Model versus Radius","Radius (kpc)","Velocity (m_sun)");

// plot gas mass (m_sun) versus distance (kpc) DONE
scf(number); // these two commands do "housekeeping" by clearing the plot window.
clf(number);    // these two commands do "housekeeping" by clearing the plot window.
number = number + 1
plot(radii,neutralGasMass,'ok','MARKERSIZE', 3)
xtitle("Plot of Neutral Gas Mass versus Radius","Radius (kpc)","Mass (m_sun)");

// plot luminosity (l_sun) versus distance (kpc) DONE
scf(number); // these two commands do "housekeeping" by clearing the plot window.
clf(number);    // these two commands do "housekeeping" by clearing the plot window.
number = number + 1
plot(radii,luminosityR,'vr','MARKERSIZE', 3) // try plotting stellar mass below, instead of stellar luminosity!
xtitle("Plot of Luminosity versus Radius","Radius (kpc)","Luminosity (l_sun)");

//NEXTNEXT NEXTNEXT NEXTNEXT NEXTNEXTNEXT
///  **** QUESTION 1 **** ///
///  **** QUESTION 1 **** ///
///  **** QUESTION 1 **** ///
///  **** QUESTION 1 **** ///

    /// Below, convert luminosity profile into mass profile, assuming a fixed mass to luminosity (ML) ratio ///
    
//MLR1 = //??
//MLR2 = //??

//massStarsR1 = //?
//massStarsR2 = //?

// modify and uncomment lines used above (reproduced below) to try plotting stellar mass, instead of luminosity!
//scf(number); // these two commands do "housekeeping" by clearing the plot window.
//clf(number);    // these two commands do "housekeeping" by clearing the plot window.
//plot(radii,luminosityR,'vr','MARKERSIZE', 3) 
//xtitle("Plot of Stellar Mass versus Radius","Radius (kpc)","Stellar Mass" (l_sun)");

    // Our stellar and neutral gas masses are at each radius, and describe the mass contained from one radius to the next.
//For example, the first gas mass data point is the gas mass contained from a radius of 0 to the first radius of our data set;
//the second point is the mass from radius 1 to radius 2, etc. In order to transform the total mass we find from the rotation
//curve formulae into this kind of "incremental" mass between two radii, we need to find the total mass at each radius and
//subtract the total mass at each previous radius.
    
Grav = 4.28*10.^(-6.) // units of kpc*km^2/(M_sun*s^2).

massEnc = velocityModel.^2..*radii./Grav  // this is the total mass within each radius (from zero) based on the rotation curve formula
indexArray = 2:length(massEnc) // an array starting at 2 and going to the last element of massEnc (ie: from element 2 to n)
incrementalMass(1) = velocityModel(1).^2..*radii(1)./Grav                // we have to define the first element differently, since our data does not have a "zero" velocity. see the above explanation; think about what the incremental mass at the first radius means.
incrementalMass(indexArray) = massEnc(indexArray)-massEnc(indexArray-1)  // subtracts element 1 from element 2 and "continues" until it subtracts element n-1 from element n

// this will plot the incremental mass versus radius 
scf(number); // these two commands do "housekeeping" by clearing the plot window.
clf(number);    // these two commands do "housekeeping" by clearing the plot window.
number = number + 1
plot(radii,incrementalMass,'gd','MARKERSIZE',3)
xtitle("Plot of ""Incremental"" Mass versus Radius","Radius (kpc)","Incremental Mass (m_sun)");

// Below, subtract the observed masses from the total masses to find the dark matter. Overplot the dark mass, total mass, and components of masses in one window

//darkMatter = //??? // Fill in how to find the dark matter, based on the arrays above. How would you change this command to allow for comparing two results?

//scf(number); // these two commands do "housekeeping" by clearing the plot window.
//clf(number);    // these two commands do "housekeeping" by clearing the plot window.
//number = number + 1
//darkMatter = //?? 
//plot(radii,darkMatter //?
//plot(radii,darkMatter //?

//plot(radii,//??)
//plot(radii,//??)

///  **** QUESTION 2 **** ///
///  **** QUESTION 2 **** ///
///  **** QUESTION 2 **** ///
///  **** QUESTION 2 **** ///

//Below, change the galaxies gas component and compare the resulting new galaxy with the old galaxy above.

//gasIonized = //

//gasTotalNew = //

//darkMatterNew = //
//scf(number); // these two commands do "housekeeping" by clearing the plot window.
//clf(number);    // these two commands do "housekeeping" by clearing the plot window.
//number = number + 1
//plot(radii,darkMatterNew)//,??)
//plot(radii,darkMatter,??)
