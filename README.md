# Ashpalt9w
Asphalt 9 cliker for windows (+ required <a href="https://tetherscript.s3-us-west-2.amazonaws.com/HVDK/HVDK+Standard_2.1_Installer.exe">Mouse virtual driver</a>)  
Data sample made for window size width: 3230  height: 1552 (see in app log)


File name parser rules:  
Data/Scenario/Step/FileName[STEP]{OPTIONS}.png  

_Data_ - directory containing the scripts  
_Scenario_ - Script title  
_Step_ - Script steps  
_FileName_ - Any  
_STEP_ - Next scenario step  
OPTIONS: (comma separated options)  
* _TOUT_ - timeout after action in milleseconds (ex: TOUT_500)  
* _TLR_ - Template searching tolerance (ex: TLR_0.8)  
* _KEY_ - Press some key instead left click (ex: KEY_ESCAPE) <a href="https://github.com/yaldabaoth444/Asphalt9w/blob/main/Readme/key-codes.txt">key-codes</a>  
* _LOC_ - The location of the image you are looking for (ex: LOC_BR40 which means bottom right 40% of screen).<br>B - bottom, T - top, L - left, R - right  
* _AREA_ - Describes the area of the image, where XY is the upper left corner, WH is the area size (ex: AREA_X1300Y300W650H155)  

**Basic scheme of the principle of operation**  
<img src="https://github.com/yaldabaoth444/Ashpalt9w/blob/main/Readme/base-processing.png" alt="Сurrent algorithm" width="800" height="477">

**The algorithm can be anything you like**  
<img src="https://github.com/yaldabaoth444/Ashpalt9w/blob/main/Readme/%D0%A1urrent%20algorithm.png" alt="Сurrent algorithm" width="766" height="800">

**Executable version output exmple (WinForms .Net 4.5.2)**  
<img src="https://github.com/yaldabaoth444/Ashpalt9w/blob/main/Readme/windows version.png" alt="Сurrent algorithm" width="659" height="628">
