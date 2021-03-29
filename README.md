# Ashpalt9w
Asphalt 9 cliker for windows (<a href="https://drive.google.com/file/d/172qS1R62UkrwzhfaEHCrYhSVB1Ub5Nup/view?usp=sharing">executable version beta</a> <a href="https://tetherscript.s3-us-west-2.amazonaws.com/HVDK/HVDK+Standard_2.1_Installer.exe">Mouse virtual driver</a>)

Usage: python Start.py  
Default folder: NETWORK  
Python version: 3.9.1+

Launch from a different folder: python Start.py [RootFolder StartSubFolder]  
RootFolder - default value 'Images'  
StartSubFolder - Start folder to proccess. Default value 'START'

File name parser rules:  
FileName[FolderName]{TOUT_**500**,TLR_**0.96**,KEY_**Code**}.png (jpg|gif|png)

_FileName_ - Any  
_FolderName_ - Change current folder  
_TOUT_ - time out after action  
_TLR_ - Template searching tolerance  
_KEY_ - Press some key instead left click 


**Basic scheme of the principle of operation**  
<img src="https://github.com/yaldabaoth444/Ashpalt9w/blob/main/base-processing.png" alt="Сurrent algorithm" width="800" height="477">

**The algorithm can be anything you like**  
<img src="https://github.com/yaldabaoth444/Ashpalt9w/blob/main/%D0%A1urrent%20algorithm.png" alt="Сurrent algorithm" width="766" height="800">

**Python version console output example**  
<img src="https://github.com/yaldabaoth444/Ashpalt9w/blob/main/Console.png" alt="Сurrent algorithm" width="687" height="443">

**Executable version output exmple (WinForms .Net 4.5.2)**  
<img src="https://github.com/yaldabaoth444/Ashpalt9w/blob/main/windows version.png" alt="Сurrent algorithm" width="659" height="628">
