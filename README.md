# Dream_Team_Codes
codes made by the Mecanon's DT




Notes:

1) Data is usually stored as a csv file. Adding a feature to extract the signal from a csv file may be a good idea.

2) Some sensors might not have the capability to store time information. If it only provides the measured information,
   maybe the addition of the creation of the time vector based on the sampling frequency can be useful.
   
3) Is the monitoring by creating an amplitude limit enough? Is there another monitoring option? RMS value?

4) Which sampling frequency would simulate a reasonable sensor?

5) How can the harmonics amplitude be modeled in order to simulate a reasonable sensor?


Progress:

The code is able to generate a signal based on some fundamental frequencies and their harmonics, with the presence of noise.
Along with the possiblity of creating a signal, the code can perform it's FFT.
The monitoring is based on establishing a maximum amplitude value to frequency interval determined by the user.
If the maximum value is exceeded, the program generates an alert message.   