# Low Dropout Linear Regulator

## Regulator
- Choose of LT3010 LDO volatge regualtor for the given project, this component was chosen from the website suggested from apply the circuit parameters. Datasheet for which is attached.

    ![image](https://user-images.githubusercontent.com/114356023/235420108-778e96f2-1322-46ca-9bd9-9924904c83e6.png)

## Calculations
1. ![image](https://user-images.githubusercontent.com/114356023/235420275-c2e62735-2461-48a7-b590-db5f4ebd965c.png)

    Rise in temperature = thermal resistance x Power dissipation

2. ![image](https://user-images.githubusercontent.com/114356023/235420428-0c448e76-8cef-4c97-9f32-d161caaab8e3.png)

    -  Choose R1 =100k, which should be less than 250k to minimize the errors in the output voltage caused by the ADJ pin bias current as per datasheet.
    -  Choose C1= 0.1uF, Because the impedance of C1 at 10khz should be less than R1 as per the datasheet. This capacitance is used for the stabilization purpose.
    - From the formula number 2, we get the value of R2 as 41.02k for the output voltage of 1.8V.
3. ![image](https://user-images.githubusercontent.com/114356023/235420545-f7552ef8-c0f8-4d7b-9683-c93fa7afd87a.png)

4. ![image](https://user-images.githubusercontent.com/114356023/235420579-20a2c8c1-346c-4d13-a657-f866f323a014.png)

## Simulations
1. <b>Turn on and turn off simulation(for_on_and_off.asc)</b>
- In this simulation, we are trying to plot the transient curve when the volatge regulator is turned on and off.
-  In this case a voltage controlled switch is used between the output voltage of the regulator and the load.
- The controlled voltage of this switch sweeps between -3v to +3v to turn the off and on the switch respectively. The input voltage to the regulator is 5V DC and output voltage is kept at 1.8v.
- From the attached waveform screenshot, transients can be viewed for both turn on and off. the plot includes input voltage, output voltage, load current(25 mA for 72 ohm), and the controlling voltage for the switch.
2. <b>Load regulation simulation(for_load_regulation.asc)</b>
-  In this simulation, we are varying the load from 72 ohms to 1.8k ohms thereby acheiving the current from 1mA to 25mA for the given 1.8V output voltage.
- A variable resistor is used at the load to vary the load for the constant input and output volatge.
- The attached waveform includes input voltage, output voltage and load current for different sets of loads(72 ohms to 1.8k ohms).
- Please zoom in the output voltage once you simulate to seen the change in output voltage for different sets of load.
3. <b>Line regulation simulation(for_line_regulation.asc)</b>
- In this simulation, we are varying the input voltage from 5v to 10v, we could have also used DC sweep option but here we will go with varying input supply voltage.
- Input supply with PWL option is used to vary the voltage range.
- The load resistance is fixed at 72 ohms, to simulate a current of 25mA at output voltage of 1.8V.
- The attached wavefom includes input and output voltages, one can see a slight change in the output voltage for the input change.

## Python program
- First part of the python code includes the calculation of load and line regulation, formulaes for which is given above( formula 3 and 4).
- Read the value of No load and full load voltage from the user and using the formula, output the percentage of the load regulation.
- Similarly for the Line regulation, calculate the change in the output voltage for the given change in input voltage, and using the formula, output the percentage of the line regulation.
- Second part of the code includes the calculatuion for the temperature rise above the ambient temperature, formula for which is given above( formula 1).
- Read the inputs such as maximum current, maximum input voltage and ground pin current from the user and by using the formula calculate the rise in temperature above the ambient temperature.
- Also calculate the maximum temperature which is the summation of temperature rise and the ambient temperature.
