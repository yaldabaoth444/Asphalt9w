# Ashpalt9w  
**Latest changes**  
![image](https://user-images.githubusercontent.com/25618671/122649742-c7827c00-d148-11eb-8c01-2940e4d8ee77.png)  
<hr>

Asphalt 9 cliker for windows (+ required <a href="https://tetherscript.s3-us-west-2.amazonaws.com/HVDK/HVDK+Standard_2.1_Installer.exe">Mouse virtual driver</a>)  
Data sample made for window size width: 3230  height: 1552 (see in app log). To set|restore the desired window size, I use <a href="http://www.brianapps.net/sizer/">Sizer</a>  
<a href="https://youtu.be/RD9A6wjkkcw">Ford GT hunting example</a>  
<a href="https://youtu.be/GC6x_9_2ci0">Aston Martin V12 Speedster hunting example</a>  

> File name parser rules:  

Data/Scenario/Step/FileName[STEP]{OPTIONS}.png  

- _Data_ - directory containing the scripts  
- _Scenario_ - Script title  
- _Step_ - Script steps. The initial step should be named **START**. The end of the script is reached by referring to the step with the name [**END**]  
- _FileName_ - Any. *Note: if there is the same part in the name before the dot, then a random pattern is chosen* (ex: **any**.CarFord.png, **any**.CarMazda.png, **any**.CarBMW.png)
- _STEP_ - Next scenario step  
- OPTIONS: (comma separated options)  
  * _TOUT_ - Timeout after action in milleseconds (ex: **TOUT_500**) 
  * _LAG_ - Temporarily excludes the pattern from processing after action for a specified time in milleseconds (ex: **LAG_500**)  
  * _TLR_ - Template searching tolerance (ex: **TLR_0.8**). The default tolerance is 0.98  
  * _KEY_ - Press some key instead left click (ex: **KEY_ESCAPE**) <a href="https://github.com/yaldabaoth444/Asphalt9w/blob/main/Readme/key-codes.txt">key-codes</a>  
  * _LOC_ - The location of the image you are looking for (ex: **LOC_BR40** which means bottom right 40% of screen). B - bottom, T - top, L - left, R - right  
  * _AREA_ - Describes the search area in the image, where XY is the upper left corner, WH is the area size (ex: **AREA_X1300Y300W650H155**)  

> Script file format:  

Each line refers to a script with number of repetitions (ex: **[HUNT] x5**)  

**How it works**  
<img src="https://github.com/yaldabaoth444/Ashpalt9w/blob/main/Readme/base-processing.png" alt="Сurrent algorithm" width="800" height="477">

**The algorithm can be anything you like**  
<img src="https://github.com/yaldabaoth444/Ashpalt9w/blob/main/Readme/%D0%A1urrent%20algorithm.png" alt="Сurrent algorithm" width="766" height="800">

**Executable version output exmple (WinForms .Net 4.5.2)**  
<img src="https://github.com/yaldabaoth444/Ashpalt9w/blob/main/Readme/windows version.png" alt="Сurrent algorithm" width="823" height="868">
